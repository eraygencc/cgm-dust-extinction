import numpy as np

def dust_mass_from_stellar_mass(log_m_star, A=2e3, beta=0.4):
    """
    Stellar-to-dust mass relation (Peek et al. 2015).
    """
    return A * (10**log_m_star)**beta


def extinction_amplitude(
    dust_mass,
    r200_kpc,
    alpha=-0.8,
    k_v=3.217, #We choose SMC type dust in accordance with Ménard et al. (2010)
    rmin_kpc=10.0, 
):
    """
    Compute extinction profile normalization following Ménard et al. (2010).
    """
    r_eff = 0.91 * r200_kpc

    rmin_pc = rmin_kpc * 1e3
    rmax_pc = r200_kpc * 1e3
    r_eff_pc = r_eff * 1e3

    integral = rmax_pc**(2 - alpha) - rmin_pc**(2 - alpha)
    prefactor = (2.5 * k_v * (2 - alpha)) / (2 * np.pi * np.log(10))

    return dust_mass * prefactor / (r_eff_pc**alpha * integral)
