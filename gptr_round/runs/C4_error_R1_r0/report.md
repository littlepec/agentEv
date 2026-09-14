# HTTP/3 and QUIC: How a UDP-Based Transport Redesign Removes HTTP/2's Structural Ceiling

## Scope, Sources, and Method

The request accompanying this report supplied no source packet, so the analysis below rests on the primary IETF specifications that define the protocols themselves — RFC 7540 and its successor RFC 9113 for HTTP/2, RFC 9000/9001/9002 for QUIC, RFC 9114 and RFC 9204 for HTTP/3 — supplemented by the peer-reviewed SIGCOMM measurement paper produced by Google's QUIC team and first-party engineering disclosures from Cloudflare and Chromium. These are the highest-reliability sources available for a protocol question of this kind, because normative behaviour is defined by the specifications and validated by large-scale deployment measurement rather than by secondary commentary. The report's central evaluative claim, stated up front, is that HTTP/3's durable advantage over HTTP/2 is architectural rather than incremental: the elimination of transport-layer head-of-line (HOL) blocking and the introduction of connection migration are structural wins, whereas the much-publicised handshake-latency reduction is real but conditional, and the protocol's costs — chiefly server-side CPU and dependence on unfiltered UDP — are significant and frequently understated.

## 1. The Baseline: What HTTP/2 Achieved and What It Could Not Fix

### 1.1 Multiplexing Over a Single TCP Connection

HTTP/2, standardised in 2015, replaced HTTP/1.1's textual, one-request-per-connection model with a binary framing layer that multiplexes many concurrent request and response streams over a single long-lived TCP connection, adds HPACK header-field compression, and introduces both stream-level and connection-level flow control ([Belshe et al., 2015](https://www.rfc-editor.org/rfc/rfc7540.html)). These were genuine gains: connection setup costs were amortised, the HTTP/1.1 practice of opening six parallel connections per origin became unnecessary, and header redundancy was compressed.

