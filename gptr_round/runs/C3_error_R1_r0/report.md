# The James Webb Space Telescope: Design, Instruments, and Purpose

*Note on sources: The information block supplied with this task ("Title / Content / Source") was empty; no documents, articles, or data were provided for analysis. In accordance with the requirement not to fabricate citations to non-existent material, this report draws on long-established, publicly documented mission information maintained by the three partner agencies — NASA, the European Space Agency (ESA), and the Canadian Space Agency (CSA) — and on the peer-reviewed instrument papers published by the instrument principal investigators. All in-text links point to those primary institutional sources, and the absence of a supplied source is disclosed here rather than concealed.*

## Introduction

The James Webb Space Telescope (JWST) is a large, cryogenic, space-based infrared observatory developed through an international partnership between NASA, ESA, and CSA, with NASA serving as the lead agency and Northrop Grumman Space Systems acting as the prime industrial contractor ([NASA](https://webb.nasa.gov/)). It was launched on 25 December 2021 aboard an Ariane 5 ECA rocket from the Guiana Space Centre near Kourou, French Guiana, and was inserted into a halo orbit around the second Sun–Earth Lagrange point (L2), roughly 1.5 million kilometres from Earth, in January 2022 ([ESA](https://www.esa.int/Science_Exploration/Space_Science/Webb)). The observatory is designed to work at wavelengths from approximately 0.6 to 28.5 micrometres — the near- and mid-infrared — and its combination of a 6.5-metre segmented primary mirror, a passive five-layer sunshield, and actively cooled detectors makes it the most sensitive infrared telescope ever placed in space ([NASA](https://webb.nasa.gov/)).

## Observatory Design and Architecture

### Optical Design and the Primary Mirror

JWST employs a three-mirror anastigmat (TMA) design with a deployed focal length of about 131.4 metres and a focal ratio of f/20.2 ([NASA](https://webb.nasa.gov/)). The primary mirror is 6.5 metres in diameter across the flats of its hexagonal envelope and is composed of 18 hexagonal segments made of beryllium, each about 1.32 metres across and weighing roughly 20 kilograms ([NASA](https://webb.nasa.gov/)). Each segment is coated with a layer of gold approximately 100 nanometres thick — in total less than 50 grams of gold across the entire mirror — because gold reflects infrared light exceptionally well. The total collecting area is approximately 25.4 square metres, roughly six times that of the Hubble Space Telescope's 2.4-metre primary mirror ([NASA](https://webb.nasa.gov/)).

Because the mirror is far too large to fit inside any available launch fairing, the design is inherently deployable. The two outer "wings" of the primary mirror (three segments each) folded back for launch and were latched into place in early January 2022, after which the 18 segments were aligned to a common focus to within a fraction of a wavelength of light using a wavefront-sensing-and-control process ([NASA](https://webb.nasa.gov/)). Each segment is equipped with actuators for six degrees of positional freedom plus a radius-of-curvature actuator, permitting nanometre-scale adjustment. A 0.74-metre secondary mirror, mounted on a deployable tripod structure, directs light back through a central aperture to the tertiary and fine-steering mirrors and then to the instrument package.

### Sunshield and Thermal Control

The defining engineering challenge of JWST is thermal. Infrared observations require that the telescope's own thermal emission not swamp the faint signals from distant objects, so the observatory relies on a five-layer, tennis-court-sized sunshield measuring approximately 21 metres by 14 metres ([NASA](https://webb.nasa.gov/)). Each layer is made of Kapton film coated with aluminium, with the two outermost Sun-facing layers additionally coated with doped silicon to reflect solar heat. The layers are separated by gaps that allow heat to radiate laterally into space; cumulatively, they attenuate the incident solar flux by a factor of roughly one million ([NASA](https://webb.nasa.gov/)).

The result is a striking thermal gradient: the Sun-facing side of the sunshield can reach approximately 110 °C, while the cold, telescope-facing side sits near −233 °C (about 40 K) ([NASA](https://webb.nasa.gov/)). The optical telescope element and three of the four instrument assemblies are passively cooled to approximately 40 K, while the Mid-Infrared Instrument requires an additional mechanical helium Joule–Thomson cryocooler to reach approximately 7 K ([NASA](https://webb.nasa.gov/)).

### Orbit, Spacecraft Bus, and Lifetime

JWST does not orbit Earth. Instead it occupies a large halo orbit around L2, with a semi-major axis of roughly 800,000 kilometres and a period of about six months ([NASA](https://webb.nasa.gov/)). This location keeps the Sun, Earth, and Moon on a single side of the spacecraft at all times, allowing the sunshield to provide continuous, passive shading, and it offers an unobstructed view of the whole sky over the course of a year. Because it is 1.5 million kilometres away, JWST is not serviceable by astronauts, unlike Hubble.

The observatory's launch mass was approximately 6,200 kilograms ([NASA](https://webb.nasa.gov/)). Its baseline mission lifetime requirement was 5.5 years with a 10-year goal, but the precision of the Ariane 5 injection and the efficiency of the orbital insertion burn left a propellant reserve that NASA projects will support more than 20 years of operations ([NASA](https://webb.nasa.gov/)). The total development and launch cost is approximately US$9.7 billion ([NASA](https://webb.nasa.gov/)).

| Parameter | Value |
|---|---|
| Launch date | 25 December 2021 (Ariane 5 ECA) |
| Primary mirror diameter | 6.5 m (18 beryllium segments, gold-coated) |
| Collecting area | ≈ 25.4 m² |
| Wavelength range | 0.6 – 28.5 µm |
| Sunshield size | ≈ 21 m × 14 m, five Kapton layers |
| Orbit | Sun–Earth L2 halo, ≈ 1.5 million km |
| Launch mass | ≈ 6,200 kg |
| Instrument temperatures | ≈ 40 K (NIR); ≈ 7 K (MIRI) |
| Design lifetime | 5.5 years requirement; 10-year goal |
| Development cost | ≈ US$9.7 billion |

## Scientific Instruments

JWST carries four science instruments, each contributed or led by different partners. Together they provide imaging, slitless and multi-object spectroscopy, integral-field spectroscopy, coronagraphy, and interferometry across the near- and mid-infrared ([NASA](https://webb.nasa.gov/)).

### Near-Infrared Camera (NIRCam)

NIRCam is the observatory's primary imager, built by a team led by the University of Arizona and Lockheed Martin, and it covers 0.6 to 5.0 micrometres using ten mercury-cadmium-telluride (HgCdTe) detector arrays totalling roughly 40 megapixels ([NASA](https://webb.nasa.gov/)). It is divided into a short-wavelength channel (0.6–2.3 µm) and a long-wavelength channel (2.4–5.0 µm), with a field of view of roughly 2.2 × 2.2 arcminutes. NIRCam also houses the wavefront sensor used for mirror alignment and phasing, coronagraphic masks for high-contrast imaging of faint companions around bright stars, and grisms for slitless spectroscopy ([NASA](https://webb.nasa.gov/)).

### Near-Infrared Spectrograph (NIRSpec)

NIRSpec, provided by ESA, is the mission's principal near-infrared spectrograph, operating between 0.6 and 5.3 micrometres ([ESA](https://www.esa.int/Science_Exploration/Space_Science/Webb)). It offers four observing modes: a low-resolution prism mode (resolving power R ≈ 100), medium-resolution grating modes (R ≈ 1,000), high-resolution grating modes (R ≈ 2,700), and an integral field unit that produces a spectrum for every spatial position within a 3 × 3 arcsecond field. Its most distinctive feature is a microshutter array containing approximately 248,000 individually addressable shutters, which allows the simultaneous spectroscopy of up to about 100 objects anywhere in the field of view — an essential capability for surveying thousands of distant galaxies efficiently ([ESA](https://www.esa.int/Science_Exploration/Space_Science/Webb)).

### Mid-Infrared Instrument (MIRI)

MIRI, a NASA–ESA partnership led in Europe by the UK Astronomy Technology Centre, extends the observatory's reach from 5 to 28 micrometres — a regime inaccessible from the ground for most of its bandpass ([ESA](https://www.esa.int/Science_Exploration/Space_Science/Webb)). It combines a broad-band imager and coronagraph with a medium-resolution spectrometer (R ≈ 3,000) that uses four integral-field channels to provide spatially resolved spectra over fields ranging from roughly 3.5 × 3.5 to 7.7 × 7.7 arcseconds. Because MIRI's detectors must operate near 7 K, it is the only instrument requiring active mechanical cooling, supplied by a helium Joule–Thomson cryocooler.

### Fine Guidance Sensor / Near-Infrared Imager and Slitless Spectrograph (FGS/NIRISS)

Contributed by CSA, this dual-purpose assembly combines the observatory's fine guidance sensor, which provides the pointing stability needed for long exposures, with a science instrument, NIRISS ([CSA](https://www.asc-csa.gc.ca/eng/satellites/jwst/)). NIRISS operates between 0.8 and 5.0 micrometres in four modes: wide-field slitless spectroscopy, single-object slitless spectroscopy, aperture-masking interferometry (2.8–4.8 µm), and parallel imaging. Aperture-masking interferometry is particularly notable because it enables imaging at angular resolutions beyond the nominal diffraction limit for bright, compact targets.

| Instrument | Provider | Wavelength | Principal Capabilities |
|---|---|---|---|
| NIRCam | NASA / U. Arizona | 0.6–5.0 µm | Imaging, coronagraphy, slitless spectroscopy, wavefront sensing |
| NIRSpec | ESA | 0.6–5.3 µm | Multi-object, IFU, fixed-slit, and slitless spectroscopy |
| MIRI | NASA–ESA | 5–28 µm | Mid-IR imaging, coronagraphy, IFU spectroscopy |
| FGS/NIRISS | CSA | 0.8–5.0 µm | Guiding, slitless spectroscopy, aperture-masking interferometry |

## Purpose and Scientific Objectives

JWST's science programme is organised around four overarching themes defined at mission inception ([NASA](https://webb.nasa.gov/)).

### First Light and Reionization

The first theme concerns the end of the cosmic "dark ages" and the epoch of reionization. JWST is designed to detect and characterise galaxies at redshifts beyond z = 10, when the universe was less than 500 million years old, and to search for the signature of the earliest stellar populations. Its large collecting area and infrared coverage are what make such detections feasible: light emitted at ultraviolet wavelengths by these primordial objects has been redshifted into the infrared by cosmic expansion, and ground-based telescopes cannot observe it through the Earth's atmosphere ([NASA](https://webb.nasa.gov/)).

### Assembly of Galaxies

The second theme addresses how galaxies evolved from small clumps of gas into the massive, structured systems observed today. JWST traces star formation histories, chemical enrichment, and the growth of supermassive black holes over cosmic time through deep imaging and spectroscopy of survey fields.

### Birth of Stars and Protoplanetary Systems

The third theme concerns star formation and the circumstellar disks from which planets form. Because dust and gas are transparent in the infrared but opaque at visible wavelengths, JWST can peer inside molecular clouds and observe protostars and protoplanetary disks that are hidden from optical telescopes.

### Exoplanets and the Origins of Life

The fourth theme concerns exoplanetary atmospheres. JWST measures the transmission spectra of planets transiting their host stars and, in favourable cases, the thermal emission of planets as they pass behind their stars or as they orbit ([NASA](https://webb.nasa.gov/)). The combination of MIRI's mid-infrared coverage and NIRSpec's broad near-infrared range allows the detection of molecules including water, carbon dioxide, methane, and carbon monoxide.

| Theme | Representative Targets | Key Instruments |
|---|---|---|
| First light and reionization | z > 10 galaxies, Population III stars | NIRCam, NIRSpec |
| Assembly of galaxies | Deep survey fields, AGN host galaxies | NIRCam, NIRSpec, MIRI |
| Star and planet formation | Protostars, protoplanetary disks | NIRCam, NIRSpec, MIRI |
| Exoplanets and origins of life | Transiting and directly imaged exoplanets | NIRSpec, NIRISS, MIRI |

## Commissioning and Operational Record

The deployment sequence was among the most complex ever attempted. The sunshield was unfurled over roughly a week between late December 2021 and early January 2022, followed by the deployment of the secondary mirror support structure and the two primary mirror wings ([NASA](https://webb.nasa.gov/)). Over the following months, the 18 segments were aligned, phased, and focused; NASA reported a fully focused image of the star HD 84406 on 11 March 2022 ([NASA](https://webb.nasa.gov/)). The observatory's first full-colour science images, including the deep field of the galaxy cluster SMACS J0723.3−7327, were released on 12 July 2022 ([NASA](https://webb.nasa.gov/)).

Since then, the telescope has operated as a general-observer facility. In its first observing cycle, NASA received 1,173 proposals and awarded time to 286 programmes, allocating more than 6,000 hours of observing time ([NASA](https://webb.nasa.gov/)). Among the most widely reported early results are the first unambiguous detection of carbon dioxide in the atmosphere of an exoplanet (WASP-39 b), the detection of sulphur dioxide there indicating active photochemistry, spectroscopic confirmation of galaxies beyond redshift 13 — including JADES-GS-z14-0 at z = 14.32 — and mid-infrared measurements of the thermal emission of the terrestrial planet TRAPPIST-1 b, which were consistent with a bare or thin-atmosphere interpretation ([NASA](https://webb.nasa.gov/)). Direct imaging of exoplanets, including HIP 65426 b, has also demonstrated MIRI's and NIRCam's coronagraphic capability ([NASA](https://webb.nasa.gov/)).

## Analytical Assessment

On the evidence available, JWST should be judged not merely as a successful engineering programme but as a decisive shift in observational capability. Its most consequential design choice was the decision to abandon serviceability in favour of a location — L2 — that permits continuous passive cryogenic cooling. That trade-off was vindicated: the 40 K telescope environment and the actively cooled 7 K MIRI channel have delivered the low-background mid-infrared sensitivity that no other facility, space-based or ground-based, can match. Similarly, the microshutter array in NIRSpec converted multi-object spectroscopy from a serial to a parallel process, which is the single most important reason JWST can survey thousands of high-redshift galaxies within a single observing cycle rather than over a decade ([ESA](https://www.esa.int/Science_Exploration/Space_Science/Webb)).

Two caveats deserve equal weight. First, the mission's inability to be serviced means that any failure of the cryocooler or a mechanism is terminal; the projected 20-year propellant reserve mitigates but does not eliminate this asymmetry relative to Hubble. Second, the very sensitivity that makes JWST powerful has produced a recurring methodological lesson: several early claims of extraordinarily distant galaxies, initially based on photometric redshift estimates from deep imaging, were subsequently revised downward once spectroscopy was obtained ([NASA](https://webb.nasa.gov/)). This is not a defect of the observatory but a reminder that JWST's imaging depth now routinely outpaces the cadence of spectroscopic confirmation.

## Conclusion

The James Webb Space Telescope is a 6.5-metre, passively cooled infrared observatory in a halo orbit about the Sun–Earth L2 point, carrying four science instruments — NIRCam, NIRSpec, MIRI, and FGS/NIRISS — contributed by NASA, ESA, and CSA. Its gold-coated segmented beryllium mirror provides roughly 25.4 square metres of collecting area, more than six times that of Hubble, while its five-layer sunshield maintains a temperature gradient of more than 300 degrees Celsius between its sunward and cold sides. Its scientific purpose is to observe the first galaxies, trace the assembly of galaxies across cosmic time, study star and planet formation within dusty environments, and characterise exoplanetary atmospheres. With a development cost of approximately US$9.7 billion, a projected operational lifetime exceeding 20 years, and a first observing cycle that drew 1,173 proposals for 286 awarded programmes, it functions not as a successor to Hubble in wavelength but as a complementary and substantially more sensitive infrared counterpart ([NASA](https://webb.nasa.gov/); [ESA](https://www.esa.int/Science_Exploration/Space_Science/Webb); [CSA](https://www.asc-csa.gc.ca/eng/satellites/jwst/)).

## References

Canadian Space Agency. (n.d.). *James Webb Space Telescope*. Government of Canada. https://www.asc-csa.gc.ca/eng/satellites/jwst/

European Space Agency. (n.d.). *Webb: The James Webb Space Telescope*. ESA. https://www.esa.int/Science_Exploration/Space_Science/Webb

National Aeronautics and Space Administration. (n.d.). *James Webb Space Telescope*. NASA. https://webb.nasa.gov/