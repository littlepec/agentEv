# HTTP/3 and QUIC: Architecture, Mechanisms, and Improvements over HTTP/2

## Introduction

HTTP/3 is the third major version of the Hypertext Transfer Protocol and the first version to abandon TCP as its transport substrate. Rather than layering HTTP semantics over a single ordered byte stream, HTTP/3 maps those semantics onto QUIC, a general-purpose, UDP-based transport that provides stream multiplexing, per-stream flow control, low-latency connection establishment, and network path migration ([Iyengar & Thomson, 2021](https://doi.org/10.17487/RFC9000); [Bishop, 2022](https://doi.org/10.17487/RFC9114)). The design goal is explicit in the HTTP/3 specification, which notes that QUIC already offers several features that HTTP/2 had to approximate at the application layer, such as multiplexing, per-stream flow control, and faster connection setup, and that HTTP/3 therefore identifies which HTTP/2 mechanisms have been subsumed by the transport ([Bishop, 2022](https://doi.org/10.17487/RFC9114)).

This report examines the technical rationale for HTTP/3, the architecture of QUIC, and the specific improvements it delivers relative to HTTP/2, while also assessing the trade-offs and operational limitations that remain.

## From HTTP/1.1 to HTTP/2: The Problem HTTP/3 Addresses

HTTP/1.1 delivers one response at a time per connection in practice, and its optional pipelining mechanism was never widely or correctly deployed, leading browsers to open multiple parallel TCP connections per origin as a workaround. HTTP/2, standardized initially as RFC 7540 and later revised as RFC 9113, introduced a binary framing layer, true stream multiplexing over a single connection, header field compression via HPACK, stream prioritization, and server push ([Thomson & Benfield, 2022](https://doi.org/10.17487/RFC9113); [Peon & Ruellan, 2015](https://doi.org/10.17487/RFC7541)).

HTTP/2 solved the application-layer concurrency problem but inherited a fundamental constraint from TCP: TCP presents an ordered byte stream, so if a single segment is lost or delayed, all bytes behind it are withheld from the receiving application regardless of which stream they belong to. This is transport-layer head-of-line (HOL) blocking, and it means a loss affecting one HTTP/2 stream stalls every other stream sharing the connection; independent measurements commonly show measurable loss-related latency penalties for such workloads. HPACK compounds the problem because its stateful dynamic table requires header blocks to be decoded in the order they were encoded, so a lost packet can delay header decompression for subsequent requests as well ([Krasic et al., 2022](https://doi.org/10.17487/RFC9204)).

## QUIC: A New Transport Protocol

### Placement in the Protocol Stack

QUIC is a UDP-based multiplexed and secure transport defined in RFC 9000 ([Iyengar & Thomson, 2021](https://doi.org/10.17487/RFC9000)). Running over UDP allows QUIC to be deployed on existing operating systems and networks without kernel or middlebox changes, while the protocol itself reimplements and improves upon the connection-oriented features that TCP provides: reliability, congestion control, flow control, and connection state. QUIC packets use long headers during connection establishment and short headers afterwards, and each packet carries an explicit packet number and a connection ID.

### Integrated TLS 1.3 Encryption

QUIC integrates TLS 1.3 directly as its cryptographic handshake rather than layering it on top of a finished transport handshake ([Thomson & Turner, 2021](https://doi.org/10.17487/RFC9001); [Rescorla, 2018](https://doi.org/10.17487/RFC8446)). The TLS handshake is carried in QUIC CRYPTO frames and produces distinct encryption levels for Initial, 0-RTT, Handshake, and 1-RTT packets. Packet numbers are protected and payloads are authenticated with AEAD, and QUIC provides no plaintext mode. The consequence is that almost all transport metadata is invisible to intermediaries, which both improves privacy and reduces protocol ossification — the tendency of middleboxes to harden assumptions about a protocol's wire image, a documented source of deployment difficulty for TCP-based protocols ([Iyengar & Thomson, 2021](https://doi.org/10.17487/RFC9000)).

### Connection Establishment: 1-RTT and 0-RTT

Because the transport and cryptographic handshakes are combined into a single exchange, QUIC can establish a usable connection in one round trip for a new connection and in zero round trips for a resumed connection in which the client has a valid ticket and can send early data ([Thomson & Turner, 2021](https://doi.org/10.17487/RFC9001)). By contrast, HTTP/2 over TLS 1.3 requires the TCP handshake (one round trip) before the TLS handshake (one more round trip) can complete, and HTTP/2 over TLS 1.2 typically requires two round trips for TLS alone. The comparison is summarized below.

| Connection scenario | Transport/crypto round trips before first request | Notes |
|---|---|---|
| HTTP/2 over TCP + TLS 1.2 | 3 | TCP handshake plus 2-RTT TLS 1.2 handshake |
| HTTP/2 over TCP + TLS 1.3 | 2 | TCP handshake plus 1-RTT TLS 1.3 handshake |
| HTTP/3 (QUIC, new connection) | 1 | Combined transport and TLS 1.3 handshake |
| HTTP/3 (QUIC, resumption) | 0 | Early data within the constraints of replay protection |

Zero-RTT data carries inherent replay risk, and the specification restricts its use to data the application is willing to send without a freshness guarantee ([Thomson & Turner, 2021](https://doi.org/10.17487/RFC9001)).

### Streams, Multiplexing, and the Removal of Transport-Level HOL Blocking

QUIC defines streams as lightweight, independently ordered sequences of bytes that can be unidirectional or bidirectional, with both stream-level and connection-level flow control ([Iyengar & Thomson, 2021](https://doi.org/10.17487/RFC9000)). Because each stream's data is reassembled and delivered independently, the loss of a datagram carrying data for one stream does not prevent the delivery of data belonging to other streams — the primary structural advantage over HTTP/2 over TCP. An important qualification is that all streams on a connection share a single congestion controller and a single end-to-end path, so a loss event still reduces the congestion window for the whole connection; QUIC removes ordering-induced blocking, not the shared-bandwidth characteristics of a single path ([Iyengar & Swett, 2021](https://doi.org/10.17487/RFC9002)).

### Connection Migration

QUIC identifies a connection by a connection ID rather than by the four-tuple of source and destination addresses and ports ([Iyengar & Thomson, 2021](https://doi.org/10.17487/RFC9000)). This permits connection migration: a client that changes networks, for example moving from Wi-Fi to cellular, or that is remapped by a NAT, can continue an existing connection on a new path. QUIC validates new paths before committing to them and supports explicit opt-out via migration-disabling options, along with server-preferred addressing. HTTP/2, bound to a TCP four-tuple, must re-establish the connection from scratch in these situations, paying the full handshake and warm-up cost again.

### Loss Detection, Congestion Control, and Packet Number Design

QUIC's loss detection and congestion control are specified separately in RFC 9002 ([Iyengar & Swett, 2021](https://doi.org/10.17487/RFC9002)). Because every QUIC packet has a monotonically increasing packet number that is never reused — even for retransmissions — QUIC avoids the retransmission ambiguity that complicates TCP round-trip-time estimation and loss detection. QUIC acknowledgements can describe ranges of received packets and carry acknowledgement delays and optional timestamps, giving senders richer signals for estimating RTT and distinguishing congestion loss from reordering. The specification defines a NewReno-style default congestion controller, while the transport is designed to accommodate alternatives such as CUBIC and BBR, and it supports features such as ECN feedback and pacing.

### Security and Resilience Mechanisms

QUIC includes address validation, an anti-amplification limit that restricts a server to sending at most three times the bytes it has received from an unvalidated address, Retry packets, and stateless resets ([Iyengar & Thomson, 2021](https://doi.org/10.17487/RFC9000)). Version 2 of QUIC was later standardized with a different initial salt and packet-type codepoint mapping, thereby making it less likely that network devices will hard-code assumptions about version 1 packets ([Duke, 2023](https://doi.org/10.17487/RFC9369)).

## HTTP/3: HTTP Semantics over QUIC

### Stream Mapping and Framing

HTTP/3 retains HTTP semantics — methods, status codes, header fields, and the request/response exchange model — but remaps them onto QUIC's streams ([Bishop, 2022](https://doi.org/10.17487/RFC9114)). Each request and response pair occupies a client-initiated bidirectional stream; a control stream carries connection-level frames such as SETTINGS and GOAWAY; and dedicated unidirectional streams carry QPACK encoder and decoder instructions. HTTP/3 frames include HEADERS, DATA, SETTINGS, GOAWAY, and PUSH_PROMISE, and the frame definitions are redefined for QUIC's stream model rather than reusing HTTP/2's framing.

### QPACK Header Compression

QPACK was designed to replace HPACK for use over QUIC ([Krasic et al., 2022](https://doi.org/10.17487/RFC9204)). It retains a static table and an optional dynamic table, but it separates the insertion of dynamic entries from their reference by using encoder and decoder instruction streams, and it allows endpoints to declare the number of streams that may block while awaiting dynamic table state. This structure is compatible with out-of-order stream delivery and avoids the requirement that all streams wait on a single in-order byte stream, as HPACK implies. Implementations may also restrict themselves to the static table to eliminate dynamic-table dependencies entirely.

### Discovery and Deployment Signaling

Clients learn that an origin supports HTTP/3 through the Alt-Svc response header or through HTTPS and SVCB DNS resource records ([Nottingham et al., 2016](https://doi.org/10.17487/RFC7838); [Schwartz et al., 2023](https://doi.org/10.17487/RFC9460)). This out-of-band discovery mechanism is essential because HTTP/3 runs on UDP, which is not universally reachable, and it allows clients to attempt QUIC while retaining a working HTTP/2 or HTTP/1.1 path.

### Server Push and Datagrams

HTTP/3 retains the PUSH_PROMISE construct in its specification ([Bishop, 2022](https://doi.org/10.17487/RFC9114)), but browser support has been withdrawn: Chrome removed support for server push in version 106, citing limited practical benefit and complexity ([Chromium, 2022](https://developer.chrome.com/blog/removing-push)). HTTP/3 also gains a capability HTTP/2 lacks on TCP: an unreliable datagram service, defined for HTTP, that allows latency-sensitive data to be sent without retransmission guarantees ([Pauly et al., 2022](https://doi.org/10.17487/RFC9297)).

## Comparative Summary

| Dimension | HTTP/2 | HTTP/3 |
|---|---|---|
| Transport | TCP | QUIC over UDP ([Iyengar & Thomson, 2021](https://doi.org/10.17487/RFC9000)) |
| Encryption | TLS optional over TCP | TLS 1.3 integrated; no plaintext mode ([Thomson & Turner, 2021](https://doi.org/10.17487/RFC9001)) |
| New-connection setup | 2 RTT minimum with TLS 1.3 | 1 RTT |
| Resumption | Session resumption with TCP setup; 0-RTT requires TCP Fast Open | 0-RTT supported natively ([Thomson & Turner, 2021](https://doi.org/10.17487/RFC9001)) |
| Multiplexing | Application-layer streams over one ordered byte stream | Native transport streams ([Bishop, 2022](https://doi.org/10.17487/RFC9114)) |
| Loss-induced HOL blocking | Affects all streams on the connection | Eliminated across streams; congestion effects remain shared ([Iyengar & Swett, 2021](https://doi.org/10.17487/RFC9002)) |
| Header compression | HPACK, order-dependent dynamic table | QPACK, designed for out-of-order delivery ([Krasic et al., 2022](https://doi.org/10.17487/RFC9204)) |
| Connection identity | IP address and port four-tuple | Connection ID, enabling migration ([Iyengar & Thomson, 2021](https://doi.org/10.17487/RFC9000)) |
| Ossification resistance | Limited; TCP headers visible to middleboxes | Transport metadata encrypted, versions negotiated ([Duke, 2023](https://doi.org/10.17487/RFC9369)) |
| Unreliable data | Not supported | HTTP datagrams supported ([Pauly et al., 2022](https://doi.org/10.17487/RFC9297)) |

## Performance and Deployment Evidence

The largest early source of deployment evidence came from Google, which reported that running QUIC in production produced measurable latency and quality-of-experience improvements for services such as Search and YouTube, with the largest benefits observed for users on lossy or high-latency paths ([Langley et al., 2017](https://doi.org/10.1145/3098822.3098842)). Those results are consistent with the protocol's structural advantages: fewer round trips at connection setup, the absence of transport-level head-of-line blocking, and better loss signals. Because the gains depend heavily on network conditions, distance to the server, connection reuse patterns, and client behaviour, published improvements vary considerably across studies and should be read as context-dependent rather than universal.

Adoption has grown steadily. Website-technology surveys record HTTP/3 usage rising from negligible levels after its 2019 drafts to a substantial share of sites by the mid-2020s ([W3Techs, 2026](https://w3techs.com/technologies/details/ce-http3)), and major content delivery networks report that a large and increasing proportion of client requests arrive over HTTP/3 where it is enabled ([Cloudflare, n.d.](https://www.cloudflare.com/learning/performance/what-is-http3/)). Broad support in browsers, CDNs, and server frameworks has made HTTP/3 a default-capable option rather than an experimental one.

## Limitations and Trade-Offs

Several caveats temper the picture. First, QUIC depends on UDP, and some enterprise firewalls and networks block or rate-limit UDP traffic; clients therefore require a fallback path to HTTP/2 or HTTP/1.1, and the discovery mechanisms described above exist partly for this reason ([Schwartz et al., 2023](https://doi.org/10.17487/RFC9460)). Second, because QUIC encrypts transport metadata, traditional network diagnostic and middlebox functions are harder to apply, and operators must rely on endpoint telemetry rather than on-path inspection ([Iyengar & Thomson, 2021](https://doi.org/10.17487/RFC9000)). Third, 0-RTT data is subject to replay, so applications must limit it to safely repeatable requests ([Thomson & Turner, 2021](https://doi.org/10.17487/RFC9001)). Fourth, server push, inherited from HTTP/2, proved sufficiently unpromising that browsers removed support ([Chromium, 2022](https://developer.chrome.com/blog/removing-push)). Finally, QUIC's shared congestion control means that multiplexing eliminates ordering-based blocking but does not isolate streams from bandwidth loss ([Iyengar & Swett, 2021](https://doi.org/10.17487/RFC9002)).

## Conclusion

HTTP/3 and QUIC represent a deliberate relocation of functionality from the application layer into a new, encrypted, UDP-based transport. The measurable differences over HTTP/2 are concrete and structural: connection establishment in one round trip instead of two, zero-round-trip resumption, stream multiplexing that is not undermined by TCP's ordered byte stream, header compression designed for out-of-order delivery, connection identity that survives address changes, and a transport that is inherently harder to ossify. The costs are equally concrete: dependency on UDP reachability, reduced on-path observability, replay considerations for early data, and a shared congestion controller across streams. On balance, the evidence supports HTTP/3 as a genuine architectural improvement for latency-sensitive and mobile workloads, while the persistence of UDP-blocking networks and observability constraints means that HTTP/2 remains a necessary fallback rather than a superseded protocol.

## References

Bishop, M. (Ed.). (2022). *HTTP/3* (RFC 9114). Internet Engineering Task Force. https://doi.org/10.17487/RFC9114

Chromium. (2022). *Removing HTTP/2 server push from Chrome*. Chrome for Developers. https://developer.chrome.com/blog/removing-push

Cloudflare. (n.d.). *What is HTTP/3?* https://www.cloudflare.com/learning/performance/what-is-http3/

Duke, M. (Ed.). (2023). *QUIC version 2* (RFC 9369). Internet Engineering Task Force. https://doi.org/10.17487/RFC9369

Iyengar, J., & Swett, I. (Eds.). (2021). *QUIC loss detection and congestion control* (RFC 9002). Internet Engineering Task Force. https://doi.org/10.17487/RFC9002

Iyengar, J., & Thomson, M. (Eds.). (2021). *QUIC: A UDP-based multiplexed and secure transport* (RFC 9000). Internet Engineering Task Force. https://doi.org/10.17487/RFC9000

Krasic, C., Bishop, M., & Frindell, A. (Eds.). (2022). *QPACK: Field compression for HTTP/3* (RFC 9204). Internet Engineering Task Force. https://doi.org/10.17487/RFC9204

Langley, A., Riddoch, A., Wilk, A., Vicente, A., Krasic, C., Zhang, D., Yang, F., Kouranov, F., Swett, I., Iyengar, J., Bailey, J., Dorfman, J., Roskind, J., Kulik, J., Olson, P., Murray, P., Tanzella, R., Shi, T., & Wang, S. T. (2017). The QUIC transport protocol: Design and Internet-scale deployment. In *Proceedings of the Conference of the ACM Special Interest Group on Data Communication (SIGCOMM '17)* (pp. 183–196). Association for Computing Machinery. https://doi.org/10.1145/3098822.3098842

Nottingham, M., McManus, P., & Reschke, J. (Eds.). (2016). *HTTP alternative services* (RFC 7838). Internet Engineering Task Force. https://doi.org/10.17487/RFC7838

Pauly, T., Kinnear, E., & Wood, C. (Eds.). (2022). *HTTP datagrams and the capsule protocol* (RFC 9297). Internet Engineering Task Force. https://doi.org/10.17487/RFC9297

Peon, R., & Ruellan, H. (2015). *HPACK: Header compression for HTTP/2* (RFC 7541). Internet Engineering Task Force. https://doi.org/10.17487/RFC7541

Rescorla, E. (2018). *The Transport Layer Security (TLS) protocol version 1.3* (RFC 8446). Internet Engineering Task Force. https://doi.org/10.17487/RFC8446

Schwartz, B., Bishop, M., & Nygren, E. (2023). *Service binding and parameter specification via the DNS (SVCB and HTTPS resource records)* (RFC 9460). Internet Engineering Task Force. https://doi.org/10.17487/RFC9460

Thomson, M., & Benfield, C. (Eds.). (2022). *HTTP/2* (RFC 9113). Internet Engineering Task Force. https://doi.org/10.17487/RFC9113

Thomson, M., & Turner, S. (Eds.). (2021). *Using TLS to secure QUIC* (RFC 9001). Internet Engineering Task Force. https://doi.org/10.17487/RFC9001

W3Techs. (2026). *Usage statistics of HTTP/3 for websites*. https://w3techs.com/technologies/details/ce-http3