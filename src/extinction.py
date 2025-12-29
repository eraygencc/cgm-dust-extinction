def extinction_contribution(
    angular_sep,
    redshift_lens,
    redshift_source,
    A0,
    R200_kpc,
    alpha=-0.8,
):
    """
    Compute dust extinction from a single lens galaxy
    to background source galaxies.

    Parameters
    ----------
    angular_sep : array-like
        Angular separation between lens and sources (radians).
    redshift_lens : float
        Redshift of the lens galaxy.
    redshift_source : array-like
        Redshifts of the source galaxies.
    A0 : float
        Extinction normalization.
    R200_kpc : float
        Virial radius of the lens halo.
    alpha : float
        Power-law slope of extinction profile.

    Returns
    -------
    extinction : array-like
        Extinction contribution in magnitudes.

    Notes
    -----
    - Only sources behind the lens contribute (z_lens < z_source)
    - Uses angular diameter distance to convert angles to physical radii
    """
    d_ang = (
        COSMOLOGY.angular_diameter_distance(redshift_lens).to(u.kpc).value
    )

    impact_radius = 0.91 * R200_kpc
    physical_sep = angular_sep * d_ang

    extinction = np.where(
        redshift_lens < redshift_source,
        A0 * (physical_sep / impact_radius) ** alpha,
        0.0,
    )

    return np.nan_to_num(extinction, nan=0.0, posinf=0.0, neginf=0.0)
