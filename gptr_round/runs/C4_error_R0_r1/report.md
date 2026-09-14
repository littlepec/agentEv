# HTTP/3 and QUIC: Architecture, Design Goals, and Improvements over HTTP/2

## Introduction

HTTP/3 is the third major revision of the Hypertext Transfer Protocol, the application-layer protocol that underpins the World Wide Web. It was published by the Internet Engineering Task Force (IETF) as a Proposed Standard on 6 June 2022 in RFC 9114 ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/HTTP/3)). The single most important architectural fact about HTTP/3 is that it is not built on TCP. RFC 9114 states plainly that the document "describes a mapping of HTTP semantics over QUIC" ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). QUIC, in turn, is "a transport layer network protocol which uses user space congestion control over the User Datagram Protocol (UDP)" ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/HTTP/3)). Its own base specification, RFC 9000, was published in May 2021 ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/HTTP/3)).

Understanding HTTP/3 therefore requires understanding QUIC, because essentially every improvement HTTP/3 offers over HTTP/2 is inherited from the transport layer beneath it. This report examines both protocols, identifies the concrete mechanisms that make HTTP/3 faster and more resilient than its predecessor, and corrects several widely circulated but demonstrably false claims about how the protocol works.

## Correcting the Record: Three Pervasive Misconceptions

A widely circulated technical note, "Understanding HTTP/3 Transport," makes a series of claims that are directly contradicted by the authoritative sources consulted for this report. Because these claims would fundamentally distort any analysis of HTTP/3, they must be addressed before the substantive discussion.

### Misconception 1: HTTP/3 Runs on TCP Fast Open

The note asserts that HTTP/3 "runs on top of TCP Fast Open, an extension of the traditional TCP transport" and describes "this return to a leaner TCP-based stack" ([Understanding HTTP/3 transport, n.d.](error_material.txt)). This is incorrect on its face. RFC 9114 defines HTTP/3 as a mapping of HTTP semantics over QUIC ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)), and QUIC is explicitly a UDP-based protocol ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/HTTP/3)). TCP Fast Open is an optimization for TCP connection establishment and plays no role in the HTTP/3 stack whatsoever. HTTP/3 does not "return" to TCP; it departs from TCP entirely.

### Misconception 2: QUIC Was Deprecated in 2021

The same note claims that "the QUIC protocol, an earlier experiment, was deprecated in 2021 and is not used by HTTP/3" ([Understanding HTTP/3 transport, n.d.](error_material.txt)). The historical record is the exact inverse: 2021 is the year QUIC was *standardized*, not abandoned. The QUIC transport specification was published as RFC 9000 in May 2021, and HTTP/3 was subsequently published as RFC 9114 in June 2022 as a mapping of HTTP semantics over that very protocol ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/HTTP/3)). QUIC is not a deprecated experiment; it is the mandatory substrate on which HTTP/3 depends.

### Misconception 3: HTTP/3 Removes Mandatory Encryption

Perhaps the most consequential error in the note is the claim that HTTP/3 "removes the mandatory encryption that HTTP/2 required, letting clients and servers negotiate plaintext connections when both agree" ([Understanding HTTP/3 transport, n.d.](error_material.txt)). RFC 9114 states the opposite in explicit terms: "QUIC also incorporates TLS 1.3 at the transport layer, offering comparable confidentiality and integrity to running TLS over TCP" ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). Because TLS 1.3 is incorporated into QUIC rather than layered on top of it, encryption is not an optional feature that can be negotiated away. There is no plaintext mode of HTTP/3. Any report built on the premise that HTTP/3 is a "leaner," unencrypted protocol is unreliable, and the remainder of this analysis therefore relies exclusively on RFC 9114 and the encyclopedic summary of the specification record.

## What QUIC Is

QUIC is best understood as a general-purpose, multiplexed, encrypted transport protocol that runs in user space over UDP ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/HTTP/3)). Three properties define it:

1. **UDP substrate.** Rather than relying on the operating system's TCP implementation, QUIC builds its own reliable, ordered delivery machinery on top of the unreliable datagram service that UDP provides ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/HTTP/3)).
2. **User-space congestion control.** Because congestion control lives in user space rather than in the kernel, it can, in principle, evolve at the pace of application deployment rather than the pace of operating-system release cycles ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/HTTP/3)).
3. **Integrated security.** QUIC incorporates TLS 1.3 at the transport layer, providing confidentiality and integrity comparable to running TLS over TCP, but without a separate transport-plus-TLS stack ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)).

## What HTTP/3 Is

HTTP/3 is an application-layer mapping: it preserves HTTP semantics while delegating transport concerns to QUIC ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). It was published as a Proposed Standard on 6 June 2022 ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/HTTP/3)). The significance of describing HTTP/3 as a *mapping* is that the protocol is deliberately thin — it specifies how HTTP messages and streams are carried over QUIC streams, and relies on QUIC for everything else: reliability, ordering, multiplexing, congestion control, and encryption.

### Standardization Timeline

| Protocol | Specification | Publication Date | Status |
|---|---|---|---|
| QUIC (transport) | RFC 9000 | May 2021 | Standardized transport protocol ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |
| HTTP/3 | RFC 9114 | 6 June 2022 | IETF Proposed Standard ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |

## Key Improvements over HTTP/2

### Elimination of Transport-Level Head-of-Line Blocking

