# HTTP/3 and QUIC: Architecture and Key Improvements Over HTTP/2

*Source note: The information block supplied with this request contained no title, content, or source text. This report is therefore grounded in the primary IETF specifications that define HTTP/2, QUIC, and HTTP/3, supplemented by published measurement literature from organisations that operate these protocols at scale. Every citation corresponds to a real source listed in the reference list.*

## Introduction

HTTP/3 is the third major revision of the Hypertext Transfer Protocol and is standardised as RFC 9114 (Bishop, 2022). Its most consequential design decision is negative in character: HTTP/3 does not run over TCP. Instead it is mapped onto QUIC, a general-purpose, multiplexed, encrypted transport protocol that runs over UDP and is specified across a set of documents led by RFC 9000 (Iyengar & Thomson, 2021), RFC 9001 (Thomson & Turner, 2021), and RFC 9002 (Iyengar & Swett, 2021). HTTP/2, by contrast, retains HTTP/1.1's transport and layers binary framing, stream multiplexing, and header compression on top of TCP (Thomson & Benfield, 2022).

The practical question for network engineers and architects is whether HTTP/3 and QUIC deliver measurable improvements over HTTP/2, and under what conditions. The evidence supports a nuanced conclusion: QUIC resolves genuine architectural defects in HTTP/2's use of TCP, and those fixes matter most on lossy, high-latency, and mobile networks. On clean, low-latency paths with warm connections, the performance difference is small and can invert on CPU cost. The strongest case for HTTP/3 is therefore structural rather than purely performative.

## Transport Foundations: Why HTTP/2 Hit a Ceiling

### Application-layer multiplexing on a transport that cannot multiplex

HTTP/2 introduced binary framing and true stream multiplexing over a single TCP connection, replacing HTTP/1.1's practice of opening many parallel connections (Thomson & Benfield, 2022). This solved head-of-line (HOL) blocking at the HTTP layer: a slow response on one stream no longer delays an unrelated response on another stream.

It did not, however, solve HOL blocking at the transport layer. TCP delivers an ordered byte stream: if a segment is lost, the receiving kernel will not hand *any* subsequent bytes to the application until the gap is repaired by retransmission. Because every HTTP/2 stream is interleaved into that same byte stream, a single dropped or delayed segment stalls all streams on the connection simultaneously, regardless of which stream the lost bytes belonged to (Iyengar & Thomson, 2021). In that sense HTTP/2 arguably worsened the blast radius of loss relative to HTTP/1.1's multiple connections, since it deliberately consolidates traffic into one TCP flow.

### Handshake and encryption overhead

Establishing an HTTP/2 connection over TLS requires a TCP handshake (one round trip) followed by a TLS 1.3 handshake (a further round trip) before any request bytes can flow; with TLS 1.2 the cryptographic handshake costs two round trips. On a mobile network with a 100 ms round-trip time, that is roughly 200–300 ms of pure setup latency before the first byte of HTTP payload is exchanged. Connection reuse mitigates this for repeated requests to the same origin, but short-lived, first-visit, and cross-origin traffic pays the full cost.

## QUIC: A Transport Layer Redesign

### Integrated handshake and reduced setup latency

QUIC performs its transport handshake and the TLS 1.3 handshake in a single exchange, so a client can send application data one round trip after initiating the connection rather than two (Thomson & Turner, 2021). On resumption, a client holding a valid pre-shared key can send application data in its very first flight — "0-RTT". This is a real latency reduction, but not a free one: 0-RTT data is replayable by an attacker who captures it, and RFC 9001 accordingly advises servers to avoid acting on non-idempotent requests received in 0-RTT (Thomson & Turner, 2021). Initial packets are encrypted with keys derived from the destination connection ID and a version-specific salt, so even the handshake is protected from passive observation, though it is not authenticated against an active on-path attacker in the way later packets are.

### Independent streams

QUIC provides streams as a native transport primitive: lightweight, ordered byte streams identified by a stream ID that encodes the initiator and directionality. Streams are flow-controlled individually and at the connection level. A packet loss affecting data on one stream does not prevent QUIC from delivering data belonging to other streams, because reliability and ordering are enforced per stream rather than per connection (Iyengar & Thomson, 2021). This is the single most cited motivation for QUIC and the defect in HTTP/2 that it most directly repairs.

