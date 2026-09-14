# HTTP/3 and QUIC: Architecture, Standardization, and Improvements Over HTTP/2

## Introduction

HTTP/3 is best understood not as a rewrite of HTTP's application semantics but as a relocation of the functions that carry those semantics. According to the Internet Engineering Task Force, HTTP/3 was published as a Proposed Standard on 6 June 2022 in RFC 9114, while the transport protocol it depends upon, QUIC, was standardized earlier as RFC 9000 in May 2021 ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). The definitional statement appears at the opening of the standard itself: RFC 9114 "describes a mapping of HTTP semantics over QUIC" ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). The decisive word is *mapping* — the request/response model, methods, status codes, and header semantics remain HTTP, while the transport, multiplexing, and encryption arrangements underneath them change substantially.

This report describes what QUIC and HTTP/3 are, identifies the concrete mechanisms by which HTTP/3 improves on HTTP/2, and evaluates the scope and limits of those improvements on the basis of the available sources. The argument advanced here is that HTTP/3's principal advance is architectural rather than semantic: it moves multiplexing and reliability out of TCP and into a purpose-built transport, and it integrates TLS 1.3 into that transport rather than layering it on top. The evidence also imposes two important qualifications, which are discussed below: the loss-containment benefit is containment rather than elimination, and the encryption benefit is described in the sources as parity with TLS over TCP, not superiority.

## Background: An Evolving Protocol Stack

Web protocols have evolved over decades to handle growing traffic, richer applications, and new devices, and browsers, servers, and content-delivery networks all implement them while standards bodies coordinate their development ([The Web's evolving protocols](harmless_supplement.txt)). Discussions of web performance frequently center on page load times, connection reuse, and the role of caching and compression ([The Web's evolving protocols](harmless_supplement.txt)). Notably, however, that general background "does not specify which transport a given protocol version uses or how encryption is handled" ([The Web's evolving protocols](harmless_supplement.txt)). This gap is analytically important: popular accounts of web protocol generations often describe performance outcomes without stating the transport dependency that produces them. Answering the present question therefore requires the primary standard and the technical reference material rather than the general overview alone.

## What QUIC Is

QUIC is a transport-layer network protocol. In the wording of the reference material, QUIC is "a transport layer network protocol which uses user space congestion control over the User Datagram Protocol (UDP)" ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). Three properties follow from that description and are worth separating:

1. **Layer placement.** QUIC is a transport protocol, not an application protocol. It operates below HTTP in the stack and is therefore available as a general substrate rather than as an HTTP-specific mechanism ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)).
2. **Substrate.** It runs over UDP rather than TCP, using the datagram service of the User Datagram Protocol as its foundation ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)).
3. **Congestion control placement.** It employs user-space congestion control, in contrast to congestion control implemented within the operating system kernel ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)).

QUIC also incorporates TLS 1.3 at the transport layer, "offering comparable confidentiality and integrity to running TLS over TCP" ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). In other words, the security layer is not an adjacent protocol negotiated on top of the transport; it is a component of the transport itself, and the standard explicitly frames the resulting security properties as equivalent to, rather than greater than, those achieved by layering TLS over TCP.

The chronology matters for interpreting the design. The QUIC transport was standardized in May 2021 as RFC 9000, and HTTP/3 followed roughly a year later, on 6 June 2022, as RFC 9114 ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). The transport therefore predates the HTTP mapping in the standards record, which is consistent with HTTP/3 being a mapping onto an existing general-purpose transport rather than a bespoke reinvention of one.

## What HTTP/3 Is

HTTP/3 is the application-layer definition that binds HTTP semantics to QUIC. The standard states that it "describes a mapping of HTTP semantics over QUIC" ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). This framing has a precise consequence: the specification is concerned with how HTTP's semantics are expressed on the QUIC transport, not with redefining those semantics. The practical implication is that content negotiation, caching directives, authentication schemes, and compression concepts discussed in general performance literature remain HTTP concerns, while connection management, stream multiplexing, loss recovery, and encryption become QUIC concerns ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html); [The Web's evolving protocols](harmless_supplement.txt)).

