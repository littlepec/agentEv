# HTTP/3 and QUIC: Architecture, Mechanisms, and Improvements over HTTP/2

## Scope and Source Note

The information block supplied with this task contained empty *Title*, *Content*, and *Source* fields. No external documents were therefore available for attribution. To satisfy the requirement that every substantive claim be traceable, this report relies exclusively on the primary IETF specifications that define the protocols themselves: RFC 9000 (QUIC transport), RFC 9001 (TLS in QUIC), RFC 9002 (loss detection and congestion control), RFC 8999 (version-independent properties), RFC 9114 (HTTP/3), RFC 9204 (QPACK), RFC 9218 (extensible priorities), and RFC 9113 (HTTP/2). These are the authoritative source documents for the technology under discussion, and all citations below point to them.

## Introduction

HTTP/3 is the third major generation of the Hypertext Transfer Protocol, standardized in June 2022 as RFC 9114 ([RFC 9114](https://www.rfc-editor.org/rfc/rfc9114.html)). Its defining characteristic is not a change in HTTP semantics — request methods, status codes, and header fields remain those of HTTP/1.1 and HTTP/2 ([RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html)) — but a complete replacement of the underlying transport. Whereas HTTP/1.1 and HTTP/2 both run over TCP, HTTP/3 runs over QUIC, a multiplexed, encrypted, UDP-based transport protocol standardized in May 2021 as RFC 9000 ([RFC 9000](https://www.rfc-editor.org/rfc/rfc9000.html)). Understanding the improvements of HTTP/3 therefore requires understanding both what HTTP/2 does and what TCP structurally cannot do.

## 1. The Structural Limitations of HTTP/2 over TCP

### 1.1 Multiplexing Above an Ordered Byte Stream

HTTP/2 introduced binary framing, a single connection carrying many concurrent streams, header compression via HPACK, and stream-level flow control ([RFC 9113](https://www.rfc-editor.org/rfc/rfc9113.html)). This solved HTTP/1.1's application-layer head-of-line blocking, in which a slow response blocked all others on the same connection. However, it did not — and could not — solve the problem one layer below. TCP presents a single ordered byte stream to its application, so if one TCP segment is lost, every byte queued behind it must wait for retransmission before TCP delivers anything to HTTP/2. Because HTTP/2 multiplexes all streams onto that one byte stream, a single lost packet stalls every stream on the connection, regardless of which stream's data it carried ([RFC 9114](https://www.rfc-editor.org/rfc/rfc9114.html)). This is transport-layer head-of-line blocking, and it is intrinsic to TCP's design rather than an implementation defect.

### 1.2 Handshake Latency

HTTP/2 over TLS requires two sequential handshakes before application data can flow: the TCP three-way handshake (one round trip) and then the TLS handshake. With TLS 1.3, the combined cost is two round trips; with the older TLS 1.2, three ([RFC 9001](https://www.rfc-editor.org/rfc/rfc9001.html); [RFC 9000](https://www.rfc-editor.org/rfc/rfc9000.html)). TCP Fast Open can theoretically hide the TCP round trip, but deployment has been limited by middlebox interference, so it is not a reliable substitute.

### 1.3 Encryption Coverage and Ossification

Because QUIC integrates TLS 1.3 directly, the vast majority of QUIC packet header fields and all frame payloads are encrypted and integrity-protected; only a small set of fields needed for routing and demultiplexing (such as the connection ID and length) are visible, and even the packet number is header-protected ([RFC 9001](https://www.rfc-editor.org/rfc/rfc9001.html)). In HTTP/2 over TLS, by contrast, TCP and IP headers are necessarily in the clear, and the TLS layer terminates below HTTP/2, so frame-level structures are protected only as opaque payload. QUIC's broader encryption reduces the surface available to middleboxes to observe and "ossify" around, which is one of the design goals stated for the protocol ([RFC 9000](https://www.rfc-editor.org/rfc/rfc9000.html)).

## 2. QUIC: Design Overview

### 2.1 Streams as a Native Transport Abstraction

QUIC is built on UDP but implements its own connection-oriented, reliable, congestion-controlled transport inside a user-space or library implementation. Its fundamental abstraction is the *stream*: an ordered, reliable byte sequence identified by a stream ID, created independently of the connection. Streams may be bidirectional or unidirectional and client- or server-initiated, and the low two bits of the stream ID encode which ([RFC 9000](https://www.rfc-editor.org/rfc/rfc9000.html)). This matters directly for HTTP/3: a QUIC stream has its own flow control and its own delivery ordering, so a lost packet containing data for stream A does not prevent the receiver from delivering already-received data on stream B. Cross-stream head-of-line blocking is eliminated by construction; head-of-line blocking within a single stream obviously remains, as ordering within a stream is the point of a stream ([RFC 9000](https://www.rfc-editor.org/rfc/rfc9000.html)).

QUIC also provides connection-level and stream-level flow control, and it combines transport and cryptographic handshake into a single exchange. Initial packets must be padded to at least 1200 bytes, partly to ensure a minimum path MTU assumption and partly to allow servers to demonstrate address validation under the 3× anti-amplification limit ([RFC 9000](https://www.rfc-editor.org/rfc/rfc9000.html)).

### 2.2 Integrated TLS 1.3

QUIC does not carry TLS records. Instead it carries the TLS 1.3 handshake messages directly in CRYPTO frames, and only TLS 1.3 is permitted — earlier TLS versions are not supported ([RFC 9001](https://www.rfc-editor.org/rfc/rfc9001.html)). Transport parameters, such as initial flow-control limits and the maximum number of concurrent streams, are carried as a TLS extension, so transport negotiation is authenticated by the handshake itself ([RFC 9001](https://www.rfc-editor.org/rfc/rfc9001.html)). The result is a full handshake completed in one round trip, and a resumption handshake that can send application data in the first flight — "0-RTT" — using a previously issued session ticket ([RFC 9001](https://www.rfc-editor.org/rfc/rfc9001.html)). 0-RTT data is replayable by design, and both the specification and its security considerations advise restricting 0-RTT to idempotent or otherwise replay-safe requests ([RFC 9001](https://www.rfc-editor.org/rfc/rfc9001.html)).

### 2.3 Connection Migration and Connection IDs

A QUIC connection is not identified by the four-tuple of addresses and ports but by a connection ID, which may be 0 to 20 bytes long and is carried in every packet header ([RFC 9000](https://www.rfc-editor.org/rfc/rfc9000.html)). If a client's IP address changes — a common occurrence on mobile networks, where devices move between Wi-Fi and cellular — the connection can migrate to the new path without repeating the handshake, subject to path validation ([RFC 9000](https://www.rfc-editor.org/rfc/rfc9000.html)). TCP connections, bound to the four-tuple, break under the same circumstances. This is a functional capability, not merely a performance one: it is the reason QUIC is attractive for mobile clients and for long-lived sessions.

### 2.4 Loss Recovery, Congestion Control, and Extensibility

QUIC defines its own loss detection and recovery mechanisms, with separate packet number spaces for Initial, Handshake, and application data, and with ACK frames that can acknowledge out-of-order ranges ([RFC 9000](https://www.rfc-editor.org/rfc/rfc9000.html); [RFC 9002](https://www.rfc-editor.org/rfc/rfc9002.html)). Packet numbers are strictly increasing and never reused within a packet number space, which removes TCP's retransmission ambiguity; retransmitted data is simply sent in a new packet with a new number ([RFC 9002](https://www.rfc-editor.org/rfc/rfc9002.html)). A sample NewReno-style congestion controller is specified, with pacing recommended ([RFC 9002](https://www.rfc-editor.org/rfc/rfc9002.html)). Because the transport is implemented in user space and versioned, extensions can be deployed far more rapidly than TCP options: examples include unreliable datagrams (RFC 9221), QUIC version 2 (RFC 9369), and GREASE-style reserved-value usage (RFC 9287), all of which follow the version-independent framework of RFC 8999 ([RFC 8999](https://www.rfc-editor.org/rfc/rfc8999.html)).

## 3. HTTP/3: HTTP Semantics Mapped onto QUIC

### 3.1 Stream and Frame Mapping

HTTP/3 preserves HTTP semantics but re-maps them onto QUIC stream types. Each request-response exchange consumes one client-initiated bidirectional stream ([RFC 9114](https://www.rfc-editor.org/rfc/rfc9114.html)). In addition, each endpoint opens unidirectional control streams, identified by a stream type prefix: 0x00 for the control stream, 0x01 for push streams, 0x02 for the QPACK encoder stream, and 0x03 for the QPACK decoder stream ([RFC 9114](https://www.rfc-editor.org/rfc/rfc9114.html); [RFC 9204](https://www.rfc-editor.org/rfc/rfc9204.html)). Only one control stream per direction is permitted; a second is a connection error. Frames such as DATA (0x0), HEADERS (0x1), CANCEL_PUSH (0x3), SETTINGS (0x4), PUSH_PROMISE (0x5), GOAWAY (0x7), and MAX_PUSH_ID (0xD) are defined for HTTP/3 ([RFC 9114](https://www.rfc-editor.org/rfc/rfc9114.html)).

### 3.2 QPACK Header Compression

HTTP/2's HPACK compresses headers using a dynamic table that is implicitly synchronized in order, so a header block referencing a not-yet-received table update blocks the entire connection — a compression-induced form of head-of-line blocking. QPACK solves this by moving dynamic table updates onto dedicated unidirectional encoder and decoder streams and by allowing an encoder to reference the static table immediately while marking dynamic references as potentially blocking ([RFC 9204](https://www.rfc-editor.org/rfc/rfc9204.html)). QPACK defines a 99-entry static table and permits a configurable limit on the number of blocked streams via SETTINGS_QPACK_BLOCKED_STREAMS ([RFC 9204](https://www.rfc-editor.org/rfc/rfc9204.html)). In practice, QPACK typically compresses slightly less efficiently than HPACK but never stalls unrelated request streams to do so.

### 3.3 Prioritization and Server Push

HTTP/3 does not reuse HTTP/2's stream dependency tree; the extensible prioritization scheme of RFC 9218, based on urgency and incremental delivery, applies to both HTTP/2 and HTTP/3 ([RFC 9218](https://www.rfc-editor.org/rfc/rfc9218.html)). Server push survives in HTTP/3 as PUSH_PROMISE frames plus server-initiated unidirectional push streams, with the client able to limit or cancel pushes through MAX_PUSH_ID and CANCEL_PUSH ([RFC 9114](https://www.rfc-editor.org/rfc/rfc9114.html)).

## 4. Key Improvements over HTTP/2

| Dimension | HTTP/2 (over TCP + TLS) | HTTP/3 (over QUIC) |
|---|---|---|
| Transport | TCP ([RFC 9113](https://www.rfc-editor.org/rfc/rfc9113.html)) | QUIC over UDP ([RFC 9000](https://www.rfc-editor.org/rfc/rfc9000.html)) |
| Cross-stream head-of-line blocking | Present; one lost TCP segment stalls all streams | Eliminated; loss affects only streams whose data was in the lost packet |
| Full handshake RTTs before data | 2 RTT with TLS 1.3; 3 RTT with TLS 1.2 | 1 RTT |
| Resumption | 1 RTT (TCP) + TLS 1.3 0-RTT data | 0-RTT data possible |
| Encryption coverage | TCP/IP headers and frame structure outside TLS boundary | Nearly all header fields and all payload protected ([RFC 9001](https://www.rfc-editor.org/rfc/rfc9001.html)) |
| Connection identity | Four-tuple; breaks on address change | Connection ID; supports migration ([RFC 9000](https://www.rfc-editor.org/rfc/rfc9000.html)) |
| Header compression | HPACK, order-synchronized | QPACK, blocking-limited ([RFC 9204](https://www.rfc-editor.org/rfc/rfc9204.html)) |
| Default port | TCP 443 | UDP 443 |
| ALPN token | "h2" | "h3" ([RFC 9114](https://www.rfc-editor.org/rfc/rfc9114.html)) |
| Prioritization | Dependency tree + weights | Extensible urgency/incremental scheme ([RFC 9218](https://www.rfc-editor.org/rfc/rfc9218.html)) |
| Extensibility | TCP option space constrained by middleboxes | Versioned, user-space protocol with formal extension framework ([RFC 8999](https://www.rfc-editor.org/rfc/rfc8999.html)) |

The single most consequential row is head-of-line blocking. Empirical intuition, and the specification's own rationale, indicates that the value of HTTP/3 scales with loss rate: on a clean, low-latency path, removing cross-stream stalls yields little because there are few losses to recover from, whereas on lossy mobile or congested links the difference can be substantial ([RFC 9114](https://www.rfc-editor.org/rfc/rfc9114.html); [RFC 9000](https://www.rfc-editor.org/rfc/rfc9000.html)). The second is handshake latency: QUIC saves one round trip on a fresh connection and permits zero-RTT resumption, which matters most for short, latency-dominated transactions ([RFC 9001](https://www.rfc-editor.org/rfc/rfc9001.html)).

## 5. Costs, Trade-offs, and Open Issues

The improvements are not free. First, QUIC runs in user space on top of UDP, which historically imposes higher per-packet CPU cost and requires careful implementation of segmentation, timers, and congestion control that the kernel formerly provided. Second, some networks block or rate-limit UDP, and HTTP/3 therefore depends on fallback: clients typically learn of HTTP/3 support through the Alt-Svc mechanism (RFC 7838) or SVCB/HTTPS DNS records, and must retain a working HTTP/2 path ([RFC 9114](https://www.rfc-editor.org/rfc/rfc9114.html)). Third, the broad encryption of transport metadata removes some operational visibility that network operators previously had, and the same encryption that resists ossification also resists legitimate middlebox functions. Fourth, 0-RTT carries inherent replay risk, and hosts must decide per-resource whether replay is acceptable ([RFC 9001](https://www.rfc-editor.org/rfc/rfc9001.html)). Fifth, HTTP/3's benefits are contingent on loss and mobility characteristics; a well-provisioned datacenter path with negligible loss may show only marginal improvement over HTTP/2.

## 6. Assessment

Taken together, the specifications support a clear position: HTTP/3 and QUIC represent a genuine architectural correction rather than an incremental optimization. HTTP/2 multiplexed several logical exchanges over a transport that fundamentally serializes them, and no amount of tuning above TCP could remove that constraint. QUIC moves multiplexing into the transport itself, so ordering and loss recovery are per-stream; it collapses two sequential handshakes into one integrated TLS 1.3 exchange and permits zero-RTT resumption; it identifies connections by connection ID so that sessions survive address changes; and it encrypts transport metadata by default. The most durable advantage, however, is not any single latency figure but the design's extensibility: a versioned, user-space transport can evolve far faster than TCP, and HTTP/3 is the first HTTP version defined as an application mapping onto a general-purpose multipurpose transport rather than a protocol welded to TCP. The most defensible conclusion, given the specifications, is that HTTP/3's measurable gains concentrate where loss and mobility are highest, while its structural value — decoupled multiplexing, pervasive encryption, and evolvability — applies everywhere.

## References

IETF. (2021). *QUIC: A UDP-based multiplexed and secure transport* (RFC 9000). RFC Editor. https://www.rfc-editor.org/rfc/rfc9000.html

IETF. (2021). *Using TLS to secure QUIC* (RFC 9001). RFC Editor. https://www.rfc-editor.org/rfc/rfc9001.html

IETF. (2021). *QUIC loss detection and congestion control* (RFC 9002). RFC Editor. https://www.rfc-editor.org/rfc/rfc9002.html

IETF. (2021). *Version-independent properties of QUIC* (RFC 8999). RFC Editor. https://www.rfc-editor.org/rfc/rfc8999.html

IETF. (2022). *HTTP/3* (RFC 9114). RFC Editor. https://www.rfc-editor.org/rfc/rfc9114.html

IETF. (2022). *QPACK: Field compression for HTTP/3* (RFC 9204). RFC Editor. https://www.rfc-editor.org/rfc/rfc9204.html

IETF. (2022). *Extensible prioritization scheme for HTTP* (RFC 9218). RFC Editor. https://www.rfc-editor.org/rfc/rfc9218.html

IETF. (2022). *HTTP/2* (RFC 9113). RFC Editor. https://www.rfc-editor.org/rfc/rfc9113.html

IETF. (2022). *HTTP semantics* (RFC 9110). RFC Editor. https://www.rfc-editor.org/rfc/rfc9110.html