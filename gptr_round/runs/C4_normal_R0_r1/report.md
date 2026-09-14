# HTTP/3 and QUIC: Architecture and Key Improvements over HTTP/2

## Introduction

The Hypertext Transfer Protocol has been revised repeatedly to keep pace with the demands of the modern web, and its third major generation — HTTP/3 — represents a structural departure from its predecessors rather than an incremental refinement. On 6 June 2022, the Internet Engineering Task Force published HTTP/3 as a Proposed Standard in RFC 9114 ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). The protocol is inseparable from QUIC, the transport protocol beneath it, which had itself been standardized as RFC 9000 in May 2021 ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). This report examines what QUIC and HTTP/3 are, how they are layered, and what specific deficiencies in HTTP/2 they were designed to address.

## What QUIC Is

QUIC is a transport layer network protocol which uses user space congestion control over the User Datagram Protocol (UDP) ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). That single sentence encodes three distinct architectural decisions that together define the protocol's character.

First, QUIC occupies the **transport layer**. It is therefore not an HTTP-specific technology; it is a general-purpose transport that other application protocols could in principle be mapped onto. HTTP/3 is one such mapping, not a definition of QUIC itself. This separation is reflected in the standardization timeline: the QUIC transport was published as RFC 9000 in May 2021, approximately thirteen months before HTTP/3 appeared in RFC 9114 in June 2022 ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)).

Second, QUIC runs **over UDP**. Rather than sitting directly on the Internet Protocol as TCP does, QUIC uses UDP as its substrate. The practical consequence is that QUIC's own transport logic — its stream management, loss recovery, and congestion control — is implemented on top of a minimal, connectionless datagram service rather than relying on the ordered, reliable byte-stream machinery that TCP provides. Because QUIC does not inherit TCP's delivery guarantees, it must construct its own.

Third, QUIC employs **user space congestion control** ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). Congestion control logic therefore lives within the userspace implementation of the protocol rather than requiring changes to operating system kernels. This is an architectural choice with deployment implications: revisions to congestion control behaviour are a matter of updating the protocol implementation rather than waiting on operating system release cycles or requiring kernel-level changes across heterogeneous host environments.

### Security Integrated at the Transport Layer

A further defining property of QUIC is that it incorporates TLS 1.3 at the transport layer, offering comparable confidentiality and integrity to running TLS over TCP ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). The RFC's wording is deliberately measured: the guarantee is *comparable* to TLS over TCP, not superior. What changes is not the strength of the cryptographic protection but its position in the stack. In the conventional model, security is a layer applied above the transport; in QUIC, TLS 1.3 is folded into the transport protocol itself, so that transport and cryptographic handshake are integrated rather than stacked.

## What HTTP/3 Is

RFC 9114 is explicit about its own scope: "This document describes a mapping of HTTP semantics over QUIC" ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). This framing is significant. HTTP/3 does not redefine HTTP semantics — the meaning of requests, responses, methods, and header fields is preserved. What HTTP/3 changes is the *transport mapping*: the rules by which those semantics are encoded into frames and carried across the network. The application-facing protocol and the wire-level delivery mechanism are decoupled, and it is the delivery mechanism that has been replaced.

## The Central Problem: Head-of-Line Blocking in HTTP/2 over TCP

The principal motivation for HTTP/3 lies in a limitation that HTTP/2 inherited from its transport. RFC 9114 describes the behaviour directly: with HTTP/2 over TCP, "a lost or reordered packet causes all active transactions to experience a stall regardless of whether that transaction was directly impacted by the lost packet" ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)).

HTTP/2 achieves multiplexing by interleaving multiple logical request/response transactions across a single TCP connection. TCP, however, presents the application with a single ordered byte stream and will not deliver data beyond a gap in that stream until the missing data has been retransmitted and the gap filled. The result is a form of head-of-line blocking at the transport layer: although the *application* has logically independent transactions, the *transport* has only one sequencing context. Consequently, a single lost packet stalls every transaction sharing the connection, including those whose own data arrived intact and on time. HTTP/2 therefore resolved the application-layer queueing that constrained HTTP/1.1 while inadvertently exposing a lower-level variant of the same problem.

That diagnosis — that the stall is connection-wide rather than transaction-local — is the precise defect that HTTP/3 and QUIC are constructed to eliminate.

## Key Improvements over HTTP/2

### Per-Stream Loss Isolation

The most consequential improvement is stated plainly: "Because QUIC provides native multiplexing, lost packets only impact the streams where data has been lost" ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). This stands in direct contrast to the RFC 9114 description of HTTP/2 over TCP, where all active transactions stall regardless of direct impact ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). Under QUIC, packet loss is contained: the affected stream waits for recovery, while streams whose data was delivered are not blocked by the gap. The failure domain shrinks from the connection to the individual stream.

### Multiplexing as a Transport Primitive