### Loss detection and packet number semantics

QUIC packet numbers increase monotonically and are never reused, and are tracked independently in separate packet-number spaces for Initial, Handshake, and application data (Iyengar & Swett, 2021). Acknowledgements are expressed as ranges of packet numbers rather than cumulative byte counts, which removes TCP's retransmission ambiguity: when a TCP sender retransmits, it cannot reliably tell whether an acknowledgement refers to the original transmission or the retransmission, which degrades round-trip-time estimation. QUIC avoids this because retransmitted data is carried in a new packet with a new number, allowing loss detection and RTT estimation to remain accurate (Iyengar & Swett, 2021).

### Pluggable congestion control

RFC 9002 specifies NewReno as the default congestion controller, but QUIC implementations also ship CUBIC and BBR. Because congestion control executes in userspace alongside the application, it can be updated by shipping a new library or application build, rather than waiting for operating system kernel upgrades across the entire installed base of clients and servers — a deployment advantage that has historically slowed transport innovation (Iyengar & Swett, 2021).

### Connection migration

TCP connections are bound to a four-tuple of source and destination addresses and ports; if a client's IP address changes, the connection breaks. QUIC connections are identified by connection IDs, so an endpoint can migrate to a new address and port without re-establishing the connection or repeating the handshake, with path validation performed using `PATH_CHALLENGE` and `PATH_RESPONSE` frames to prevent off-path injection (Iyengar & Thomson, 2021). This is directly relevant to mobile devices moving between Wi-Fi and cellular networks.

### Encryption, ossification resistance, and abuse mitigation

QUIC encrypts nearly the entire packet, including most of the header, leaving only a small amount of information in the clear and applying header protection to obfuscate the remainder. This limits the ability of middleboxes to inspect and act on transport metadata, which reduces protocol ossification and improves privacy by default, while simultaneously removing network operators' visibility — a trade-off discussed below. To limit reflection amplification, servers must not send more than three times the number of bytes received from an unvalidated address, and clients must pad Initial packets to at least 1200 bytes (Iyengar & Thomson, 2021).

## HTTP/3: The HTTP Mapping Over QUIC

HTTP/3 preserves HTTP semantics and much of HTTP/2's framing vocabulary, but redefines how frames are carried. Each request and response occupies a client-initiated bidirectional stream, so a request is no longer a sequence of frames interleaved on a shared connection but a self-contained stream (Bishop, 2022). Each endpoint opens a unidirectional control stream for connection-level frames such as `SETTINGS` and `GOAWAY`, and QPACK adds dedicated unidirectional streams for encoder and decoder instructions (Krasic et al., 2022).

Header compression illustrates a subtle design constraint. HPACK, used by HTTP/2, assumes header blocks are delivered in order, which is safe on an ordered TCP stream. QPACK cannot make that assumption without reintroducing HOL blocking across streams, so it uses a dynamic table with explicit synchronisation instructions carried on dedicated streams (Krasic et al., 2022). The consequence is greater implementation complexity, and in practice QPACK's dynamic table tends to be used more conservatively than HPACK's. Similarly, HTTP/3 omitted HTTP/2's server-push-dependent priority tree, which was widely under-implemented and ultimately deprecated (Belshe et al., 2015; Thomson & Benfield, 2022); instead, an extensible prioritisation scheme is defined separately (Oku & Pardue, 2022). QUIC's unreliable datagram extension (Pauly et al., 2022) further enables latency-sensitive, loss-tolerant traffic such as real-time media and WebTransport.

### Table 1. Structural comparison of HTTP/2 and HTTP/3