The unresolved problem was inherited from the transport. TCP presents the application with a single, strictly ordered byte stream, and the specification itself acknowledged the consequence: because all HTTP/2 streams are carried on one TCP connection, a single lost or reordered TCP segment prevents delivery of *every* stream behind it, regardless of whether those streams have any data in the lost segment ([Belshe et al., 2015](https://www.rfc-editor.org/rfc/rfc7540.html)). This is transport-layer HOL blocking, and it is qualitatively worse than HTTP/1.1's application-layer version: HTTP/1.1's head-of-line blocking could be worked around by opening parallel connections, whereas HTTP/2's cannot be worked around at all without abandoning the connection. On a lossy mobile link, the multiplexing benefit of HTTP/2 can therefore be substantially neutralised.

### 1.2 Handshake Latency

Establishing an HTTP/2 connection requires two sequential round trips before application data can flow: one RTT for the TCP three-way handshake, then one RTT for a TLS 1.3 handshake. A resumed session still costs one RTT for TCP plus the TLS resumption flight ([Marx, 2019](https://blog.cloudflare.com/http3-the-past-present-and-future/)). Because these layers are independent, they cannot be overlapped.

### 1.3 Ossification and Deployment Inertia

TCP is implemented in operating-system kernels and hardware, and its wire format is assumed by a vast population of middleboxes. Consequently, meaningful TCP changes — new congestion-control algorithms, new options, additional metadata — either take many years to deploy or are stripped in transit. This "ossification" is a structural property of deploying transport functionality at the wrong layer of the stack ([Langley et al., 2017](https://doi.org/10.1145/3098822.3098842)).

## 2. QUIC: Architecture and Design Principles

### 2.1 A User-Space Transport Running Over UDP

QUIC is specified as "a new multiplexed and secure transport" that provides stream multiplexing, per-stream flow control, low-latency connection establishment, and connection migration ([Iyengar & Thomson, 2021](https://www.rfc-editor.org/rfc/rfc9000.html)). Rather than replacing TCP, it is carried inside UDP datagrams, which means it traverses existing network equipment without requiring kernel or middlebox changes and can be updated by shipping new application or library code rather than a new operating system. The trade-off is that the transport is now subject to UDP's treatment in the network: firewalls that block UDP, rate-limiting of non-TCP traffic, and default socket buffer sizes that are too small for the required throughput all become deployment concerns ([Marx, 2019](https://blog.cloudflare.com/http3-the-past-present-and-future/)).

### 2.2 Streams Without Transport-Level Head-of-Line Blocking

QUIC implements streams as first-class transport objects. Each stream is independently flow-controlled, and QUIC also applies a connection-level flow-control limit, so a slow or stalled stream does not consume the entire connection's buffer budget ([Iyengar & Thomson, 2021](https://www.rfc-editor.org/rfc/rfc9000.html)). Because stream data is framed inside individually protected QUIC packets, loss of a packet only blocks the stream or streams whose bytes were in that packet; other streams continue to be delivered and processed. This is the single most important functional difference from HTTP/2 over TCP, and it is a property of the transport rather than of the application protocol.

### 2.3 An Integrated TLS 1.3 Handshake

QUIC does not layer TLS on top of a byte stream. Instead, TLS 1.3 handshake messages are carried in QUIC `CRYPTO` frames, and QUIC requires TLS 1.3 or later — earlier TLS versions are not permitted ([Thomson & Turner, 2021](https://www.rfc-editor.org/rfc/rfc9001.html)). Combining the transport and cryptographic handshakes collapses what was two sequential round trips into one: a first-time QUIC connection can send application data after a single RTT, and a resumed connection can send it in the very first flight using 0-RTT data ([Iyengar & Thomson, 2021](https://www.rfc-editor.org/rfc/rfc9000.html)). It is worth stating plainly that 0-RTT is not free: those early bytes are replayable by an attacker who captures them, which is why the specification requires application protocols to treat 0-RTT data as non-idempotent by default ([Thomson & Turner, 2021](https://www.rfc-editor.org/rfc/rfc9001.html)).

### 2.4 Connection IDs and Connection Migration

A QUIC connection is identified by a Connection ID rather than by the four-tuple of source and destination addresses and ports, and endpoints negotiate new Connection IDs during the connection ([Iyengar & Thomson, 2021](https://www.rfc-editor.org/rfc/rfc9000.html)). This allows a client whose IP address changes — a phone moving from Wi-Fi to cellular, or a device switching between NAT bindings — to continue the same connection, with path validation used to confirm reachability on the new path before the change is considered confirmed ([Iyengar & Thomson, 2021](https://www.rfc-editor.org/rfc/rfc9000.html)). HTTP/2 over TCP has no equivalent capability; an address change terminates the connection and forces a full re-handshake.

### 2.5 Loss Detection, Congestion Control, and Packet Protection

QUIC's recovery behaviour is specified separately from its transport framing. Loss detection uses a packet threshold of three packets and a time threshold of 9/8 multiplied by the maximum of the smoothed and latest RTT estimates; the default congestion controller is a NewReno-style algorithm with a recommended initial congestion window of the minimum of ten maximum-sized datagrams or the larger of two maximum-sized datagrams and 14,720 bytes ([Iyengar & Swett, 2021](https://www.rfc-editor.org/rfc/rfc9002.html)). QUIC uses packet numbers that are monotonically increasing and never reused, which removes TCP's retransmission-ambiguity problem entirely.

All QUIC packets except Version Negotiation and Retry are protected with AEAD, and header fields are separately protected; a client must expand Initial datagrams to at least 1,200 bytes, and a server must not send more than three times the volume of data it has received from an unvalidated address, as an anti-amplification measure ([Iyengar & Thomson, 2021](https://www.rfc-editor.org/rfc/rfc9000.html)). The specification has also been versioned independently of HTTP: QUIC Version 2 is defined in its own document, preserving the ability to roll the transport forward without touching the application mapping ([Duckworth, 2023](https://www.rfc-editor.org/rfc/rfc9369.html)).

## 3. HTTP/3: Mapping HTTP Semantics onto QUIC

### 3.1 Framing and Stream Types

HTTP/3 preserves HTTP semantics — methods, status codes, fields, and their meaning — while replacing the framing layer: "HTTP/3 ... is the mapping of HTTP over QUIC" and, like HTTP/2, it uses a binary framing layer over a multiplexed transport ([Bishop, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). Requests and responses are carried on client-initiated bidirectional streams; a control stream and one or more unidirectional streams carry connection-level configuration and header-compression state. HTTP/3 uses UDP port 443 by default, and because it depends on QUIC, it has no cleartext variant — encryption is mandatory rather than optional ([Bishop, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)).

### 3.2 QPACK: Header Compression Without Reintroducing HOL Blocking

HTTP/2's HPACK compresses header fields against a dynamic table that both endpoints update in a strictly ordered sequence over the connection, so a single lost packet can block decoding of all subsequent header blocks — effectively reintroducing head-of-line blocking at the compression layer. QPACK was designed specifically to avoid this: encoder and decoder instructions travel on dedicated unidirectional streams separate from the request streams, and a header block can be encoded without depending on information that may still be in flight ([Krasic et al., 2022](https://www.rfc-editor.org/rfc/rfc9204.html)). Header compression therefore no longer undermines the transport's stream independence.

### 3.3 Prioritisation

HTTP/2 originally defined an elaborate priority tree with dependencies and weights. It was widely regarded as too complex and was sparsely implemented, and the revised HTTP/2 specification dropped the signal in favour of a simpler extensible scheme ([Thomson & Benfield, 2022](https://www.rfc-editor.org/rfc/rfc9113.html)). HTTP/3 adopts that replacement scheme directly: priorities are expressed as an urgency level from 0 to 7 plus an incremental flag, and can be sent or updated in `PRIORITY_UPDATE` frames at any point in the connection's life ([Oku & Pardue, 2022](https://www.rfc-editor.org/rfc/rfc9218.html)). This is a case where HTTP/3 did not merely inherit HTTP/2's design but corrected it.

### 3.4 Server Push and Discovery

Server push remains part of the HTTP/3 specification, with push streams carrying server-initiated responses ([Bishop, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). In practice, however, the feature has been withdrawn from the browser that drove most of its adoption, with Chrome removing HTTP/2 server push on the grounds that it was rarely beneficial and often harmed performance ([Chromium, 2022](https://developer.chrome.com/blog/removing-push/)). Discovery of HTTP/3 support is handled out of band: clients learn of an HTTP/3 endpoint through the `Alt-Svc` mechanism or, more recently, through HTTPS and SVCB DNS resource records that publish service parameters including ALPN identifiers ([Schwartz et al., 2023](https://www.rfc-editor.org/rfc/rfc9460.html)).

## 4. Head-to-Head Comparison

| Dimension | HTTP/1.1 | HTTP/2 | HTTP/3 |
|---|---|---|---|
| Transport | TCP | TCP | QUIC over UDP |
| Multiplexing | Multiple connections | Streams on one TCP connection | Independent QUIC streams |
| HOL blocking | Application layer | Transport layer (TCP) | Stream-level only |
| Header compression | None | HPACK | QPACK |
| Compression-layer HOL blocking | N/A | Yes | Avoided by design |
| Cryptographic handshake | TLS over TCP | TLS over TCP | Integrated into QUIC |
| Encryption | Optional | Optional (de facto) | Mandatory |
| Connection migration | No | No | Yes (Connection IDs) |
| Prioritisation | Connection-based | Priority tree (removed) | Extensible priorities (RFC 9218) |
| Server push | No | Yes | Yes, but withdrawn in browsers |
| Handshake to first data | 2–3 RTT | 2 RTT | 1 RTT |
| Resumed handshake | 2 RTT | 1 RTT | 0 RTT (replay-limited) |

Sources: ([Belshe et al., 2015](https://www.rfc-editor.org/rfc/rfc7540.html); [Iyengar & Thomson, 2021](https://www.rfc-editor.org/rfc/rfc9000.html); [Bishop, 2022](https://www.rfc-editor.org/rfc/rfc9114.html); [Krasic et al., 2022](https://www.rfc-editor.org/rfc/rfc9204.html); [Thomson & Benfield, 2022](https://www.rfc-editor.org/rfc/rfc9113.html)).

## 5. Evidence on the Magnitude of Improvement

Two classes of benefit should be distinguished, because they behave very differently across network conditions.

**Latency from connection establishment.** On a first visit to an origin, HTTP/3 removes one RTT relative to HTTP/2 over TLS 1.3, and on a repeat visit it can remove the remaining RTT by sending a request in 0-RTT data ([Iyengar & Thomson, 2021](https://www.rfc-editor.org/rfc/rfc9000.html)). On a low-RTT, lossless terrestrial path this saves a few tens of milliseconds per new connection — measurable but not transformative. On a 200 ms RTT cellular path, or on a connection where TCP handshake loss triggers a retransmission timeout, the saving can reach several hundred milliseconds and dominates the user-perceived improvement ([Marx, 2019](https://blog.cloudflare.com/http3-the-past-present-and-future/)).

**Throughput and stability under loss.** The removal of transport-layer HOL blocking is the benefit that scales with adversity. Google's large-scale deployment study reported that QUIC reduced the mean latency of Google Search by roughly 8% and mean YouTube rebuffering by roughly 18%, with the improvement being notably larger for users on poor connections ([Langley et al., 2017](https://doi.org/10.1145/3098822.3098842)). That last qualifier is the analytically important part: the distribution of gains is skewed, and an operator measuring aggregate or median latency on a well-provisioned network will see a far smaller effect than a mobile-first operator measuring the tail.

A third, less frequently quantified benefit is connection migration, which converts a network transition from a full teardown and re-handshake into a path change on an existing connection ([Iyengar & Thomson, 2021](https://www.rfc-editor.org/rfc/rfc9000.html)). For applications that maintain long-lived stateful sessions, this is arguably more valuable than any latency figure.

## 6. Costs, Trade-offs, and Open Questions

An impartial assessment must weigh the following against the gains.

**Server and client CPU cost.** QUIC's encryption, header protection, and finer-grained packet processing cost more CPU per byte than a kernel TCP stack. The transport must be implemented in user space, which removes the benefit of kernel offloads such as segmentation and receive coalescing unless explicitly implemented ([Langley et al., 2017](https://doi.org/10.1145/3098822.3098842)).

**UDP reachability and rate limiting.** Because HTTP/3 depends on UDP, any network that blocks or throttles UDP silently degrades performance relative to HTTP/2 rather than failing visibly; hence the importance of robust fallback to TCP-based HTTP/2 ([Marx, 2019](https://blog.cloudflare.com/http3-the-past-present-and-future/)).

**Amplification and validation.** The 1,200-byte Initial requirement and the three-times amplification limit are protocol-level defences against the classic UDP reflection attack, but they impose a real cost on small handshake payloads ([Iyengar & Thomson, 2021](https://www.rfc-editor.org/rfc/rfc9000.html)).

**Replay exposure in 0-RTT.** The latency win from 0-RTT is purchased with replayability, and applications must decide themselves which requests are safe to send early ([Thomson & Turner, 2021](https://www.rfc-editor.org/rfc/rfc9001.html)).

**Metadata exposure.** Although the transport encrypts nearly everything, the QUIC Initial packet is protected with keys derived from the connection ID, meaning the Server Name Indication remains observable until the handshake completes unless Encrypted Client Hello is deployed ([Iyengar & Thomson, 2021](https://www.rfc-editor.org/rfc/rfc9000.html)). HTTP/3 is therefore not a complete answer to transport-level metadata leakage.

**Extensibility beyond request/response.** QUIC's unreliable datagram extension and the corresponding HTTP datagram and capsule mapping open the door to non-streaming traffic such as interactive media and tunnelling over the same connection ([Pauly et al., 2022](https://www.rfc-editor.org/rfc/rfc9221.html); [Schinazi & Pardue, 2022](https://www.rfc-editor.org/rfc/rfc9297.html)). This is a capability HTTP/2 has no route to, and it is likely to matter more in the long run than raw page-load latency.

## 7. Assessment

The evidence supports a differentiated verdict rather than a blanket endorsement. HTTP/3's decisive advantage over HTTP/2 is architectural: by moving multiplexing, flow control, and encryption into a single transport that the network does not attempt to interpret, it removes a head-of-line blocking constraint that HTTP/2 could only mitigate, adds connection migration that HTTP/2 cannot offer at all, and permits future transport evolution without operating-system dependencies. Its handshake advantage is genuine but conditional, delivering the greatest benefit precisely where HTTP/2 is weakest — high-RTT, lossy, and mobile paths — and the least benefit on the fast, clean paths where HTTP/2 already performs well. Its costs, above all higher CPU per byte and dependence on UDP being permitted in the path, are structural rather than transitional and will not disappear with maturity. The rational engineering conclusion, therefore, is that HTTP/3 should be deployed broadly and negotiated opportunistically, with fallback to HTTP/2 retained indefinitely, and that the specific benefit an operator should expect to observe is tail-latency and connection-recovery improvement rather than a uniform speed-up.

## References

Belshe, M., Peon, R., & Thomson, M. (Ed.). (2015). *Hypertext Transfer Protocol version 2 (HTTP/2)* (RFC 7540). RFC Editor. https://www.rfc-editor.org/rfc/rfc7540.html

Bishop, M. (Ed.). (2022). *HTTP/3* (RFC 9114). RFC Editor. https://www.rfc-editor.org/rfc/rfc9114.html

Chromium. (2022). *Removing HTTP/2 server push from Chrome*. Chrome for Developers. https://developer.chrome.com/blog/removing-push/

Duckworth, M. (Ed.). (2023). *QUIC version 2* (RFC 9369). RFC Editor. https://www.rfc-editor.org/rfc/rfc9369.html

Iyengar, J., & Swett, I. (Eds.). (2021). *QUIC loss detection and congestion control* (RFC 9002). RFC Editor. https://www.rfc-editor.org/rfc/rfc9002.html

Iyengar, J., & Thomson, M. (Eds.). (2021). *QUIC: A UDP-based multiplexed and secure transport* (RFC 9000). RFC Editor. https://www.rfc-editor.org/rfc/rfc9000.html

Krasic, C., Bishop, M., & Frindell, A. (Eds.). (2022). *QPACK: Field compression for HTTP/3* (RFC 9204). RFC Editor. https://www.rfc-editor.org/rfc/rfc9204.html

Langley, A., Riddoch, A., Wilk, A., Vicente, A., Krasic, C., Zhang, D., Yang, F., Kouranov, F., Swett, I., Iyengar, J., Bailey, J., Dorfman, J., Roskind, J., Kulik, J., Olson, J., Murray, K., Sindelar, K., & Orman, M. (2017). The QUIC transport protocol: Design and Internet-scale deployment. In *Proceedings of the Conference of the ACM Special Interest Group on Data Communication (SIGCOMM '17)* (pp. 183–196). ACM. https://doi.org/10.1145/3098822.3098842

Marx, R. (2019, September 26). *HTTP/3: The past, present, and future*. The Cloudflare Blog. https://blog.cloudflare.com/http3-the-past-present-and-future/

Oku, K., & Pardue, L. (2022). *Extensible prioritization scheme for HTTP* (RFC 9218). RFC Editor. https://www.rfc-editor.org/rfc/rfc9218.html

Pauly, T., Kinnear, E., & Schinazi, D. (2022). *An unreliable datagram extension to QUIC* (RFC 9221). RFC Editor. https://www.rfc-editor.org/rfc/rfc9221.html

Schinazi, D., & Pardue, L. (2022). *HTTP datagrams and the capsule protocol* (RFC 9297). RFC Editor. https://www.rfc-editor.org/rfc/rfc9297.html

Schwartz, B., Bishop, M., & Nygren, E. (Eds.). (2023). *Service binding and parameter specification via the DNS (SVCB and HTTPS resource records)* (RFC 9460). RFC Editor. https://www.rfc-editor.org/rfc/rfc9460.html

Thomson, M., & Benfield, C. (Eds.). (2022). *HTTP/2* (RFC 9113). RFC Editor. https://www.rfc-editor.org/rfc/rfc9113.html

Thomson, M., & Turner, S. (2021). *Using TLS to secure QUIC* (RFC 9001). RFC Editor. https://www.rfc-editor.org/rfc/rfc9001.html