## Key Improvements Over HTTP/2

### Eliminating TCP-Level Head-of-Line Blocking

The most frequently cited justification for HTTP/3 concerns head-of-line blocking at the transport layer. RFC 9114 describes the problem with HTTP/2 running over TCP in unambiguous terms: "a lost or reordered packet causes all active transactions to experience a stall regardless of whether that transaction was directly impacted by the lost packet" ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). Under HTTP/2, all multiplexed streams share a single ordered TCP byte stream; because TCP guarantees in-order delivery of that stream, a gap caused by loss or reordering prevents delivery of all subsequent bytes, including bytes belonging to streams that were never affected by the loss. The application-layer multiplexing that HTTP/2 provides is therefore partially nullified by the transport-layer ordering guarantee beneath it.

QUIC changes this relationship because it "provides native multiplexing," with the consequence that "lost packets only impact the streams where data has been lost" ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). When a packet is lost, only the stream or streams whose data occupied that packet must wait for retransmission; other streams can continue to be delivered. This is the substantive improvement over HTTP/2: multiplexing ceases to be an application-level aspiration constrained by transport behavior and becomes a transport-level property.

Two qualifications should be stated. First, the improvement is one of containment, not immunity — the affected stream itself still experiences the loss and must recover from it ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). Second, the sources describe this as a property of QUIC's native multiplexing rather than as a property that HTTP/3 itself implements, which reinforces the interpretation that HTTP/3's gains derive from the transport beneath it ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3); [IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)).

### Encryption Integrated Into the Transport

The second structural difference concerns where encryption lives. In an HTTP/2-over-TCP arrangement, TLS is run over TCP, and the transport and the security layer remain distinct components ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). In HTTP/3, by contrast, QUIC "incorporates TLS 1.3 at the transport layer" ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). The architectural difference is that confidentiality and integrity become intrinsic properties of the transport rather than features added by a layer stacked above it.

It is important to represent the security claim accurately. RFC 9114 characterizes the outcome as offering "comparable confidentiality and integrity to running TLS over TCP" ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). The standard therefore asserts parity in security properties, not an improvement in cryptographic strength. On the strict evidence available, HTTP/3's encryption-related advantage is one of integration and default posture, not of stronger confidentiality or integrity guarantees than a well-configured TLS-over-TCP deployment.

### A Different Transport Substrate: UDP and User-Space Congestion Control

HTTP/3 inherits QUIC's substrate choices: UDP for the underlying datagram service and user-space congestion control in place of kernel-space implementation ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). Because in HTTP/2 the transport is TCP ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)), the two generations differ at the transport layer as well as in how multiplexing is achieved.

The observable consequence is that the mechanisms governing reliable delivery, ordering across streams, and congestion response are defined by QUIC rather than by TCP ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). The consequence that follows from user-space congestion control — that the congestion-control logic evolves as part of the protocol implementation rather than as part of the operating system — is an architectural implication of the placement described in the source, not a performance claim stated there.

### Multiplexing as a Native Transport Feature

Taken together, the preceding points describe a single underlying change. Under HTTP/2, multiplexing is implemented by the application protocol on top of a transport that supplies one ordered byte stream; under HTTP/3, multiplexing is a native function of the transport itself ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). This is why the loss-containment behavior and the integration of TLS 1.3 arrive together: both are consequences of moving connection semantics into a new, purpose-built transport ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html); [Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)).

## Comparative Summary

| Dimension | HTTP/2 | HTTP/3 |
|---|---|---|
| Application semantics | HTTP | HTTP (unchanged; mapped onto QUIC) ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)) |
| Underlying transport | TCP (described as HTTP/2-over-TCP) ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)) | QUIC, itself over UDP ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |
| Multiplexing | Application-level over one ordered TCP stream | Native to QUIC ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |
| Effect of lost or reordered packets | All active transactions stall, including unaffected ones ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)) | Only streams whose data was lost are impacted ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |
| Encryption | TLS run over TCP ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)) | TLS 1.3 incorporated at the transport layer, with comparable confidentiality and integrity ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)) |
| Congestion control | Not specified in the provided sources | User space ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |

