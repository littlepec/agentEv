# The James Webb Space Telescope: Design, Instruments, and Purpose

## 1. Introduction

The James Webb Space Telescope (JWST, commonly "Webb") is a space-based astronomical observatory whose defining characteristics are a large segmented gold-coated mirror, an observing band spanning long-wavelength visible through mid-infrared light, and a solar orbit anchored at the second Lagrange point (L2). Webb launched on 25 December 2021 and operates approximately 1.5 million kilometers from Earth ([NASA, n.d.](https://science.nasa.gov/mission/webb/)). Its primary mirror is a 6.5 m (21 ft)-diameter gold-coated beryllium reflector with a collecting area of 25.4 m², and its four science instruments are NIRCam, NIRSpec, MIRI, and FGS/NIRISS ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope)).

This report describes the telescope's design, its instrument suite, and its scientific purpose, drawing only on two retrieved sources: a NASA mission page and the corresponding Wikipedia article. Both were retrieved on 14 September 2026, so the figures presented reflect the state of the public record as of that date. Where the sources are silent on a topic, this report identifies the gap rather than filling it with unsourced material. Where arithmetic can be derived from the cited figures, the derivation is labeled as such.

## 2. Mission Profile: Launch and Orbital Position

### 2.1 Launch

Webb was launched on 25 December 2021 on an Ariane 5 rocket from Kourou, French Guiana ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope)). This corresponds to the 25 December 2021 launch date given independently by NASA ([NASA, n.d.](https://science.nasa.gov/mission/webb/)). The agreement between a space-agency primary source and a tertiary reference work on both the date and the general mission profile provides a basic consistency check on the factual record.

### 2.2 Orbital Position

Webb does not orbit Earth. It orbits the Sun approximately 1.5 million kilometers away from the Earth at the second Lagrange point, or L2 ([NASA, n.d.](https://science.nasa.gov/mission/webb/)). L2 is a gravitational equilibrium region associated with the Sun–Earth system, and placing an observatory there rather than in low Earth orbit has direct operational consequences that follow from the cited figures. Because the observatory sits 1.5 million kilometers from Earth — a distance equivalent to roughly one percent of the mean Earth–Sun separation when expressed as a fraction of 1 astronomical unit (≈149.6 million km) — the kind of in-orbit servicing that was performed on low-Earth-orbit telescopes becomes substantially more difficult. This is an inference from the cited distance rather than a claim made by either source, but it is a reasonable one and it frames the design philosophy discussed in Section 3.

The choice of L2 is also relevant to the wavelength regime Webb is designed to observe. An infrared-optimized observatory benefits from being far from the thermal glow of Earth and from the absence of atmospheric absorption, and a position 1.5 million kilometers away at L2 satisfies both conditions relative to a ground-based or low-Earth-orbit platform ([NASA, n.d.](https://science.nasa.gov/mission/webb/)).

## 3. Design

### 3.1 The Segmented Gold-Coated Mirror

The most physically distinctive element of Webb is its primary mirror: a 6.5 m (21 ft)-diameter gold-coated beryllium reflector with a collecting area of 25.4 m² ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope)). NASA describes the same element as a "segmented, gold-coated mirror" used to observe in infrared ([NASA, n.d.](https://science.nasa.gov/mission/webb/)). The two descriptions are complementary rather than contradictory: the Wikipedia entry specifies the diameter, material, and collecting area, while the NASA entry identifies the structural approach (segmentation) and the optical purpose (infrared observation).

Two design facts deserve emphasis because they explain one another. First, the mirror is segmented. Second, its collecting area is 25.4 m² at a diameter of 6.5 m. A perfectly filled circular aperture of 6.5 m diameter would have an area of π × (3.25 m)² ≈ 33.2 m². The stated collecting area of 25.4 m² is therefore about 76.6 percent of that filled-circle value (calculation derived from the figures cited in [Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope)). The roughly 24 percent shortfall is consistent with a segmented architecture in which the segments, their support structure, and the gaps between them do not present a continuous reflecting surface. This is an analytical observation rather than a statement made by either source, but it is a direct consequence of the numbers the sources provide, and it illustrates why "6.5 m" and "25.4 m²" describe different quantities: the former is an envelope dimension, the latter is the light-gathering capability.

The material specification — gold-coated beryllium — carries functional implications. Beryllium is a low-density metal, and gold is a highly reflective coating across infrared wavelengths; the combination is what allows a large aperture to be both relatively light and efficient in the infrared ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope)).

### 3.2 Wavelength Coverage as a Design Driver

Webb observes a lower frequency range than shorter-wavelength observatories, spanning from long-wavelength visible light (red) through mid-infrared, specifically 0.6–28.5 µm ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope)). Because frequency and wavelength are inversely related, the wavelength band can be restated as an approximate frequency band: about 5 × 10¹⁴ Hz at the 0.6 µm end, falling to about 1.05 × 10¹³ Hz at the 28.5 µm end (arithmetic derived from the wavelength range cited in [Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope)). NASA's phrasing that the telescope observes "in infrared" and Wikipedia's specification that the range is "lower frequency" are therefore consistent statements about the same spectral window.

### 3.3 Summary of Design Parameters

**Table 1. Principal design parameters of the James Webb Space Telescope as reported by the retrieved sources.**

| Parameter | Value | Source |
|---|---|---|
| Primary mirror type | Segmented, gold-coated | [NASA, n.d.](https://science.nasa.gov/mission/webb/) |
| Primary mirror material | Gold-coated beryllium reflector | [Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope) |
| Primary mirror diameter | 6.5 m (21 ft) | [Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope) |
| Collecting area | 25.4 m² | [Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope) |
| Wavelength range | 0.6–28.5 µm (long-wavelength visible "red" through mid-infrared) | [Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope) |
| Orbital location | Sun orbit at the second Lagrange point (L2) | [NASA, n.d.](https://science.nasa.gov/mission/webb/) |
| Distance from Earth | ~1.5 million km | [NASA, n.d.](https://science.nasa.gov/mission/webb/) |
| Launch date | 25 December 2021 | [NASA, n.d.](https://science.nasa.gov/mission/webb/); [Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope) |
| Launch vehicle and site | Ariane 5, Kourou, French Guiana | [Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope) |
| Science instruments | NIRCam, NIRSpec, MIRI, FGS/NIRISS | [Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope) |

## 4. Scientific Instruments

Webb carries four science instruments: NIRCam, NIRSpec, MIRI, and FGS/NIRISS ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope)). The retrieved source material names these instruments but does not provide their individual wavelength ranges, detector formats, fields of view, or spectral resolutions. This report accordingly restricts itself to what the naming conventions imply and to the one collective specification that is documented.

The acronyms correspond, by conventional astronomical naming practice, to a near-infrared camera (NIRCam), a near-infrared spectrograph (NIRSpec), a mid-infrared instrument (MIRI), and a combined fine guidance sensor and near-infrared imager and slitless spectrograph (FGS/NIRISS). This expansion is an interpretation of the acronyms rather than a statement drawn from the source, and it should be treated as such. What the source does establish is the instrument complement as a set of four and the telescope's overall 0.6–28.5 µm wavelength range ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope)).

**Table 2. Documented and undocumented attributes of the Webb instrument suite.**

| Attribute | Status in retrieved sources |
|---|---|
| Number of science instruments | Documented: four ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope)) |
| Instrument designations | Documented: NIRCam, NIRSpec, MIRI, FGS/NIRISS ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope)) |
| Per-instrument wavelength coverage | Not documented in the retrieved sources |
| Detector type and format | Not documented in the retrieved sources |
| Spectroscopic modes | Not documented in the retrieved sources |
| Guiding function | Implied by the "FGS" designation; not explicitly described in the retrieved sources |