The word "native" in that description carries the architectural weight. In HTTP/2, multiplexing is an application-layer construct imposed on a transport that possesses no concept of streams. In QUIC, multiplexing is a property of the transport itself: the protocol is aware of stream boundaries as a first-class concept, which is why it can deliver data for unaffected streams without waiting on another stream's missing bytes. The improvement over HTTP/2 is not a matter of tuning; it is a relocation of responsibility from the application layer to the transport layer.

### Integrated Security

Because QUIC incorporates TLS 1.3 at the transport layer, HTTP/3 obtains confidentiality and integrity comparable to running TLS over TCP ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). The benefit here is architectural economy: the cryptographic handshake is part of the transport protocol rather than an additional layer negotiated above it.

### Deployable Congestion Control

The use of user space congestion control ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)) means congestion control evolution is decoupled from operating system kernels — a practical advantage for iterating on transport behaviour in the field.

### Comparison of the Two Stacks

| Dimension | HTTP/2 over TCP | HTTP/3 over QUIC |
|---|---|---|
| Underlying transport | TCP | QUIC, itself over UDP ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |
| Multiplexing | Application-layer construct over a single ordered byte stream | Native to the transport protocol ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |
| Effect of a lost or reordered packet | All active transactions stall, including those not directly impacted ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)) | Only streams where data was lost are impacted ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |
| Security layering | TLS over TCP (separate layer above transport) | TLS 1.3 incorporated at the transport layer ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)) |
| Confidentiality/integrity | Baseline for comparison | Comparable to TLS over TCP ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)) |
| Congestion control placement | Not specified in the reviewed sources | User space ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |
| HTTP semantics | Preserved | Preserved; RFC 9114 is a mapping of HTTP semantics over QUIC ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)) |
| Standardization | Not covered by the reviewed sources | QUIC: RFC 9000, May 2021; HTTP/3: RFC 9114, Proposed Standard, 6 June 2022 ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |

## Assessment

On the evidence of these sources, the most defensible conclusion is that HTTP/3's contribution is **architectural relocation rather than protocol reinvention**. HTTP semantics are unchanged — RFC 9114 is explicitly a mapping of existing semantics onto a new transport ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). What changes is where multiplexing and security live in the stack, and what happens to unrelated traffic when a packet goes missing.

Two qualifications follow from the sources and should be stated plainly rather than glossed over.

First, the improvement is **scoped to a specific failure mode**. The RFC's description of HTTP/2's deficiency is conditioned on a lost or reordered packet ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). It follows that the cross-transaction stall HTTP/3 eliminates is a mechanism that activates under loss or reordering; the sources make no claim that HTTP/3 reduces latency or improves throughput generally. The benefits described are containment benefits: when something goes wrong, the blast radius is smaller. Any expectation of broad performance gains is not supported by the material reviewed here.

Second, the security claim is one of **parity, not advancement**. QUIC's TLS 1.3 integration offers confidentiality and integrity "comparable to running TLS over TCP" ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). HTTP/3 should therefore not be adopted on the premise that it is cryptographically stronger than HTTP/2; the case for it rests on transport behaviour.

It is also worth noting the maturity status. HTTP/3 was published as a **Proposed Standard**, not a full Internet Standard ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). The specification is stable enough to implement and deploy, but the standards track has not reached its final maturity level. Meanwhile, the QUIC transport — the component doing the actual work of stream isolation — was standardized separately and earlier, in May 2021 ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). That ordering reflects the layering accurately: the transport capability came first, and HTTP/3 is the application protocol that exploits it.

Finally, a note on the evidence base. The authoritative source here is RFC 9114, an IETF standards document ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)); the supplementary source is an encyclopedic article, current as of the retrieval date of 14 September 2026 ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). Notably, **neither source supplies quantitative performance measurements** — no figures for latency reduction, throughput improvement, or loss-recovery timing. Consequently, this report makes no numeric performance claims, and any evaluation of HTTP/3's real-world advantage must rest on the qualitative mechanism described: the confinement of packet-loss impact to the streams actually affected.

## Conclusion

QUIC is a transport layer protocol that uses user space congestion control over UDP and incorporates TLS 1.3 at the transport layer ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3); [IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). HTTP/3 is an IETF Proposed Standard, published 6 June 2022 as RFC 9114, that maps HTTP semantics onto that transport ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3); [IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). Its defining improvement over HTTP/2 over TCP is the elimination of connection-wide head-of-line blocking: where a single lost or reordered packet previously stalled all active transactions regardless of direct impact, QUIC's native multiplexing confines loss to the streams whose data was lost. Security and congestion control are likewise repositioned — TLS 1.3 inside the transport, congestion control in user space — while HTTP semantics remain untouched. The result is a protocol whose value proposition is precision of failure isolation, not a redefinition of what HTTP means.

## References

Internet Engineering Task Force. (2022). *HTTP/3* (RFC 9114). IETF Trust. https://www.rfc-editor.org/rfc/rfc9114.html

Wikipedia. (2026, September 14). *HTTP/3*. In *Wikipedia*. https://en.wikipedia.org/wiki/HTTP/3