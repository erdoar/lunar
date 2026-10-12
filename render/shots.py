"""Camera shots. Positions are in metres; `loc` helpers place a camera relative to a target by azimuth/elevation.

Azimuths are math angles (deg, from +x). The Sun is at SUN_AZ (-30 deg); cameras on that side see the cell faces.
"""
from math import cos, sin, radians, degrees
import params as P

SUN = degrees(P.SUN_AZ)


def L2W(x, y, z):
    """Rotating-frame point (yard along x) to world."""
    a = P.YARD_AZ
    return (x * cos(a) - y * sin(a), x * sin(a) + y * cos(a), z)


def FOOT(az_deg, r, z, side=0.0):
    """Point near the foot at az_deg: r metres out along its plane, `side` metres across it."""
    a = radians(az_deg)
    return (r * cos(a) - side * sin(a), r * sin(a) + side * cos(a), z)


def around(target, az, el, dist):
    t = target
    return (t[0] + dist * cos(radians(el)) * cos(radians(az)),
            t[1] + dist * cos(radians(el)) * sin(radians(az)),
            t[2] + dist * sin(radians(el)))


ISO = 35.264
SHOTS = [
    dict(name='01_iso_rig', title='Isometric, whole rig', ortho=True, target=(0, 0, 54), az=SUN + 50, el=ISO,
         scale=132, res=(1440, 1920), exposure=1.6),
    dict(name='02_iso_site', title='Isometric, site on the crater rim', ortho=True, target=(-20, -10, 0), az=SUN + 50, el=ISO,
         scale=430, res=(1920, 1080), exposure=2.0),
    dict(name='03_ground_hero', title='Ground level, from the sunward side', target=(0, 0, 47), az=SUN - 12, el=0,
         dist=150, ground=True, eye=1.7, lens=17, res=(1920, 1080), exposure=0.0),
    dict(name='04_ground_foot', title='Ground level at a strut foot', target=FOOT(330, 22, 7.0),
         pos=FOOT(330, 36, 0, side=-4.0), ground=True, eye=1.1, lens=16, res=(1920, 1080), exposure=0.6),
    dict(name='05_zoom_masthead', title='Zoom: masthead, crown and topping lifts', target=L2W(0, 0.1, 107.4),
         az=SUN + 72, el=3, dist=8.5, lens=28, res=(1920, 1080), exposure=0.0),
    dict(name='06_zoom_yard_tip', title='Zoom: yard tip, walkway between the lift rods', target=L2W(-12.5, 0, 100.6),
         pos=L2W(-21.5, -3.2, 103.2), lens=26, res=(1920, 1080), exposure=0.0),
    dict(name='07_pack_swap', title='Pack swap: one pack on two ropes', target=L2W(-7, 0, 60),
         pos=L2W(-34, -82, 50), lens=24, res=(1920, 1080), exposure=0.2),
    dict(name='08_zoom_base', title='Zoom: base, pivot enclosure and landing trays', target=(-0.8, -3.0, 1.4),
         az=SUN + 10, el=9, dist=13, lens=24, res=(1920, 1080), exposure=0.3),
    dict(name='09_far_rim', title='From 260 m along the rim, Earth low in the sky', target=(0, 0, 44),
         az=degrees(P.EARTH_AZ) + 168, el=0, dist=260, ground=True, eye=2.0, lens=35, res=(1920, 1080), exposure=0.3),
    dict(name='10_iso_plan', title='High isometric: tripod, trays and shadows', ortho=True, target=(0, 0, 10), az=SUN + 50,
         el=62, scale=95, res=(1920, 1080), exposure=1.8),
]
