"""
cgm_dust_extinction package

This module provides tools to simulate and apply circumgalactic dust extinction effects
to galaxy magnitudes based on lens-source geometry, halo and stellar masses.

Includes:
- Dust extinction simulation per lens galaxy.
- Total extinction calculation per source.
- Extinction addition to galaxy magnitudes.
"""

__version__ = "0.1.0"

# Core functionality import
from .extinction_simulator import DustExtinctionSimulator
from .extinction_summer import TotalExtinctionSummer
from .magnitude_extender import MagnitudeExtender

__all__ = [
    "DustExtinctionSimulator",
    "TotalExtinctionSummer",
    "MagnitudeExtender",
]
