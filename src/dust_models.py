import numpy as np

def dust_mass_from_stellar_mass(log_m_star, A=2e3, beta=0.4):
    """
    Stellar-to-dust mass relation (Peek et al. 2015).
    """
    return A * (10**log_m_star)**beta


def extinction_amplitude(
    dust_mass,
    R200_kpc,
    r_min_kpc=10.0,
    alpha=0.8,
    K_V=3.217,
):
    """
    Compute the normalization of the CGM extinction profile.

    Parameters
    ----------
    dust_mass : float or array-like
        Total dust mass associated with the halo.
    R200_kpc : float or array-like
        Virial radius of the halo in kpc.
    r_min_kpc : float, optional
        Inner cutoff radius to avoid divergence.
    alpha : float, optional
        Power-law slope of the extinction profile.
    K_V : float, optional
        V-band extinction coefficient.

    Returns
    -------
    A0 : float or array-like
        Extinction normalization in magnitudes.

    Notes
    -----
    The extinction profile follows:

        A(r) ∝ r^{-α}

    with normalization fixed by integrating the dust mass
    over the halo volume.
    """
    r_eff_kpc = 0.91 * R200_kpc  # Empirical scaling from Ménard et al.
    r_max_kpc = R200_kpc

    # Convert to parsecs
    r_eff_pc = r_eff_kpc * 1e3
    r_min_pc = r_min_kpc * 1e3
    r_max_pc = r_max_kpc * 1e3

    integral = r_max_pc ** (2 - alpha) - r_min_pc ** (2 - alpha)

    prefactor = (2.5 * K_V * (2 - alpha)) / (2 * np.pi * np.log(10))

    return dust_mass * prefactor / (r_eff_pc ** alpha * integral)

