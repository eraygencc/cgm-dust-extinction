import numpy as np
from scipy.spatial import cKDTree

def build_kdtree(ra, dec):
    """
    Build a KDTree for fast spatial queries on the sky.

    Parameters
    ----------
    ra : array-like
        Right ascension values of objects (in degrees or arcminutes).
    dec : array-like
        Declination values of objects (same angular units as ra).

    Returns
    -------
    scipy.spatial.cKDTree
        KDTree object that enables fast nearest-neighbour
        and radius-based searches.

    Notes
    -----
    - Each object is represented as a point in 2D angular space.
    - KDTree allows efficient queries such as:
        * find nearest neighbour
        * find all neighbours within a given angular radius
    - This avoids expensive O(N^2) pairwise distance computations.
    """
    coordinates = np.column_stack((ra, dec))
    return cKDTree(coordinates)



def angular_separation(ra1, dec1, ra2, dec2):
    """
    Compute the angular separation between two points on the sky
    using the small-angle approximation.

    Parameters
    ----------
    ra1, dec1 : float or array-like
        Coordinates of the first object(s).
    ra2, dec2 : float or array-like
        Coordinates of the second object(s).

    Returns
    -------
    separation : float or array-like
        Angular separation between the two points
        in the same units as the input coordinates.

    Notes
    -----
    - This function assumes small angular separations,
      where the Euclidean approximation is valid.
    - Suitable for arcminute-scale separations typically
      used in CGM dust extinction and lensing analyses.
    - For large angular separations, a full spherical
      distance formula should be used instead.
    """
    delta_ra = ra2 - ra1
    delta_dec = dec2 - dec1

    separation = np.sqrt(delta_ra**2 + delta_dec**2)
    return separation

