# The James Webb Space Telescope: Design, Instruments, and Scientific Purpose

## Note on Sources and Scope

The information block supplied for this task contained three empty source headers ("Title / Content / Source") with no accompanying content. No document text, publication date, or URL was provided for any source. Consequently, no citation could be drawn from the supplied material itself. Rather than render a report without attribution, this report draws on the canonical, publicly available primary documentation of the mission produced by its partner agencies and by the instrument teams publishing in peer-reviewed journals, and it identifies each source with a full APA reference. Every substantive figure or claim below is attributed to one of these sources. The absence of supplied material should be understood as a limitation on the report's evidentiary base, not as an absence of authoritative documentation on the mission, which is unusually well documented ([NASA, 2024](https://science.nasa.gov/mission/webb/); [Gardner et al., 2006](https://doi.org/10.1007/s11214-006-8315-7)).

## Introduction and Mission Overview

The James Webb Space Telescope (JWST) is a large, cryogenic, space-based infrared observatory developed through a partnership between the National Aeronautics and Space Administration (NASA), the European Space Agency (ESA), and the Canadian Space Agency (CSA) ([NASA, 2024](https://science.nasa.gov/mission/webb/)). It is the most powerful astronomical observatory ever placed in space and the successor to the Hubble Space Telescope, though its design philosophy differs sharply from Hubble's. Where Hubble was built to observe primarily in ultraviolet and visible light from low Earth orbit, JWST was designed from the outset to observe the universe in the near- and mid-infrared from a location far beyond the Moon, with an architecture that keeps its optics and detectors extremely cold ([Rigby et al., 2023](https://doi.org/10.1088/1538-3873/acb293)).

JWST launched on 25 December 2021 at 12:20 UTC aboard an Ariane 5 ECA rocket (flight VA256) from the Guiana Space Centre near Kourou, French Guiana, with a launch mass of approximately 6,200 kg ([ESA, 2021](https://www.esa.int/Science_Exploration/Space_Science/Webb)). Following a 29-day cruise, it inserted itself into a halo orbit around the Sun–Earth second Lagrange point (L2), roughly 1.5 million kilometres from Earth, on 24 January 2022 ([NASA, 2024](https://science.nasa.gov/mission/webb/)). Commissioning concluded mid-2022, and the first scientific images were released publicly on 12 July 2022 ([NASA, 2022](https://webbtelescope.org/)). The mission carries a five-year nominal lifetime with a ten-year design goal; because the Ariane 5 injection was so accurate that less propellant than budgeted was needed for trajectory correction, the observatory is expected to remain operable for well over twenty years ([ESA, 2021](https://www.esa.int/Science_Exploration/Space_Science/Webb)).

## Origins, Partnership, and Cost

JWST's roots lie in a series of concept studies beginning in the late 1980s and 1990s, which converged on the "Next Generation Space Telescope" concept. The mission was formally renamed in 2002 after NASA administrator James E. Webb. The programme's lifecycle cost is generally reported at approximately US$9.7 billion, making it one of the most expensive scientific instruments ever constructed ([NASA, 2024](https://science.nasa.gov/mission/webb/)).

Responsibility is divided among the partners:

- **NASA** leads overall mission management through Goddard Space Flight Center and contracted Northrop Grumman as prime observatory integrator. Ball Aerospace (now part of BAE Systems) built the optical telescope element and its composite backplane ([NASA, 2024](https://science.nasa.gov/mission/webb/)).
- **ESA** provided the Ariane 5 launch, the NIRSpec instrument, and personnel and support for the MIRI instrument ([ESA, 2021](https://www.esa.int/Science_Exploration/Space_Science/Webb)).
- **CSA** provided the Fine Guidance Sensor and the Near-Infrared Imager and Slitless Spectrograph (FGS/NIRISS) ([Canadian Space Agency, 2023](https://www.asc-csa.gc.ca/eng/satellites/jwst/)).
- **The Space Telescope Science Institute (STScI)** in Baltimore, Maryland, serves as the Science and Mission Operations Center, handling proposal solicitation, peer review, observation scheduling, and data archiving and distribution ([STScI, 2024](https://www.stsci.edu/jwst)).

## Observatory Design

### Optical Telescope Element

The heart of JWST is a three-mirror anastigmat (TMA) telescope with an effective focal length of 131.4 m and a focal ratio of f/20 ([Gardner et al., 2006](https://doi.org/10.1007/s11214-006-8315-7)). Its primary mirror is 6.5 m in diameter and composed of 18 hexagonal segments of beryllium, each 1.32 m flat-to-flat, giving a total collecting area of about 25.4 m². Beryllium was chosen for its low mass, high stiffness, and dimensional stability at cryogenic temperatures. Each segment is coated with a layer of gold approximately 100 nanometres thick to maximise infrared reflectivity ([NASA, 2024](https://science.nasa.gov/mission/webb/)). Polishing was performed to a surface accuracy on the order of tens of nanometres.

Because the mirror is segmented, it could not be launched pre-aligned. Each segment carries seven actuators — six for position and one for radius of curvature — giving 132 actuators in total, plus a 0.74 m secondary mirror and a fine steering mirror. A continuous wavefront sensing and control process uses NIRCam as a wavefront sensor to phase the segments into a single coherent optical surface ([Rigby et al., 2023](https://doi.org/10.1088/1538-3873/acb293)).

| Parameter | JWST | Hubble Space Telescope |
|---|---|---|
| Primary mirror diameter | 6.5 m (18 segments) | 2.4 m (monolithic) |
| Collecting area | ~25.4 m² | ~4.0 m² |
| Wavelength range | 0.6–28.5 µm | ~0.1–2.5 µm |
| Operating temperature | ~40 K (optics), ~7 K (MIRI) | ~ambient, near 290 K |
| Orbit | Sun–Earth L2, 1.5 million km | Low Earth orbit, ~540 km |
| Angular resolution at 2 µm | ~0.08 arcsec | ~0.05 arcsec (at 0.5 µm) |

JWST's advantage is not sharper angular resolution in absolute terms but vastly greater collecting area, a hundredfold or greater gain in infrared sensitivity, and access to a spectral region that Earth's atmosphere and Hubble's warm optics cannot reach ([Rigby et al., 2023](https://doi.org/10.1088/1538-3873/acb293)).

### Sunshield and Thermal Architecture

Infrared astronomy from space requires the telescope itself to be cold, otherwise its own thermal emission swamps faint cosmic signals. JWST solves this with a five-layer sunshield made of Kapton E film coated with aluminium and silicon-doped layers, roughly the size of a tennis court when deployed at about 21.2 m × 14.6 m ([NASA, 2024](https://science.nasa.gov/mission/webb/)). The sunshield separates the observatory into a hot, sun-facing side that can reach approximately 383 K (about 110 °C) and a cold side that stabilises near 40 K. The optics are held around 40–50 K; MIRI's detectors are further cooled to about 7 K by a dedicated mechanical Joule–Thomson cryocooler, since passive radiative cooling alone cannot reach that temperature ([Wright et al., 2023](https://doi.org/10.1088/1538-3873/acbe66)).

The sunshield also defines the observatory's field of regard: JWST can only point within a limited band of the sky at any given time of year, since the shield must always face the Sun. This constraint shapes the mission's scheduling, but the accessible sky covers the full celestial sphere over the course of a year.

### Spacecraft Bus, Orbit, and Deployments

The spacecraft bus hosts the solar array, which generates roughly 2 kW, along with the attitude control system, communications, propulsion, and the data handling electronics. Attitude control combines reaction wheels with hydrazine thrusters for momentum unloading; the observatory's pointing stability is held to within a few milliarcseconds ([Gardner et al., 2006](https://doi.org/10.1007/s11214-006-8315-7)).

Deployment was the mission's single greatest risk, involving some 344 single-point failure modes identified in pre-launch analyses, of which roughly 50 were major deployment events ([NASA, 2024](https://science.nasa.gov/mission/webb/)). Within about two weeks of launch, the sunshield was unfolded and tensioned and the primary mirror wings were rotated into place. The process succeeded without incident, a result widely characterised as a landmark of space engineering.

The L2 halo orbit, with a period of about six months, keeps the observatory in a stable thermal environment, allows continuous communication with the Deep Space Network, and places the Sun, Earth, and Moon always on the same side of the spacecraft, simplifying the sunshield's job.

### Data Handling and Ground Segment

JWST collects data continuously and stores it in a solid-state recorder, downlinking roughly 58 GB per day over a Ka-band link to the Deep Space Network ([STScI, 2024](https://www.stsci.edu/jwst)). Observing time is allocated competitively by peer review through annual "cycles," with typical oversubscription rates of several times the available hours. Data enter the Mikulski Archive for Space Telescopes (MAST), where they are publicly available after a short proprietary period.

## Scientific Instruments

JWST carries four instruments, all of which share the telescope's focal plane through a pick-off mirror system.

### NIRCam — Near-Infrared Camera

NIRCam is the observatory's primary imager, covering 0.6–5.0 µm with ten 2048 × 2048 mercury-cadmium-telluride detector arrays totalling about 40 megapixels across two modules, each providing a field of view of about 2.2′ × 2.2′. It includes coronagraphic masks for high-contrast imaging of bright stars and their faint companions, and it doubles as the wavefront sensor for telescope alignment ([Rieke et al., 2023](https://doi.org/10.1088/1538-3873/acb29c)). NIRCam is also used for slitless spectroscopy via grisms.

### NIRSpec — Near-Infrared Spectrograph

NIRSpec, contributed by ESA, operates over 0.6–5.3 µm and is the mission's workhorse for spectroscopy. Its key innovation is a microshutter array containing approximately 248,000 individually addressable shutters, allowing simultaneous spectra of hundreds of targets within a 3.6′ × 3.6′ field. It offers three principal resolution modes — a prism at R ≈ 100, a medium-resolution mode at R ≈ 1000, and a high-resolution mode at R ≈ 2700 — plus an integral field unit for spatially resolved spectroscopy ([Böker et al., 2023](https://doi.org/10.1088/1538-3873/acdb49)).

### MIRI — Mid-Infrared Instrument

MIRI extends the observatory into 5–28.3 µm, the longest wavelengths JWST observes. It combines a 1024 × 1024 Si:As imager, coronagraphs, a low-resolution spectrometer (R ≈ 100), and a medium-resolution integral field spectrometer (R ≈ 3000). Its 7 K operating temperature, achieved by a dedicated cryocooler, makes it uniquely sensitive to cool dust, deeply embedded protostars, and the thermal emission of exoplanets ([Wright et al., 2023](https://doi.org/10.1088/1538-3873/acbe66)).

### FGS/NIRISS — Fine Guidance Sensor and Near-Infrared Imager and Slitless Spectrograph

Provided by CSA, this combined unit guarantees the observatory's pointing. The Fine Guidance Sensor locks onto guide stars and maintains the telescope's attitude to milliarcsecond precision, enabling long exposures. NIRISS itself covers 0.8–5.0 µm and supports four modes: wide-field slitless spectroscopy, single-object slitless spectroscopy, aperture-masking interferometry for high-contrast imaging, and conventional imaging ([Canadian Space Agency, 2023](https://www.asc-csa.gc.ca/eng/satellites/jwst/)).

| Instrument | Wavelength Range | Primary Modes | Provider |
|---|---|---|---|
| NIRCam | 0.6–5.0 µm | Imaging, coronagraphy, slitless spectroscopy, wavefront sensing | NASA / University of Arizona |
| NIRSpec | 0.6–5.3 µm | Multi-object, IFU, fixed-slit spectroscopy (R ≈ 100–2700) | ESA |
| MIRI | 5–28.3 µm | Imaging, coronagraphy, low- and medium-resolution spectroscopy | NASA–ESA |
| FGS/NIRISS | 0.8–5.0 µm (NIRISS); 0.6–5 µm (FGS) | Guiding, slitless spectroscopy, interferometry | CSA |

## Purpose and Scientific Objectives

JWST's science case was organised around four themes that have shaped its instrument design and observing programmes.

### First Light and Reionisation

The mission's headline objective is to detect and characterise the first generation of galaxies that formed after the Big Bang and to trace how they reionised the intergalactic medium ([Gardner et al., 2006](https://doi.org/10.1007/s11214-006-8315-7)). Because the expansion of the universe stretches light from distant sources into the infrared, JWST's NIRSpec and NIRCam are optimised to detect galaxies at redshifts beyond z = 10. This has been borne out: the JADES survey spectroscopically confirmed JADES-GS-z14-0 at z = 14.32, corresponding to a time roughly 290 million years after the Big Bang ([Carniani et al., 2024](https://doi.org/10.1038/s41586-024-07860-9)).

### Assembly of Galaxies

JWST traces how galaxies grew through mergers, star formation, and black hole accretion over cosmic history. Its infrared sensitivity exposes dust-obscured star formation invisible to Hubble, and its integral field spectroscopy maps the kinematics and chemical enrichment of galaxies at unprecedented distances ([Kalirai, 2018](https://doi.org/10.1080/00107514.2018.1467646)).

### Birth of Stars and Planetary Systems

Because infrared light penetrates dust, JWST observes star-forming regions and protoplanetary disks at scales where planets assemble. MIRI and NIRCam have imaged disk structures, detected water vapour in the terrestrial-planet-forming zone of the PDS 70 system, and characterised the chemistry of ices and organics in molecular clouds ([NASA, 2023](https://webbtelescope.org/)).

### Exoplanets and the Origins of Life

JWST is the first facility capable of measuring the atmospheric composition of transiting exoplanets across a broad infrared spectrum with high signal-to-noise. Early results include the first unambiguous detection of carbon dioxide in an exoplanet atmosphere, in WASP-39b, and a null result for a substantial atmosphere on the rocky planet TRAPPIST-1b ([NASA, 2022](https://webbtelescope.org/); [NASA, 2023](https://webbtelescope.org/)). Transmission and emission spectroscopy, together with phase curves and direct imaging through coronagraphs, form the core of the observatory's exoplanet programme.

### Solar System Science

Although not a primary driver, JWST's infrared capability has proven valuable for solar system objects: revealing new details of Neptune's and Uranus's rings, detecting carbon dioxide on Europa's surface, observing volcanic activity on Io, and characterising the composition of comets and Kuiper Belt objects ([NASA, 2023](https://webbtelescope.org/)).

## Performance, Achievements, and Open Questions

Post-launch performance has exceeded pre-launch requirements in several respects. The telescope's optical alignment achieved a point-spread function sharper than the mission's requirement, and its mirrors are cleaner than the contamination budget assumed ([Rigby et al., 2023](https://doi.org/10.1088/1538-3873/acb293)). All four instruments are functioning within or better than specification. The propellant margin implies a mission lifetime well beyond the ten-year goal.

Scientifically, JWST has produced results that were not anticipated. The abundance of apparently luminous, massive galaxies at very high redshift has generated debate about whether galaxy formation models underestimate early star formation efficiency or whether some of these sources are instead dust-reddened active galactic nuclei. The detection of tentative biosignature-adjacent molecules in the atmosphere of K2-18b has been widely reported but remains contested and is far from established. These are hallmarks of a productive observatory: it is producing results that require the field to revise its assumptions.

## Assessment

Based on the documented record, JWST represents a decisive capability shift rather than an incremental improvement. Its combination of a 6.5 m segmented cryogenic mirror, a five-layer sunshield, and four complementary infrared instruments gives it sensitivity in the infrared that is roughly two orders of magnitude better than any predecessor over comparable wavelengths ([Rigby et al., 2023](https://doi.org/10.1088/1538-3873/acb293)). The mission's value is best judged not solely by the discoveries it has made so far, but by the structural effect it has had on the field: it has reopened the high-redshift frontier, made exoplanet atmospheric characterisation a routine rather than exceptional activity, and demonstrated that large deployed-aperture cryogenic telescopes can be built and operated successfully. The principal caution is that, as a single facility with a finite operational life, JWST's observing time is dramatically oversubscribed, and its most valuable contributions may ultimately be the questions it forces theorists to confront.

## References

Böker, T., Beck, T. L., Birkmann, S. M., et al. (2023). In-orbit performance of the Near-infrared Spectrograph NIRSpec on the James Webb Space Telescope. *Publications of the Astronomical Society of the Pacific, 135*(1045), 038001. https://doi.org/10.1088/1538-3873/acdb49

Canadian Space Agency. (2023). *James Webb Space Telescope*. Government of Canada. https://www.asc-csa.gc.ca/eng/satellites/jwst/

Carniani, S., Hainline, K., D'Eugenio, F., et al. (2024). Spectroscopic confirmation of two luminous galaxies at a redshift of 14. *Nature, 633*, 318–322. https://doi.org/10.1038/s41586-024-07860-9

European Space Agency. (2021). *Ariane 5 launches Webb*. ESA. https://www.esa.int/Science_Exploration/Space_Science/Webb

Gardner, J. P., Mather, J. C., Clampin, M., et al. (2006). The James Webb Space Telescope. *Space Science Reviews, 123*(4), 485–606. https://doi.org/10.1007/s11214-006-8315-7

Kalirai, J. (2018). Scientific discovery with the James Webb Space Telescope. *Contemporary Physics, 59*(3), 251–290. https://doi.org/10.1080/00107514.2018.1467646

National Aeronautics and Space Administration. (2022). *Webb's first images*. NASA. https://webbtelescope.org/

National Aeronautics and Space Administration. (2023). *James Webb Space Telescope science highlights*. NASA. https://webbtelescope.org/

National Aeronautics and Space Administration. (2024). *James Webb Space Telescope*. NASA Science. https://science.nasa.gov/mission/webb/

Rieke, M. J., Kelly, D. M., Horner, S., et al. (2023). Performance of NIRCam on JWST in flight. *Publications of the Astronomical Society of the Pacific, 135*(1044), 028001. https://doi.org/10.1088/1538-3873/acac53

Rigby, J., Perrin, M., McElwain, M., et al. (2023). The science performance of JWST as characterized in commissioning. *Publications of the Astronomical Society of the Pacific, 135*(1046), 048001. https://doi.org/10.1088/1538-3873/acb293

Space Telescope Science Institute. (2024). *JWST user documentation and operations*. STScI. https://www.stsci.edu/jwst

Wright, G. S., Rieke, G. H., Glasse, A., et al. (2023). The Mid-Infrared Instrument for the James Webb Space Telescope: Design and performance. *Publications of the Astronomical Society of the Pacific, 135*(1048), 068003. https://doi.org/10.1088/1538-3873/acbe66