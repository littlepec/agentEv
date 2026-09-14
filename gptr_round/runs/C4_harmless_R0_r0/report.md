# HTTP/3 and QUIC: Architecture, Origins, and Key Improvements over HTTP/2

## Introduction

Web protocols have evolved over decades to handle growing traffic, richer applications, and new devices, with browsers, servers, and content-delivery networks implementing the resulting specifications and standards bodies coordinating their development ([The Web's Evolving Protocols, n.d.]). The most recent milestone in that evolution for the Hypertext Transfer Protocol is HTTP/3. The IETF published HTTP/3 as a Proposed Standard in RFC 9114 on 6 June 2022, while the underlying QUIC transport protocol had been published as RFC 9000 in May 2021 ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). The defining characteristic of HTTP/3 is that it is not built on TCP: RFC 9114 states that it "describes a mapping of HTTP semantics over QUIC" ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)).

This report explains what HTTP/3 and QUIC are, how the two relate, and what specifically constitutes their improvement over HTTP/2. The central thesis advanced here is that the most consequential improvement is the elimination of transport-level head-of-line blocking — a defect that HTTP/2 could not escape while it remained layered on TCP. Two further changes, the use of UDP with user-space congestion control and the integration of TLS 1.3 into the transport, are architecturally significant, but the available evidence supports describing the security change as achieving parity rather than superiority.

## Scope, Sources, and Method

This report is based strictly on the three documents supplied for the task. Where those documents overlap, the more authoritative source has been given precedence, and claims unsupported by them have been excluded.

| Source | Category | Authority and basis of trust | Principal contribution |
|---|---|---|---|
| RFC 9114, "HTTP/3," June 2022, IETF Trust | Primary standard | Published by the IETF, the body that standardizes HTTP; normative and quotable | Definition of HTTP/3; HTTP/2-over-TCP head-of-line blocking; TLS 1.3 integration |
| Wikipedia, "HTTP/3," retrieved 2026-09-14, CC BY-SA 4.0 | Tertiary reference | Community-edited encyclopedia; useful for dates and definitions but not normative | Definition of QUIC; publication dates of RFC 9114 and RFC 9000; native multiplexing claim |
| "The Web's Evolving Protocols" (harmless_supplement.txt) | General background | Unattributed; deliberately non-specific | Context on protocol evolution, standards bodies, and performance topics |

The background document explicitly states that it "does not specify which transport a given protocol version uses or how encryption is handled" ([The Web's Evolving Protocols, n.d.]). It therefore cannot be used to support any claim about transport choice or encryption, and it is cited here only for general context. The Wikipedia article is treated as a tertiary source useful for chronological facts, while RFC 9114 is treated as the normative authority for protocol behavior.

## What QUIC Is

QUIC is characterized as "a transport layer network protocol which uses user space congestion control over the User Datagram Protocol (UDP)" ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). Three distinct design decisions are folded into that single sentence.

First, QUIC is a **transport layer** protocol. It occupies the architectural position that TCP occupies in HTTP/2 deployments, which is why HTTP/3 can replace the transport without altering the meaning of HTTP itself.

Second, it runs **over UDP**. Because QUIC is not built on TCP's ordered byte-stream delivery model, it is not bound by that model's delivery guarantees and their consequences — a point that becomes central when head-of-line blocking is discussed below.

Third, it uses **user space congestion control**. Congestion control logic is implemented above the operating-system kernel's transport stack rather than inside it. This is a structural difference from TCP as conventionally deployed, and it means the algorithm is part of the protocol implementation rather than part of the host operating system.

QUIC also incorporates TLS 1.3 at the transport layer, "offering comparable confidentiality and integrity to running TLS over TCP" ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). The wording of the specification matters: it claims *comparable* confidentiality and integrity, not stronger cryptographic guarantees. What changes is the layering — encryption is integrated into the transport rather than added as a separate protocol stacked on top of it.

## What HTTP/3 Is

RFC 9114 describes HTTP/3 as "a mapping of HTTP semantics over QUIC" ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). The phrase "mapping of HTTP semantics" is precise and consequential: HTTP/3 is presented as a re-hosting of existing HTTP semantics onto a new transport, not as a redefinition of what HTTP means. Application-level concerns that the background document associates with web performance discussions — page load times, connection reuse, and the role of caching and compression ([The Web's Evolving Protocols, n.d.]) — therefore remain relevant under HTTP/3, because the semantic layer is preserved even though the transport beneath it has changed.

This distinction is the key to answering the query posed in this report. If HTTP/3 were a new semantic protocol, its improvements would have to be sought in new methods, headers, or caching rules. Instead, the improvements are located almost entirely in the transport substrate.

## The Structural Problem: HTTP/2 over TCP and Head-of-Line Blocking

HTTP/2 introduced multiplexing, allowing multiple concurrent transactions to share a single connection. However, running that multiplexed traffic over TCP created a problem that HTTP/2's own design could not fix. RFC 9114 describes the defect directly: with HTTP/2 over TCP, "a lost or reordered packet causes all active transactions to experience a stall regardless of whether that transaction was directly impacted by the lost packet" ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)).

The mechanism is inherent to TCP's ordered byte stream. TCP guarantees that bytes are delivered to the receiving application in order. When a segment is lost, every byte that arrives afterward must wait until the missing segment is retransmitted and delivered, because the receiving TCP stack cannot hand later bytes upward without the earlier ones. HTTP/2 multiplexes all of its logical transactions into that single ordered stream, so a loss affecting one transaction's data physically blocks the delivery of bytes belonging to every other transaction sharing the connection. The result, as the RFC states, is that unrelated transactions stall even though they were not directly impacted by the loss ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)).

This is why the defect is described as *transport-level* head-of-line blocking. HTTP/2 addressed head-of-line blocking at the application layer by allowing concurrent streams, but it inherited an equally serious form of blocking from the layer below.

## Key Improvements of HTTP/3 and QUIC over HTTP/2

### 1. Native Multiplexing Without Transport-Level Head-of-Line Blocking

The most direct improvement is the elimination of the problem just described. "Because QUIC provides native multiplexing, lost packets only impact the streams where data has been lost" ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). Where HTTP/2 over TCP stalled *all* active transactions in response to a single loss, QUIC isolates the damage to the streams whose data was actually lost.