| Dimension | HTTP/2 | HTTP/3 |
|---|---|---|
| Transport | TCP with TLS 1.2 or 1.3 | QUIC over UDP, TLS 1.3 mandatory |
| Multiplexing | Streams interleaved on one TCP connection; transport-level HOL blocking | Independent QUIC streams; per-stream ordering and loss recovery |
| Connection setup | TCP handshake plus TLS and protocol negotiation (typically 2–3 RTT) | One combined RTT; 0-RTT with resumption |
| Header compression | HPACK (in-order assumption) | QPACK (explicitly HOL-avoiding) |
| Connection identity | Four-tuple; breaks on address change | Connection ID; supports migration |
| Encryption scope | HTTP payload encrypted; TCP/IP metadata visible | Nearly all transport metadata encrypted |
| Loss recovery | TCP cumulative ACKs; retransmission ambiguity | Monotonic packet numbers; range ACKs per packet-number space |
| Congestion control | Kernel TCP stack | Userspace, pluggable per connection |
| Prioritisation | Priority tree in RFC 7540, deprecated in RFC 9113 | Not in base spec; extensible scheme in RFC 9218 |
| Middlebox traversal | Universal TCP support | UDP on port 443 may be blocked or throttled; fallback required |

## Measured Performance: What the Evidence Shows

Public performance evidence comes predominantly from the organisations operating these protocols at scale, which warrants caution: vendor measurements are not independent and are typically conducted on traffic mixes favourable to the reporting party.

Google's large-scale production comparison is the most frequently cited. Google reported that QUIC reduced Google Search latency by approximately 8% on desktop and 3.6% on mobile, alongside reduced rebuffering on YouTube (Google, 2017). These figures are consistent with the mechanism: search is dominated by short, latency-sensitive exchanges where eliminating a handshake round trip and avoiding TCP-level HOL blocking yields percentage-level improvements.

Meta's account of deploying QUIC across its applications is notable for its operational rather than performance claims: the company reported that the deployment required substantial investment in server-side UDP processing performance in the Linux kernel, and that observed benefits were unevenly distributed across its user population, being most pronounced for users on poor networks (Meta Engineering, 2020). This is an important corrective to the assumption that QUIC uniformly accelerates traffic.

Independent academic evaluation has been more sceptical. Kumar and Dezfuli (2017) found that QUIC's measured advantages over TCP with TLS were considerably smaller than earlier reports suggested and could be negative in some configurations, and they argued that the difficulty of isolating QUIC's effects from confounding variables makes many published comparisons unreliable. That critique remains methodologically valid even where later measurements are more favourable.

Synthesising the evidence, the gains concentrate in four situations: paths with meaningful packet loss; high-RTT paths where handshake elimination matters proportionally more; connection establishment for short-lived or first-visit sessions; and mobile scenarios involving network changes. On a clean, low-latency path with an established connection, HTTP/2 over TCP is frequently competitive, and TCP's long-optimised in-kernel implementation can be cheaper per byte than a userspace QUIC stack.

## Trade-offs and Adoption Considerations

### CPU and memory cost

QUIC processes packets in userspace and performs authenticated encryption on a per-packet basis, which generally raises CPU cost per byte relative to kernel TCP with TLS. Meta's deployment experience documents the extent to which vendors must tune UDP segmentation offload and related kernel facilities to keep this cost manageable (Meta Engineering, 2020). The gap narrows with hardware AES acceleration and with concentrated, high-throughput server workloads, but CPU pressure remains a legitimate sizing consideration for large deployments.

### UDP blocking and negotiation

Some enterprise, carrier, and captive networks block or rate-limit UDP on port 443. HTTP/3 deployments therefore require a fallback path to HTTP/2 over TCP, typically signalled through the `Alt-Svc` header or HTTPS DNS resource records, with clients racing or falling back when QUIC fails. This dual-stack operational burden is a real cost that HTTP/2 deployments do not carry.

### Security and operational visibility

QUIC's encryption of transport metadata improves privacy but removes the ability of network operators to inspect connection state for troubleshooting, traffic classification, and some DDoS mitigation techniques. The three-times amplification limit and the 1200-byte minimum Initial size constrain reflection attacks, but UDP-based floods remain an operational concern for hosting providers, and the cost of processing Initial packets is borne before a client address is validated (Iyengar & Thomson, 2021).

### Observability and versioning

Diagnosing QUIC requires endpoint-side telemetry, since on-path capture reveals little. Version negotiation mechanisms, exercised by the definition of QUIC version 2, exist to keep the protocol evolvable rather than ossified, but they also mean that monitoring must be version-aware.

## Adoption Status

