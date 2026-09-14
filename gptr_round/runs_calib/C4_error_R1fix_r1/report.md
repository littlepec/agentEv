# HTTP/3 and QUIC: Architecture, Standardization, and the Key Improvements over HTTP/2

## Introduction

HTTP/3 is the third major version of the Hypertext Transfer Protocol, and its defining architectural decision is not a change in HTTP semantics at all but a change in the transport beneath them. The protocol is explicitly specified as a mapping of HTTP semantics onto QUIC ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). In other words, the request/response model familiar from HTTP/1.1 and HTTP/2 is preserved, while the layer that actually carries the bytes across the network is replaced. That replacement is the source of nearly every practical improvement attributed to HTTP/3, most notably the elimination of the transport-level head-of-line blocking that constrains HTTP/2 when it runs over TCP.

This report explains what QUIC is, what HTTP/3 is, how the two relate, and why the pairing materially improves on HTTP/2. It relies on two sources: the authoritative specification RFC 9114, published by the IETF in June 2022, and the Wikipedia article "HTTP/3," retrieved 14 September 2026, which summarizes QUIC's design and the standardization timeline. The analysis below gives priority to RFC 9114 where the two sources overlap, because a primary standards document carries greater authority than an encyclopedic summary, while using the Wikipedia entry to supply contextual and historical details the RFC does not restate.

## Source Base and Reliability Assessment

Before presenting the technical findings, it is worth stating plainly how the evidence was weighted. RFC 9114 is a primary source: it is the normative specification of HTTP/3, published by the IETF and held by the IETF Trust ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). Claims drawn from it — particularly the description of HTTP/2-over-TCP head-of-line blocking and the integration of TLS 1.3 into QUIC — should be treated as definitive statements of protocol behavior. The Wikipedia article is a secondary source, licensed CC BY-SA 4.0 and retrieved on 14 September 2026 ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). It is useful for dates, for the concise characterization of QUIC as a user-space transport over UDP, and for the stream-level loss-isolation property, but it is not normative. Where the report states a mechanism, the more authoritative source is cited.

## The Standardization Record

The standardization history matters because it clarifies that HTTP/3 was not published in isolation; it was the application-layer companion to an already-standardized transport.

| Milestone | Date | Document | Status |
|---|---|---|---|
| QUIC transport specification | May 2021 | RFC 9000 | Published standard for the transport layer |
| HTTP/3 mapping onto QUIC | 6 June 2022 | RFC 9114 | IETF Proposed Standard |

The IETF published HTTP/3 as a Proposed Standard in RFC 9114 on 6 June 2022, while the underlying QUIC transport was specified as RFC 9000 in May 2021 ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). RFC 9114 itself is dated June 2022 and is issued under the IETF Trust ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). The sequencing is significant: QUIC existed as a transport protocol before HTTP/3 existed as a mapping onto it, which means HTTP/3 inherited a completed transport design rather than negotiating one simultaneously. The practical consequence is that the improvements over HTTP/2 are essentially the improvements of QUIC over TCP, filtered through HTTP's semantics.

## What QUIC Is

### A Transport Protocol in User Space over UDP

QUIC is a transport layer network protocol that uses user space congestion control over the User Datagram Protocol (UDP) ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). Three elements of that description deserve emphasis.

First, QUIC is a *transport* protocol. It occupies the architectural position that TCP has historically occupied, providing reliable, ordered delivery of streams to the application above it. HTTP/3 therefore does not sit directly on UDP in the sense that a naive datagram application would; it sits on QUIC, which itself sits on UDP.

Second, congestion control is implemented in *user space* rather than in the operating system kernel. This is an architectural choice with real consequences: it means the congestion control algorithm ships with the application or library rather than being tied to the host operating system's TCP stack, and it can therefore be updated on the application's release cadence rather than the operating system's.

Third, UDP is the substrate. Because UDP is a minimal, connectionless datagram protocol, QUIC must implement reliability, ordering, and congestion control itself rather than inheriting them. That apparent burden is precisely what grants QUIC the freedom to make different trade-offs from TCP — most importantly the freedom to treat loss per stream rather than per connection.

### TLS 1.3 at the Transport Layer

QUIC incorporates TLS 1.3 at the transport layer, offering confidentiality and integrity comparable to running TLS over TCP ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). The phrasing is carefully chosen: the security properties are described as *comparable* to TLS-over-TCP, not superior. What differs is the architecture. In the HTTP/2 world, TLS is a layer applied on top of a TCP connection — a separate protocol negotiation and encryption stage stacked above the transport. In QUIC, TLS 1.3 is built into the transport protocol itself, so the handshake that establishes the secure channel and the handshake that establishes the transport connection are, in effect, the same handshake. The claim worth taking from the specification is therefore one of parity in security with an improvement in structural integration, not a claim that HTTP/3 is cryptographically stronger than HTTP/2 over TLS.

### Native Multiplexing and Stream-Level Loss Isolation

The most consequential property of QUIC for HTTP is that it provides native multiplexing. Because QUIC multiplexes streams itself, lost packets only affect the streams whose data was actually lost ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). This single sentence is the crux of the entire HTTP/3 value proposition, and it is best understood by contrast with HTTP/2.

## What HTTP/3 Is

HTTP/3 is a mapping of HTTP semantics over QUIC ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). The word "mapping" is doing important work. HTTP/3 does not redefine methods, status codes, header fields, or the request/response exchange as application-level concepts. It redefines how those concepts are carried: how requests and responses are framed into streams, how streams are managed, how settings are exchanged, and how the connection is managed — all expressed in terms of QUIC streams and QUIC connection primitives rather than TCP byte streams. Developers and operators therefore encounter HTTP/3 as "the same HTTP, on a different transport," which is exactly why it can be adopted incrementally and why the comparison with HTTP/2 is fundamentally a transport comparison.

