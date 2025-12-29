# CGM Dust Extinction

This repository provides a physically motivated forward model to compute
**circumgalactic dust extinction** for galaxies in cosmological
catalogs.

The implementation combines:
- Stellar-to-dust mass scaling from **Peek et al. (2015)**
- Radial extinction profile from **Ménard et al. (2010)**

The code is designed so that it can be applied to any
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

---

## Physical Model

### Dust Mass Scaling (Peek et al. 2015)

The dust mass is assumed to scale with stellar mass as:

$$
M_\mathrm{dust} \propto M_*^{\beta}
$$

with default parameter:
- $\beta = 0.4$
We choose the upper range of the relation of Peek et al.(2015).

---

### Extinction Profile (Ménard et al. 2010)

The extinction profile follows a power law:

$$
A(r) = A_0 \left( \frac{r}{r_\mathrm{eff}} \right)^{\alpha}
$$

where:
- $\alpha = -0.8$
- $r_\mathrm{eff} = 0.91 \times R_{200}$

The amplitude $A_0$ is computed by normalizing the profile to the total dust
mass within $R_{200}$.

---

### Total Extinction per Source

For each source galaxy $s$, the total extinction is:

$$
A_s = \sum_{l \in \mathrm{foreground}} A_l(r_{ls})
$$

where $r_{ls}$ is the projected separation between lens $l$ and source $s$.

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