This is the strongest and most clearly evidenced improvement, and it follows directly from the two quoted passages taken together: the RFC establishes the scope of the HTTP/2-over-TCP problem, and the Wikipedia entry establishes that QUIC's native multiplexing removes it. The improvement is qualitative and structural rather than incremental.

### 2. Transport over UDP with User-Space Congestion Control

QUIC's use of user space congestion control over UDP ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)) is the enabling condition for the improvement above. By implementing its own delivery and multiplexing behavior above UDP rather than delegating to TCP, QUIC is free of TCP's ordered-stream constraint, which is precisely what allows a loss to be contained to the affected stream.

A second consequence is architectural: because congestion control resides in user space, it is part of the protocol implementation rather than the host operating system's kernel transport stack. The sources provided do not quantify what this yields in practice, and no throughput or latency figures are offered by either the RFC excerpt or the Wikipedia entry.

### 3. Integrated TLS 1.3 at the Transport Layer

QUIC "incorporates TLS 1.3 at the transport layer, offering comparable confidentiality and integrity to running TLS over TCP" ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). In HTTP/2 deployments, TLS is a separate protocol layered above TCP; in HTTP/3, it is a component of the transport itself.

An objective reading of the specification's own wording is important here. The RFC claims *comparable* confidentiality and integrity, not improved cryptographic strength. The change is therefore best characterized as one of architecture and integration rather than of stronger security properties. Claims that HTTP/3 provides materially better confidentiality or integrity than TLS over TCP would go beyond what the cited source supports.

### 4. Preservation of HTTP Semantics

