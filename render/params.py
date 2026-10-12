"""Rig dimensions for the 3D model (rev 33). One source of truth for the render assets.

All lengths in metres, z up, mast axis at the origin. Values come from DESIGN.md and the *_check.py scripts.
"""
from math import radians

# ---- mast
MAST_TOP = 108.0            # crown plate
MAST_FOOT = 1.0             # foot plate over the pivot
FACE = 1.4                  # triangular lattice face
CHORD_D, DIAG_D = 0.10, 0.04
PANEL = 0.75                # diagonal panel height
SECTION = 3.0               # flat-pack section length (Ti joint bands)

# ---- collars and bracing (fixed, do not turn)
STRUT_COLLAR, UPPER_COLLAR = 35.0, 62.0
COLLAR_R, COLLAR_H = 1.27, 0.35
FOOT_R = 30.0
FOOT_ANGLES = [radians(a) for a in (90, 210, 330)]   # bracing planes (math angle from +x)
STRUT_D, STRUT_SPREAD = 0.30, 1.5                  # A-frame tubes, spread at the collar
STAY_D, ROD_D = 0.010, 0.011                       # drawn diameters (6 mm stay drawn at 10 mm)
VLINK_OUT = 1.0
PAD = (1.2, 1.2, 0.3)

# ---- rotating top
YARD_Z, YARD_DEPTH, YARD_WIDTH, YARD_HALF = 100.0, 0.8, 0.5, 18.7
YARD_CHORD_D = 0.06
LIFT_TIP = 18.5
OUTRIGGER = 0.55
SPREADER_Z, SPREADER_HALF = 81.0, 6.0
DIAMOND_LOW = 64.0
CROWN_STAY_ARM = 0.95
POST_TOP = 109.5

# ---- wings
N_PACKS = 8
PACK_W, PACK_H, PACK_PITCH, PACK_C0 = 2.0, 30.0, 2.1, 2.8
PANEL_H = 1.0
PACK_TOP = 99.6
HANGER_L = 2.0

# ---- base
BASE_FRAME_R, BASE_FRAME_Z = 1.5, 1.5
ENCLOSURE_R, ENCLOSURE_H = 1.15, 1.25

# ---- scene layout
YARD_AZ = radians(60)       # yard axis (math angle): maintenance azimuth 30 deg from foot 0 (north)
SUN_EL = radians(1.5)       # polar Sun
SUN_AZ = YARD_AZ - radians(90)   # array faces the Sun
EARTH_AZ, EARTH_EL = radians(125), radians(5.5)   # ~150 deg from the Sun: gibbous; libration keeps it within ~7 deg of the horizon
LOWERED_PACK = 5            # port pack index being lowered in the swap scene
LOWERED_TOP = 48.0