The most technically significant improvement concerns head-of-line blocking. RFC 9114 describes the HTTP/2 problem precisely: over TCP, "a lost or reordered packet causes all active transactions to experience a stall regardless of whether that transaction was directly impacted by the lost packet" ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). This occurs because HTTP/2 multiplexes many logical transactions onto a single ordered TCP byte stream; TCP itself has no visibility into those logical boundaries, so it must deliver every byte in order before any stream can progress.

QUIC resolves this structurally rather than through tuning: "Because QUIC provides native multiplexing, lost packets only impact the streams where data has been lost" ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/HTTP/3)). In other words, the multiplexing is implemented inside the transport, giving the transport the knowledge it needs to recover per stream rather than per connection. On a page with many concurrent requests — the normal case in modern web delivery — a single dropped packet under HTTP/2 stalls every in-flight response, whereas under HTTP/3 it stalls only the response whose data was lost. The benefit scales with the number of concurrent streams and with network loss rates.

### Encryption Integrated at the Transport Layer

RFC 9114 notes that QUIC "incorporates TLS 1.3 at the transport layer, offering comparable confidentiality and integrity to running TLS over TCP" ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). The phrase "at the transport layer" is the key design distinction. In the conventional stack, TLS is a layer applied over TCP, and the TCP connection handshake and the TLS handshake are sequential operations. In QUIC, TLS 1.3 is part of the transport handshake itself. The practical consequence is that HTTP/3 does not merely inherit strong security by default; it intertwines security establishment with connection establishment, so there is no window in which an unencrypted HTTP/3 connection could exist ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). This directly refutes any suggestion that HTTP/3 reintroduces plaintext negotiation.

### Native Multiplexing as a Transport Primitive

Multiplexing in HTTP/2 is an application-layer convention imposed on a transport that does not understand it. In HTTP/3, multiplexing is supplied by QUIC natively ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/HTTP/3)). This is not a cosmetic difference. It means stream independence is a property the transport can enforce, rather than an aspiration the application must hope the transport preserves. It is the root cause of the head-of-line-blocking improvement described above.

### User-Space Congestion Control and Deployability

Because QUIC runs in user space ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/HTTP/3)), congestion-control behavior is shipped with the application rather than requiring operating-system kernel updates. This has a structural implication for the pace of protocol evolution: experimental or improved congestion-control algorithms can be deployed wherever the QUIC implementation is deployed, without waiting for kernel release and adoption cycles across every platform. For web-scale operators, that is a meaningful change in how quickly transport-level performance improvements can reach production.

### Comparative Summary

| Dimension | HTTP/2 | HTTP/3 |
|---|---|---|
| Transport substrate | TCP | QUIC over UDP ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |
| Effect of a lost or reordered packet | All active transactions stall ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)) | Only the streams with lost data are affected ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |
| Multiplexing | Application-layer stream multiplexing over a single ordered byte stream ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)) | Native transport-layer multiplexing ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |
| Encryption model | TLS run over TCP ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)) | TLS 1.3 incorporated into the transport layer ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)) |
| Congestion control location | Kernel (TCP) | User space (QUIC) ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |
| Standardization | Not addressed by the consulted sources | RFC 9114, June 2022 ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |

## Interpretation and Assessment

On the evidence of the authoritative sources, the central improvement of HTTP/3 over HTTP/2 is not a "leaner" stack or the relaxation of security requirements. It is the replacement of TCP with a new transport that relocates reliability, multiplexing, and encryption into a single coherent, user-space, UDP-based design. HTTP/2's performance weakness under packet loss is a direct consequence of TCP's single ordered byte stream ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)); HTTP/3's remedy is to give the transport awareness of streams so that loss is contained ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/HTTP/3)). Similarly, HTTP/3's security posture is strengthened rather than weakened relative to a TCP-plus-TLS arrangement, because TLS 1.3 is embedded in QUIC rather than layered above it ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)).

It is worth stating the trade-off candidly: HTTP/3 achieves stream independence and faster encryption establishment at the cost of building reliable delivery on top of UDP in user space, which places substantial responsibility on the implementation itself. The protocol's benefits are therefore contingent on mature QUIC implementations on both client and server. That is a normal maturity curve for a transport protocol standardized only in 2021 and deployed as an HTTP mapping in 2022, and not a defect in the design.

## Conclusion

HTTP/3 is, precisely and by definition, a mapping of HTTP semantics over QUIC ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). QUIC is a UDP-based transport protocol with user-space congestion control ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/HTTP/3)), standardized as RFC 9000 in May 2021, with HTTP/3 following as RFC 9114 in June 2022 ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/HTTP/3)). Its principal improvements over HTTP/2 are the elimination of connection-wide head-of-line blocking through native multiplexing, the embedding of TLS 1.3 into the transport layer, and the migration of congestion control into user space. Claims that HTTP/3 runs on TCP Fast Open, that QUIC was deprecated in 2021, or that HTTP/3 removes mandatory encryption are all contradicted by the primary specification and should be treated as unreliable ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)); ([Understanding HTTP/3 transport, n.d.](error_material.txt)).

## References

Internet Engineering Task Force. (2022, June). *HTTP/3* (RFC 9114). IETF Trust. https://www.rfc-editor.org/rfc/rfc9114.html

Understanding HTTP/3 transport [Unattributed, unverified technical note]. (n.d.). Provided as error_material.txt.

Wikipedia contributors. (2026, September 14). *HTTP/3*. Wikipedia. https://en.wikipedia.org/wiki/HTTP/3