# CGM Dust Extinction

This repository provides a physically motivated forward model to compute
**circumgalactic dust extinction** for galaxies in cosmological
catalogs.

The implementation combines:
- Stellar-to-dust mass scaling from **Peek et al. (2015)**
- Radial extinction profile from **Ménard et al. (2010)**

The code is so designed that it can be applied to any
galaxy catalog providing sky positions, redshifts, and halo/stellar masses.

---

## Scientific Motivation

Dust in the circumgalactic medium (CGM) causes measurable extinction of
background sources. This effect biases:
- galaxy magnitudes
- color-based selections
- lensing magnification measurements

This repository computes the **total extinction per source galaxy** by
summing contributions from all foreground lenses within a physically
motivated radius.



## Model Assumptions and Physical Framework

This repository implements a **phenomenological model** for circumgalactic dust extinction.  
The goal is not to provide a full hydrodynamical treatment, but to capture the **observationally motivated effects** in a form that is efficient, interpretable, and suitable for large cosmological catalogs.

The main assumptions are summarized below.

---

### 1. Dust Mass Assignment

The dust mass is assumed to scale with stellar mass as:
$$
M_\mathrm{dust} \propto M_*^\beta
$$
with \beta = 0.4. It should be noted that we choose the upper range of the relation of Peek et al.(2015).

---

### 2. Halo Geometry

- Each galaxy resides in a spherical dark matter halo defined by the **$R_{200c}$** virial radius.
- The virial radius is computed using a standard spherical overdensity definition with respect to the critical density.
- The dust distribution is assumed to extend out to the virial radius.

---

### 3. Radial Extinction Profile

- The extinction profile follows a power law:

$$
A(r) = A_0 \left( \frac{r}{r_\mathrm{eff}} \right)^{\alpha}
$$

where:
- $\alpha = -0.8$
- $r_\mathrm{eff} = R_{200}$

The amplitude $A_0$ is computed by normalizing the profile to the total dust
mass within $R_{200}$.

- The fiducial slope is motivated by **Ménard et al. (2010)**: observational constraints from quasar reddening measurements.

---

### 4. Line-of-Sight Geometry

- Only **foreground galaxies** contribute to extinction:
  
  $$
  z_\mathrm{lens} < z_\mathrm{source}
  $$

- Sources at lower redshift than the lens receive zero extinction contribution.
- Angular separations are converted to physical distances using the angular diameter distance.

---

### 5. Superposition Principle

- The total extinction affecting a source galaxy is computed as the **sum of contributions from all foreground lenses** within a redshift-dependent angular search radius.
- This assumes that extinction contributions add linearly in magnitude space, which is valid in the low-optical-depth regime considered here.

---

### 6. Computational Considerations

- Spatial neighbour searches are performed using **KDTree-based radius queries** to avoid $\mathcal{O}(N^2)$ scaling.
- The implementation is optimized for:
  - Large catalogs
  - Vectorized numerical operations
  - Memory efficiency in high-performance computing environments

---

### Scope and Limitations

- The model does **not** include:
  - Dust clumpiness or anisotropy
  - Dust grain composition
  - Time evolution of dust properties
- These simplifications are intentional and reflect a trade-off between physical realism and computational scalability.

Despite these assumptions, the model captures the leading-order effects relevant for **statistical studies of dust extinction in cosmological surveys**.


---

## Repository Structure

```

cgm_dust_extinction/
│
├── README.md
├── requirements.txt
│
├── src/
│   ├── __init__.py
│   ├── cosmology.py          # cosmology & distance utilities
│   ├── dust_models.py        # Peek+15, Menard+10 models
│   ├── geometry.py           # projected separations, KDTree utilities (nearest neighbour algorithm)
│   ├── extinction.py         # dust extinction for lens–source pairs
│   └── pipeline.py           # main loop: sum extinction per source
│
│
└── LICENSE
```

---

## Required Catalog Columns

The input catalog must provide at least:

- Right ascension [deg]
- Declination [deg]
- Redshift
- Stellar mass 
- Halo mass 

---

## Performance Notes

- Uses **KDTree-based neighbor search**
- Vectorized extinction evaluation
- Designed for **HPC environments**
- Chunked redshift processing to limit memory usage

---

## References

- Peek et al. 2015, *ApJ*, 813, 7
- Ménard et al. 2010, *MNRAS*, 405, 1025