## The Core Problem: Head-of-Line Blocking in HTTP/2 over TCP

### The TCP-Level Stall

HTTP/2 introduced multiplexing at the application layer: multiple concurrent transactions share a single TCP connection. That design solved the connection-count problem of HTTP/1.1 but inherited a limitation from TCP itself. As the specification states, in HTTP/2 over TCP a lost or reordered packet causes all active transactions to experience a stall regardless of whether that transaction was directly impacted by the lost packet ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)).

The mechanism behind this is implied clearly by the statement: TCP delivers a single, ordered byte stream, and the application-layer multiplexing of HTTP/2 is invisible to TCP. TCP cannot know that bytes belonging to stream A and bytes belonging to stream B are logically independent; it sees one sequence of bytes and will not deliver later bytes until the missing earlier bytes arrive. Every multiplexed transaction on that connection therefore waits behind the same gap. The loss of one packet for one stream stalls all streams, even though the other streams' data may already have arrived intact.

### How QUIC Changes the Failure Domain

QUIC removes that coupling by making multiplexing a transport-layer capability rather than an application-layer convention. Because QUIC provides native multiplexing, a lost packet only impacts the streams whose data was lost ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). The failure domain shrinks from the entire connection to the individual affected stream or streams. A transaction that lost nothing does not wait for the retransmission of data belonging to a transaction that did.

This is the single most important architectural improvement, and it should be stated precisely. HTTP/3 does not eliminate packet loss, and it does not eliminate head-of-line blocking within a single stream — data within one stream must still be delivered in order. What it eliminates is *cross-stream* head-of-line blocking caused by the transport, which is exactly the class of blocking that HTTP/2 over TCP suffers. This is a narrower claim than "HTTP/3 removes head-of-line blocking," and it is the accurate one.

## Comparative Analysis

| Dimension | HTTP/2 (over TCP) | HTTP/3 (over QUIC) |
|---|---|---|
| Underlying transport | TCP, with TLS layered above | QUIC over UDP, with TLS 1.3 built into the transport ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3); [IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)) |
| Where multiplexing lives | Application layer, on top of a single ordered byte stream | Native to the transport protocol ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |
| Effect of a lost packet | All active transactions stall, including those not directly impacted ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)) | Only the streams whose data was lost are affected ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |
| Effect of a reordered packet | All active transactions stall ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)) | Streams not implicated are unaffected ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |
| Security | TLS over TCP | TLS 1.3 integrated at the transport layer, offering comparable confidentiality and integrity ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)) |
| Congestion control location | Kernel TCP stack | User space, over UDP ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |
| Standard | HTTP/2 | RFC 9114, Proposed Standard, 6 June 2022; transport RFC 9000, May 2021 ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |

## Interpretation and Opinion

Weighing the evidence, the defensible conclusion is that the headline improvement of HTTP/3 over HTTP/2 is neither the switch to UDP nor the encryption story, but the relocation of multiplexing from the application layer into the transport layer — and the resulting reduction in the blast radius of packet loss. The UDP substrate is a means to that end: it is what allows QUIC to implement its own reliability and stream model in user space rather than inheriting TCP's single ordered byte stream. Likewise, the TLS 1.3 integration is a parity claim about confidentiality and integrity, not a superiority claim ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)); presenting HTTP/3 as "more secure" than HTTP/2 over TLS overstates what the specification actually asserts.

The strongest evidence in the provided material therefore supports a specific and somewhat modest thesis: HTTP/3 concentrates its gains in loss-prone and reordering-prone network conditions, where the per-connection stall of HTTP/2 is most damaging. On a clean path with negligible loss, the difference between the two is far less dramatic, because the mechanism that HTTP/3 fixes is only triggered by loss or reordering. Conversely, on congested or high-jitter paths, the difference is structural rather than incremental, since every lost packet in HTTP/2 taxes every concurrent transaction on the connection ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). That is where HTTP/3 earns its place as a Proposed Standard rather than a marginal revision.

## Limitations of the Available Evidence

Two limitations should be acknowledged. First, neither source provides quantitative performance measurements — no latency figures, throughput comparisons, or measured reduction in stall time are offered — so any numeric performance claim would be unsupported and is deliberately omitted here. Second, the provided material does not address migration, connection resumption, or other QUIC features beyond those named, so those topics are outside the scope of this report. The conclusions above are limited to the mechanisms explicitly documented: the mapping of HTTP semantics onto QUIC ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)), the characterization of QUIC as a user-space transport over UDP with native multiplexing ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)), the head-of-line blocking behavior of HTTP/2 over TCP ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)), and the standardization dates of RFC 9114 and RFC 9000 ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)).

## Conclusion

HTTP/3 is HTTP's semantics mapped onto QUIC ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)), standardized as RFC 9114 on 6 June 2022, with QUIC itself specified in RFC 9000 in May 2021 ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). QUIC is a transport-layer protocol running over UDP with user-space congestion control and native multiplexing ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)), and it incorporates TLS 1.3 at the transport layer with confidentiality and integrity comparable to TLS over TCP ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). The decisive improvement over HTTP/2 is stream-level loss isolation: where a lost or reordered packet stalls all active transactions in HTTP/2 over TCP ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)), in QUIC it affects only the streams whose data was lost ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). HTTP/3 is therefore best understood not as a new version of HTTP's semantics, but as a new foundation beneath them.

## References

IETF. (2022). *HTTP/3* (RFC 9114). IETF Trust. https://www.rfc-editor.org/rfc/rfc9114.html

Wikipedia. (2026). *HTTP/3*. Retrieved September 14, 2026, from https://en.wikipedia.org/wiki/HTTP/3 (Source: document_1.txt; licensed CC BY-SA 4.0)