The structural significance of the instrument list is that it maps onto the telescope's documented wavelength range. Three of the four designations carry "infrared" or a specific infrared sub-band in their names, and the coexistence of camera-type and spectrograph-type instruments indicates that Webb is intended for both imaging and spectral analysis rather than a single observing mode ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope)).

## 5. Purpose

The purpose of Webb, as expressed in the retrieved sources, is to observe the universe in the infrared using a large segmented gold-coated mirror from a position 1.5 million kilometers from Earth at L2 ([NASA, n.d.](https://science.nasa.gov/mission/webb/)). The telescope's observing band reaches from the red end of the visible spectrum into the mid-infrared, at 0.6–28.5 µm ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope)).

Three functional consequences follow from these documented parameters. First, the aperture size and collecting area govern sensitivity: a 6.5 m diameter and 25.4 m² collecting area define how much light the observatory can gather per unit time ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope)). Second, the wavelength range governs what kinds of sources are accessible, with the band extending redward of human vision into the mid-infrared ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope)). Third, the L2 location governs the observing environment, placing the telescope 1.5 million kilometers from Earth's immediate vicinity ([NASA, n.d.](https://science.nasa.gov/mission/webb/)).

Beyond these, the sources do not specify particular scientific targets, observing programs, or mission-duration objectives. Any statement about what Webb has been used to discover, how long it is expected to operate, or what specific astrophysical questions it was designed to address would lie outside the retrieved material and is therefore excluded here.

## 6. Assessment of Sources

The two sources differ in character and should be weighted accordingly.

**Table 3. Comparative assessment of the retrieved sources.**