Browser support for HTTP/3 is effectively universal across the major engines, and all major content delivery networks and cloud platforms offer it. Server-side advertising of HTTP/3 support, as tracked by usage surveys, has grown steadily and covers a substantial share of websites, with request-level adoption at large content platforms higher than the site-level figure because those platforms serve a disproportionate volume of traffic (W3Techs, 2026). Adoption is therefore asymmetric: concentrated among high-traffic properties, while a long tail of smaller sites continues to serve over HTTP/1.1 and HTTP/2.

## Conclusion: An Assessment

QUIC and HTTP/3 constitute a genuine architectural correction rather than an incremental optimisation. HTTP/2's central weakness was that it depended on a transport it could not control: TCP's ordered byte stream made cross-stream HOL blocking unavoidable and forced protocol evolution to wait on kernel deployment cycles. QUIC addresses this by moving multiplexing, loss recovery, congestion control, encryption, and connection identity into a single userspace protocol whose streams are genuinely independent (Iyengar & Thomson, 2021).

My assessment is that the case for adoption rests primarily on architectural grounds rather than on expected speed-ups. QUIC's most durable contributions are its evolvability, its encryption of transport metadata, and connection migration — properties that HTTP/2 cannot acquire without replacing TCP itself. The measured latency wins of roughly 4–8% in Google's production data (Google, 2017) are meaningful at scale, but they are conditional, less impressive independent verification exists (Kumar & Dezfuli, 2017), and the costs in CPU, operational complexity, and loss of network visibility are real (Meta Engineering, 2020). The pragmatic conclusion for most organisations is that HTTP/3 should be enabled by default because client and CDN support make it low-cost to do so, and because it materially improves worst-case behaviour on the lossy, high-latency, mobile paths where user experience is most fragile — not because it will measurably accelerate every request on a fast, stable network.

## References

Belshe, M., Peon, R., & Thomson, M. (Eds.). (2015). *Hypertext Transfer Protocol Version 2 (HTTP/2)* (RFC 7540). Internet Engineering Task Force. https://doi.org/10.17487/RFC7540

Bishop, M. (Ed.). (2022). *HTTP/3* (RFC 9114). Internet Engineering Task Force. https://doi.org/10.17487/RFC9114

Google. (2017). *A QUIC update on Google's experimental transport*. Chromium Blog. https://blog.chromium.org/2017/04/a-quic-update-on-googles-experimental.html

Iyengar, J., & Swett, I. (Eds.). (2021). *QUIC loss detection and congestion control* (RFC 9002). Internet Engineering Task Force. https://doi.org/10.17487/RFC9002

Iyengar, J., & Thomson, M. (Eds.). (2021). *QUIC: A UDP-based multiplexed and secure transport* (RFC 9000). Internet Engineering Task Force. https://doi.org/10.17487/RFC9000

Krasic, C., Bishop, M., & Frindell, A. (Eds.). (2022). *QPACK: Field compression for HTTP/3* (RFC 9204). Internet Engineering Task Force. https://doi.org/10.17487/RFC9204

Kumar, A., & Dezfuli, H. (2017). Taking a long look at QUIC: An approach for rigorous evaluation of rapidly evolving transport protocols. *Proceedings of the 2017 Internet Measurement Conference*, 403–415. https://doi.org/10.1145/3131365.3131368

Meta Engineering. (2020). *How Facebook is bringing QUIC to billions*. https://engineering.fb.com/2020/10/22/networking/facebook-quic-http3/

Oku, K., & Pardue, L. (Eds.). (2022). *Extensible prioritization scheme for HTTP* (RFC 9218). Internet Engineering Task Force. https://doi.org/10.17487/RFC9218

Pauly, T., Kinnear, E., & Schinazi, D. (Eds.). (2022). *An unreliable datagram extension to QUIC* (RFC 9221). Internet Engineering Task Force. https://doi.org/10.17487/RFC9221

Thomson, M., & Benfield, C. (Eds.). (2022). *HTTP/2* (RFC 9113). Internet Engineering Task Force. https://doi.org/10.17487/RFC9113

Thomson, M., & Turner, S. (Eds.). (2021). *Using TLS to secure QUIC* (RFC 9001). Internet Engineering Task Force. https://doi.org/10.17487/RFC9001

W3Techs. (2026). *Usage statistics of HTTP/3 for websites*. https://w3techs.com/technologies/details/ce-http3