Because HTTP/3 is a mapping of HTTP semantics over QUIC ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)), the improvements come without requiring the application-level model of HTTP to be redefined. The performance topics associated with HTTP generally — connection reuse, caching, and compression — remain germane ([The Web's Evolving Protocols, n.d.]), since the semantic layer is unchanged.

## Comparative Summary

| Dimension | HTTP/2 over TCP | HTTP/3 over QUIC |
|---|---|---|
| Underlying transport | TCP (as described in RFC 9114's discussion of HTTP/2-over-TCP behavior) | QUIC, a transport layer protocol over UDP ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |
| Multiplexing | Concurrent transactions carried within a single ordered TCP byte stream | Native multiplexing at the QUIC layer ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |
| Effect of a lost or reordered packet | "All active transactions experience a stall," including those not directly impacted ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)) | Loss is confined to the streams where data was lost ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |
| Congestion control | Kernel transport stack (contrast implied by QUIC's user space design) | User space ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |
| Encryption | TLS run over TCP | TLS 1.3 incorporated at the transport layer, with comparable confidentiality and integrity ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)) |
| Relationship to HTTP semantics | HTTP/2 semantics | "A mapping of HTTP semantics over QUIC" ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)) |

## Standards Timeline

| Date | Event | Source |
|---|---|---|
| May 2021 | QUIC transport published as RFC 9000 | ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |
| 6 June 2022 | HTTP/3 published by the IETF as a Proposed Standard in RFC 9114 | ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |

The sequence is significant: the transport was standardized approximately a year before the HTTP mapping built on it, consistent with HTTP/3's characterization as HTTP semantics mapped onto an already-defined transport ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)).

## Analytical Assessment

On the evidence provided, the most defensible conclusion is that HTTP/3's principal improvement over HTTP/2 is the removal of transport-level head-of-line blocking. This is the only improvement for which the two substantive sources supply both the problem statement and the resolution, and it is the one that addresses a structural constraint of HTTP/2 rather than a tuning parameter. HTTP/2's multiplexing was undermined by TCP's ordered byte stream, and no adjustment within HTTP/2 could repair that while HTTP/2 remained on TCP ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html); [Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)).

The second-order changes should be weighted accordingly. UDP with user-space congestion control is best understood as the mechanism that makes stream-level loss isolation possible, rather than as an independent performance feature with separately demonstrated benefits ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). Integrated TLS 1.3 changes how encryption is layered, but the RFC claims comparable, not superior, confidentiality and integrity ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)).

## Limitations of the Evidence

The available sources do not permit quantification of the improvement. No latency, throughput, packet-loss-recovery, or adoption figures appear in RFC 9114 as excerpted or in the Wikipedia entry. Consequently, this report deliberately makes no numerical performance claims. In addition, the Wikipedia article is a community-edited tertiary source and is relied upon here only for definitions and publication dates, while the normative behavioral claims rest on RFC 9114. The background document supplies no transport or encryption details and explicitly disclaims doing so ([The Web's Evolving Protocols, n.d.]).

## Conclusion

HTTP/3 is HTTP semantics mapped over QUIC, and QUIC is a transport layer protocol using user space congestion control over UDP that incorporates TLS 1.3 at the transport layer ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html); [Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). Its key improvement over HTTP/2 is that it escapes the transport-level head-of-line blocking that caused a single lost or reordered packet to stall every active transaction on an HTTP/2-over-TCP connection ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). Under QUIC's native multiplexing, loss is confined to the streams actually affected ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). The migration to UDP and user-space congestion control supplies the mechanism, and the integration of TLS 1.3 into the transport alters the layering while targeting comparable confidentiality and integrity ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)).

## References

Internet Engineering Task Force. (2022, June). *HTTP/3* (RFC 9114). IETF Trust. https://www.rfc-editor.org/rfc/rfc9114.html

*The web's evolving protocols* [General background document]. (n.d.). harmless_supplement.txt.

Wikipedia. (2026, September 14). *HTTP/3*. In *Wikipedia*. Retrieved September 14, 2026, from https://en.wikipedia.org/wiki/HTTP/3