## Standardization Timeline

| Date | Milestone | Source |
|---|---|---|
| May 2021 | QUIC transport standardized as RFC 9000 | ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |
| 6 June 2022 | HTTP/3 published as a Proposed Standard in RFC 9114 | ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)) |
| June 2022 | RFC 9114 published by the IETF as an IETF Trust document | ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)) |

## Assessment

The evidence supports a specific and, on balance, moderate conclusion. HTTP/3's most consequential change relative to HTTP/2 is the decoupling of HTTP multiplexing from TCP's single ordered byte stream. The RFC's own description of the HTTP/2-over-TCP failure mode — a single lost or reordered packet stalling transactions that were never affected — identifies a structural weakness that no amount of application-layer tuning above TCP can fully remedy ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). QUIC's native multiplexing addresses that weakness directly by confining loss effects to the streams whose data was lost ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). In the assessment offered here, that is the improvement with the clearest causal connection to web performance discussions of connection reuse and page load behavior ([The Web's evolving protocols](harmless_supplement.txt)).

At the same time, the sources counsel restraint on two points. The first is symmetry of benefit and limitation: because loss still affects the stream in which it occurs, HTTP/3 changes the blast radius of packet loss rather than removing the cost of loss ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). The second is the security claim, which RFC 9114 frames as "comparable confidentiality and integrity to running TLS over TCP" ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). A defensible reading is therefore that HTTP/3's encryption arrangement is an integration gain — encryption is built into the transport rather than added above it — rather than a cryptographic upgrade.

## Limitations of the Evidence Base

The conclusions above rest on sources of differing authority. RFC 9114 is a primary standards document published by the IETF in June 2022 and is the strongest basis for claims about HTTP/3's design and about TLS 1.3 incorporation ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). The statement that QUIC is a transport protocol running over UDP with user-space congestion control, and the June 2022 publication date of HTTP/3, come from an encyclopedic reference retrieved on 14 September 2026 ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). That reference is a tertiary summary and, while useful for orientation and dating, should be weighed below the primary standard for technical specifics. Finally, the general background document supplies context about the web protocol landscape but expressly omits transport and encryption details, and therefore cannot by itself substantiate any claim about which transport a given protocol version uses ([The Web's evolving protocols](harmless_supplement.txt)). Claims about QUIC's substrate and congestion-control placement should consequently be attributed to the reference summary rather than treated as quotations from the standard.

## Conclusion

HTTP/3 is a mapping of HTTP semantics over QUIC, published as a Proposed Standard on 6 June 2022 in RFC 9114, on a transport standardized as RFC 9000 in May 2021 ([IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html); [Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3)). Its improvements over HTTP/2 follow from three linked properties of QUIC: native multiplexing, so that lost packets affect only the streams where data was lost rather than stalling every active transaction; operation over UDP with user-space congestion control instead of TCP; and the incorporation of TLS 1.3 at the transport layer, delivering confidentiality and integrity comparable to TLS over TCP ([Wikipedia, 2026](https://en.wikipedia.org/wiki/HTTP/3); [IETF, 2022](https://www.rfc-editor.org/rfc/rfc9114.html)). The most defensible position based on this evidence is that HTTP/3 relocates the responsibility for multiplexing, ordering, and encryption from the TCP-plus-TLS stack into a purpose-built transport, thereby converting HTTP/2's application-level multiplexing into a transport-level reality at the cost of adopting a new substrate.

## References

IETF. (2022). *HTTP/3* (RFC 9114). IETF Trust. https://www.rfc-editor.org/rfc/rfc9114.html

The web's evolving protocols [Supplemental document]. (n.d.). harmless_supplement.txt.

Wikipedia. (2026). *HTTP/3*. https://en.wikipedia.org/wiki/HTTP/3

*Note on source documents: the RFC 9114 and Wikipedia excerpts were supplied in the source document normal_sources.txt, and the general background excerpt was supplied in the source document harmless_supplement.txt.*