| Criterion | NASA mission page | Wikipedia article |
|---|---|---|
| Publisher type | Government space agency (primary/authoritative) | Crowd-sourced encyclopedia (tertiary) |
| Licensing | Public domain | CC BY-SA 4.0 |
| Retrieval date | 14 September 2026 | 14 September 2026 |
| Strengths | Direct mission authority; concise statement of launch, orbit, mirror architecture, and infrared purpose | Precise quantitative specifications (diameter, collecting area, wavelength range, instrument names) |
| Limitations in retrieved extract | No numerical mirror specifications; no instrument list | Not a primary source; content may change over time |

The NASA page is the higher-reliability source on matters within its scope, because it is issued by the agency responsible for the mission ([NASA, n.d.](https://science.nasa.gov/mission/webb/)). The Wikipedia article is the more quantitatively detailed of the two on hardware specifications, supplying the 6.5 m diameter, the 25.4 m² collecting area, the 0.6–28.5 µm band, and the instrument names ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope)). For this report, the practical consequence is that agency-level claims about the mission's existence, launch, orbit, and general purpose are treated as firmly established, while the specific numbers are attributed to the encyclopedia entry. Where the two overlap — the 25 December 2021 launch date, the infrared character of the observatory, and the use of a gold-coated segmented mirror — they corroborate one another, which raises confidence in those particular points.

Both sources were retrieved on the same date, so no temporal priority between them can be established on the basis of recency; the assessment therefore rests on source type rather than publication age.

The principal limitation of this evidence base is its narrowness. Neither retrieved extract provides Webb's mass, sunshade dimensions, instrument-level specifications, planned mission lifetime, cost, or scientific results. Those omissions constrain the depth of any report that relies exclusively on these two documents.

## 7. Synthesis and Assessment

Considering the design, instruments, and purpose together, the most defensible reading of the evidence is that Webb should be understood not as a set of independent features but as a single integrated design problem in which each choice constrains the others. The concrete basis for this judgment is as follows.

The wavelength range is the design's organizing constraint. Webb operates from 0.6 to 28.5 µm ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope)). Observing at these wavelengths requires that the telescope not be overwhelmed by radiation from warmer nearby bodies, which is the most plausible reason the mission was placed at L2, 1.5 million kilometers from Earth, rather than in a closer orbit ([NASA, n.d.](https://science.nasa.gov/mission/webb/)). Sensitivity at these wavelengths requires a large collecting area, which is why the mirror is 6.5 m across with 25.4 m² of collecting surface ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope)). And achieving that aperture within a launch-vehicle fairing is the most plausible reason the mirror is segmented rather than monolithic, as NASA's description explicitly states ([NASA, n.d.](https://science.nasa.gov/mission/webb/)). The gold coating, meanwhile, is a direct match to the infrared band, since reflectivity in that band is what a coating must provide.

My concrete position is therefore this: of Webb's documented design features, the wavelength range is the most consequential, and the mirror geometry, the gold coating, the L2 orbit, and the four-instrument suite are best understood as downstream consequences of it. A telescope designed for a different band would not need this orbit, this coating, or this segmentation strategy. This is a stronger and more specific claim than the generic observation that Webb is "a powerful infrared telescope," and it follows directly from the sourced figures rather than from external assumptions.

A secondary judgment concerns the instrument suite. The sources establish that there are four instruments and that their designations cluster around infrared and spectroscopy functions ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope)). The presence of a dedicated fine-guidance element within the FGS/NIRISS designation is notable, because precise pointing is a prerequisite for the long exposures that a large collecting area makes possible. Instruments and mirror are thus not independent subsystems but mutually enabling components.

## 8. Conclusion

The James Webb Space Telescope launched on 25 December 2021 aboard an Ariane 5 from Kourou, French Guiana, and operates in a solar orbit at the second Lagrange point, approximately 1.5 million kilometers from Earth ([NASA, n.d.](https://science.nasa.gov/mission/webb/); [Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope)). Its primary mirror is a 6.5 m gold-coated beryllium reflector with a collecting area of 25.4 m², and it observes from long-wavelength visible light through mid-infrared, covering 0.6–28.5 µm ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope)). Its four science instruments are NIRCam, NIRSpec, MIRI, and FGS/NIRISS ([Wikipedia contributors, 2026](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope)).

The evidence supports a coherent picture: a large segmented gold-coated mirror, a distant equilibrium-point orbit, an infrared band extending well beyond the visible, and a four-instrument payload together constitute a single design logic in which the observing wavelength dictates the orbit, the aperture, and the coating. The principal gap in this report is instrument-level detail, which neither retrieved source supplies. A complete technical evaluation of Webb would require primary documentation specifying each instrument's wavelength coverage, detector characteristics, and observing modes — material that falls outside the evidence base used here and is therefore not asserted.

## References

NASA. (n.d.). *James Webb Space Telescope*. NASA Science. Retrieved September 14, 2026, from https://science.nasa.gov/mission/webb/

Wikipedia contributors. (2026). *James Webb Space Telescope*. Wikipedia. Retrieved September 14, 2026, from https://en.wikipedia.org/wiki/James_Webb_Space_Telescope