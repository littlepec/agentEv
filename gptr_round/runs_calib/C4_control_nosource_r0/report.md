**Note on sources:** No source materials were included with your request, so I can't cite provided documents. The following is drawn from my own knowledge of the relevant IETF specifications (notably RFC 9000, RFC 9001, RFC 9002, and RFC 9114), which you can consult directly to verify any detail.

---

## The short version

**HTTP/2** fixed application-layer inefficiency by multiplexing many requests over one TCP connection, but it inherited TCP's rigidity: because TCP guarantees in-order byte delivery, one lost packet stalls *every* stream on the connection. **QUIC** (RFC 9000) is a new general-purpose transport built on **UDP** that reimplements reliability, congestion control, and flow control in user space, integrates TLS 1.3 into its own handshake, and multiplexes **independent streams** so loss on one doesn't block the others. **HTTP/3** (RFC 9114) is simply HTTP semantics mapped onto QUIC streams instead of TCP.

---

## Why HTTP/2 wasn't enough

HTTP/2 over TCP+TLS has three structural problems:

1. **Transport-layer head-of-line (HOL) blocking.** HTTP/2 solved *application-layer* HOL blocking (no more one-request-per-connection queueing), but TCP still delivers a single ordered byte stream. A dropped segment forces the kernel to hold back all later bytes until retransmission completes — so a single loss stalls all multiplexed streams on that connection. This is worst exactly where HTTP/2 performs best: many concurrent streams over one lossy link.
2. **Handshake latency.** TCP's three-way handshake plus a separate TLS handshake costs 2–3 round trips before the first byte of application data.
3. **Ossification.** TCP headers are visible to middleboxes; changing TCP is effectively impossible in practice, which froze transport evolution for decades.

Also, HPACK (RFC 7541) header compression assumes strictly in-order delivery, which makes it a poor fit for any transport that delivers streams out of order.

---

## What QUIC actually is

QUIC is a **UDP-based, multiplexed, encrypted transport**. From the network's view it's just UDP datagrams; everything else — reliability, retransmission, congestion control (RFC 9002), flow control, stream multiplexing — lives in the endpoint's user space, where it can evolve without touching kernels or middleboxes.

Key design elements:

- **Integrated TLS 1.3 handshake (RFC 9001).** Encryption is mandatory, not layered on top. Transport parameters are exchanged inside the TLS handshake, so connection setup and cryptographic setup happen together — typically **1 RTT** to first application data, and **0-RTT** on resumption.
- **Independent streams.** QUIC provides lightweight streams within a connection. Each carries its own ordered byte sequence, but loss is recovered per-stream. A lost packet only blocks the stream(s) whose data it contained.
- **Connection IDs and connection migration.** A connection is identified by a connection ID, not a 4-tuple, so a client can change IP address or port (Wi-Fi → cellular) and keep the connection alive.
- **Monotonically increasing packet numbers, never reused.** This removes TCP's retransmission ambiguity (the "is this ACK for the original or the retransmit?" problem) and yields cleaner RTT estimation and loss detection.
- **Header protection.** Most of the QUIC packet header is encrypted, limiting middlebox interference — though the **spin bit** was added as a deliberately visible latency signal, and ossification of QUIC itself remains a live concern.
- **Extensibility.** Version negotiation (QUIC v2 is RFC 9369), an unreliable datagram extension (RFC 9221), and HTTP datagrams (RFC 9297) are all specified extensions rather than transport rewrites.

---

## HTTP/3 on top of QUIC

HTTP/3 keeps HTTP semantics — methods, status codes, headers — and changes only the mapping:

- **One bidirectional QUIC stream per request/response**, so streams are genuinely independent.
- **QPACK (RFC 9204)** replaces HPACK. It splits compression state across dedicated unidirectional streams and lets endpoints bound how much they block on dynamic-table updates, making header compression safe over an out-of-order transport.
- **Control streams** carry connection-level settings and stream management.
- **Discovery** happens via the `Alt-Svc` HTTP header or the HTTPS/SVCB DNS record type, with ALPN token `h3`.
- **Prioritization** uses the extensible scheme in RFC 9218, since HTTP/2's tree-based priority was widely unimplemented and later deprecated.

Server push exists in HTTP/3 but was deprecated in browsers, largely for the same reasons it failed in HTTP/2.

---

## Improvements, side by side

| Concern | HTTP/2 (TCP + TLS) | HTTP/3 (QUIC + TLS 1.3) |
|---|---|---|
| Multiplexing HOL blocking | App layer solved; TCP layer remains | Solved per-stream |
| Connection setup | 2–3 RTT; 1 RTT resumed | 1 RTT; 0 RTT resumed |
| Crypto integration | Separate TLS handshake | Built into transport handshake |
| Header compression | HPACK (requires in-order) | QPACK (out-of-order safe) |
| Mobility | Connection breaks on IP change | Connection migration via connection ID |
| Loss recovery | TCP RTO/ACK ambiguity | Monotonic packet numbers, richer ACKs |
| Deployability | Kernel/middlebox ossified | User space, evolvable |
| Encryption | Optional (de facto mandatory) | Mandatory |

**The headline gains** are elimination of transport-layer HOL blocking, a noticeably faster handshake, and connection migration.

---

## Trade-offs and caveats

- **UDP blocking.** Some corporate and restrictive networks throttle or block UDP, forcing fallback to HTTP/2.
- **CPU cost.** User-space processing can be more expensive than kernel TCP, though GSO/GRO offloads and mature stacks have narrowed the gap.
- **0-RTT replay risk.** Early data isn't forward-secret and can be replayed; servers should only allow it for idempotent requests.
- **Uniformity isn't guaranteed.** Not every HTTP/3 deployment shows a clear win over a well-tuned HTTP/2 on low-loss networks — the benefit scales with latency and packet loss.
- **Adoption** is substantial at major CDNs and browsers but remains a minority of overall web traffic.

For authoritative detail, the primary references are RFC 9000 (QUIC transport), RFC 9001 (TLS in QUIC), RFC 9002 (loss detection and congestion control), RFC 9114 (HTTP/3), and RFC 9204 (QPACK).