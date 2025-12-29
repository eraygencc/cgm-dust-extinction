import numpy as np
from scipy.spatial import cKDTree

from .dust_models import dust_mass_from_stellar_mass, extinction_amplitude
from .extinction import extinction_contribution

def compute_extinction_per_source(
    lens_catalog,
    source_catalog,
    angular_diameter_distance,
    r200,
    alpha=-0.8,
):
    """
    Sum CGM dust extinction from all foreground lenses for each source.
    """
    tree = cKDTree(np.column_stack((source_catalog["ra"], source_catalog["dec"])))

    dust_mass = dust_mass_from_stellar_mass(lens_catalog["log_m_star"])
    A0 = extinction_amplitude(dust_mass, r200)

    indices = tree.query_ball_point(
        np.column_stack((lens_catalog["ra"], lens_catalog["dec"])),
        lens_catalog["theta_max"],
    )

    extinction = np.zeros(len(source_catalog), dtype=np.float32)

    for i, src_idx in enumerate(indices):
        sep = lens_catalog["separation"][i]
        contrib = extinction_contribution(sep, A0[i], alpha)
        np.add.at(extinction, src_idx, contrib)

    return extinction
