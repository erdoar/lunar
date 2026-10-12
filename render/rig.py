"""Rig assets (rev 33) built from params.py: fixed bracing and base, and the rotating mast, yard, wings and masthead.

The rotating parts are modelled in a local frame (yard along +x, the cell side of the wings facing -y)
and turned to YARD_AZ as one object, the way the real rig turns on its pivot.
"""
from math import cos, sin, atan2, pi, radians, sqrt
import numpy as np
import bpy
from meshes import MB
import params as P

NAMES = None   # material name -> slot index, set by build()


def M(name):
    return NAMES[name]


def tri_pts(z, R=P.FACE / sqrt(3)):
    return [np.array([R * cos(a), R * sin(a), z]) for a in (radians(-90), radians(30), radians(150))]


# ---------------------------------------------------------------- humanoid figures
def bot(mb, base, heading, kneel=False, reel=True, scale=1.0, shell='bot_shell', visor='visor'):
    """Service bot (or astronaut with shell='suit'), feet at `base`, facing `heading` (rad)."""
    s = scale
    f = np.array([cos(heading), sin(heading), 0.0])
    side = np.array([-sin(heading), cos(heading), 0.0])
    up = np.array([0, 0, 1.0])
    b = np.asarray(base, float)
    hip = b + up * (0.55 if kneel else 0.9) * s
    sh = hip + up * 0.55 * s
    mb.box(hip + up * 0.3 * s, 0.13 * s, 0.2 * s, 0.32 * s, M(shell), (f, side, up))
    mb.sphere(sh + up * 0.22 * s, 0.13 * s, M(shell))
    mb.box(sh + up * 0.22 * s + f * 0.1 * s, 0.03 * s, 0.09 * s, 0.06 * s, M(visor), (f, side, up))
    for sd in (-1, 1):
        sp = sh + side * sd * 0.24 * s
        mb.sphere(sp, 0.07 * s, M('bot_joint'))
        el = sp + up * -0.28 * s + f * 0.1 * s
        mb.tube(sp, el, 0.05 * s, M(shell))
        mb.tube(el, el + f * 0.28 * s + up * 0.05 * s, 0.045 * s, M(shell))
        hp = hip + side * sd * 0.11 * s
        if kneel:
            kn = hp + f * 0.4 * s + up * -0.12 * s if sd < 0 else hp + up * -0.5 * s + f * 0.05 * s
            ft = kn + up * -0.43 * s if sd < 0 else kn + f * -0.42 * s
        else:
            kn = hp + up * -0.45 * s
            ft = kn + up * -0.43 * s
        mb.tube(hp, kn, 0.065 * s, M(shell))
        mb.sphere(kn, 0.07 * s, M('bot_joint'))
        mb.tube(kn, ft, 0.055 * s, M(shell))
        mb.box(ft + f * 0.06 * s + up * 0.03 * s, 0.12 * s, 0.05 * s, 0.03 * s, M('bot_joint'), (f, side, up))
    if reel:
        mb.box(sh + up * -0.2 * s + f * 0.22 * s, 0.09 * s, 0.15 * s, 0.1 * s, M('silver_mli'), (f, side, up))


# ---------------------------------------------------------------- fixed parts (world frame)
def fixed(mats):
    mb = MB()
    # foundation frame + base enclosure (6-panel tub, radiator louvres)
    mb.box((0, 0, 0.1), 1.0, 1.0, 0.12, M('steel'))
    R, z0, z1 = P.ENCLOSURE_R, 0.22, P.ENCLOSURE_H
    for k in range(6):
        a0, a1 = radians(60 * k), radians(60 * (k + 1))
        p0 = np.array([R * cos(a0), R * sin(a0), 0]); p1 = np.array([R * cos(a1), R * sin(a1), 0])
        mid = (p0 + p1) / 2
        out = mid / np.linalg.norm(mid)
        tang = (p1 - p0) / np.linalg.norm(p1 - p0)
        mb.box(mid + (0, 0, (z0 + z1) / 2), np.linalg.norm(p1 - p0) / 2, 0.02, (z1 - z0) / 2, M('osr_radiator'),
               (tang, out, (0, 0, 1)))
        for zz in np.arange(z0 + 0.12, z1 - 0.05, 0.11):
            mb.box(mid + out * 0.05 + (0, 0, zz), np.linalg.norm(p1 - p0) / 2 - 0.08, 0.03, 0.008, M('white_coat'),
                   (tang, out, (0, 0, 1)))
    # struts, feet, stays, ties
    for th in P.FOOT_ANGLES:
        rad = np.array([cos(th), sin(th), 0.0]); tg = np.array([-sin(th), cos(th), 0.0])
        foot = rad * P.FOOT_R
        mb.box(foot + (0, 0, 0.05), P.PAD[0] / 2, P.PAD[1] / 2, P.PAD[2] / 2, M('sintered'), (rad, tg, (0, 0, 1)))
        mb.box(foot + (0, 0, 0.32), 0.45, 0.35, 0.12, M('titanium'), (rad, tg, (0, 0, 1)))
        hinge = foot + (0, 0, 0.62) - rad * 0.2
        mb.box(hinge, 0.12, 0.25, 0.15, M('titanium'), (rad, tg, (0, 0, 1)))
        mb.box(foot + rad * 0.55 + (0, 0, 0.6), 0.25, 0.3, 0.22, M('gold_mli'), (rad, tg, (0, 0, 1)))   # tensioner
        top_c = rad * (P.COLLAR_R + 0.2) + (0, 0, P.STRUT_COLLAR)
        for sd in (-1, 1):
            top = top_c + tg * sd * P.STRUT_SPREAD
            mb.tube(hinge, top, P.STRUT_D / 2, M('white_coat'), n=16)
            d = (top - hinge); L = np.linalg.norm(d); d /= L
            for k in range(1, 15):
                c = hinge + d * L * k / 15
                mb.tube(c - d * 0.04, c + d * 0.04, P.STRUT_D / 2 + 0.012, M('titanium'), n=16)
            mb.box(top, 0.12, 0.1, 0.12, M('titanium'))
        # V-link on the upper collar, stay from its apex to the foot tensioner
        hc = rad * (P.COLLAR_R + 0.08) + (0, 0, P.UPPER_COLLAR)
        sdir = (foot + (0, 0, 0.8)) - hc; sdir /= np.linalg.norm(sdir)
        apex = hc + sdir * P.VLINK_OUT
        for sd in (-1, 1):
            mb.box_between(hc + tg * sd * 0.2, apex, 0.018, 0.005, M('titanium'), up=tuple(np.cross(sdir, tg)))
            mb.box(hc + tg * sd * 0.2, 0.05, 0.05, 0.07, M('titanium'))
        mb.tube(apex, foot + rad * 0.55 + (0, 0, 0.75), P.STAY_D / 2, M('rope'), n=6)
        mb.tube(foot - rad * 0.4 + (0, 0, 0.25), rad * 1.0 + (0, 0, 0.18), P.STAY_D / 2, M('rope'), n=6)   # tie
    # collars (fixed rings, rollers inside, lugs)
    for zc in (P.STRUT_COLLAR, P.UPPER_COLLAR):
        mb.ring((0, 0, 0), 0.95, P.COLLAR_R, zc - P.COLLAR_H / 2, zc + P.COLLAR_H / 2, M('collar_white'), n=64)
        for k in range(6):
            a = radians(60 * k + 30)
            mb.box((0.97 * cos(a), 0.97 * sin(a), zc), 0.06, 0.12, 0.14, M('gold_mli'),
                   ((cos(a), sin(a), 0), (-sin(a), cos(a), 0), (0, 0, 1)))
        for th in P.FOOT_ANGLES:
            mb.box((1.32 * cos(th), 1.32 * sin(th), zc), 0.1, 0.25 if zc < 50 else 0.28, 0.16, M('teal_anod'),
                   ((cos(th), sin(th), 0), (-sin(th), cos(th), 0), (0, 0, 1)))
        a = radians(15)
        mb.box((1.3 * cos(a), 1.3 * sin(a), zc + 0.25), 0.12, 0.12, 0.08, M('gold_mli'))                  # sensor hub
    # landing trays at the maintenance azimuth (fixed on the ground)
    ax = np.array([cos(P.YARD_AZ), sin(P.YARD_AZ), 0.0]); cr = np.array([-sin(P.YARD_AZ), cos(P.YARD_AZ), 0.0])
    for sx in (-1, 1):
        a0, a1 = ax * sx * 1.8, ax * sx * 18.5
        for so in (-0.55, 0.55):
            mb.box_between(a0 + cr * so + (0, 0, 1.5), a1 + cr * so + (0, 0, 1.5), 0.04, 0.08, M('aluminium'))
        for k in range(9):
            p = ax * sx * (1.8 + k * 2.1 - 0.05) + (0, 0, 1.45)
            mb.box(p, 0.03, 0.6, 0.04, M('aluminium'), (ax, cr, (0, 0, 1)))
        for r in (2.4, 10.2, 18.0):
            for so in (-0.55, 0.55):
                p = ax * sx * r + cr * so
                mb.tube(p + (0, 0, -0.1), p + (0, 0, 1.45), 0.04, M('aluminium'))
    # folded spare pack waiting beside the port tray, and one folded pack in its slot
    for (r, o, z) in ((21.0, 0.0, 0.42), (-2.8 - 2.1 * 6 + 0.0, 0.0, 1.85)):
        c = -ax * abs(r) + cr * o + (0, 0, z) if r > 0 else ax * r + (0, 0, z)
        mb.box(c, 1.0, 0.5, 0.35, M('kapton'), (ax, cr, (0, 0, 1)))
        mb.box(c + (0, 0, 0.36), 1.0, 0.12, 0.05, M('gold_mli'), (ax, cr, (0, 0, 1)))
    # astronaut for scale, by the port tray
    astro = -ax * 8.5 + cr * -3.2
    bot(mb, (astro[0], astro[1], 0.02), P.SUN_AZ + pi + 0.6, reel=False, shell='suit', scale=1.0)
    mb.box(astro + cr * -0.0 + (0, 0, 1.35) - np.array([cos(P.SUN_AZ + pi + 0.6), sin(P.SUN_AZ + pi + 0.6), 0]) * 0.22,
           0.12, 0.25, 0.3, M('suit'))                                                                     # PLSS
    return mb.build('rig_fixed', mats)


# ---------------------------------------------------------------- rotating parts (local frame)
def panel(mb, c, w, h, t, tilt):
    """One concertina panel: cells on -y, kapton on +y, frame edges. Tilted about x by `tilt`."""
    ex = np.array([1.0, 0, 0])
    ez = np.array([0, sin(tilt), cos(tilt)])
    ey = np.cross(ez, ex)
    c = np.asarray(c, float)
    v = lambda sx, sy, sz: c + sx * w / 2 * ex + sy * t / 2 * ey + sz * h / 2 * ez
    verts = [v(sx, sy, sz) for sz in (-1, 1) for sy in (-1, 1) for sx in (-1, 1)]
    mb.add(verts, [(0, 1, 5, 4)], [((0, 0), (w, 0), (w, h), (0, h))], M('solar_cell'))
    mb.add(verts, [(2, 6, 7, 3)], [((0, 0), (0, h), (w, h), (w, 0))], M('kapton'))
    mb.add(verts, [(0, 2, 3, 1), (4, 5, 7, 6), (0, 4, 6, 2), (1, 3, 7, 5)],
           [((0, 0), (0, t), (w, t), (w, 0)), ((0, 0), (w, 0), (w, t), (0, t)),
            ((0, 0), (0, h), (t, h), (t, 0)), ((0, 0), (t, 0), (t, h), (0, h))], M('pack_frame'))


def pack(mb, xc, ztop):
    mb.box((xc, 0, ztop + 0.115), 0.98, 0.12, 0.05, M('gold_mli'))                       # pack head
    mb.box((xc + 0.3, 0.0, ztop + 0.22), 0.25, 0.1, 0.06, M('gold_mli'))                  # converter
    mb.box((xc + 0.3, 0.14, ztop + 0.22), 0.25, 0.01, 0.12, M('radiator_black'))         # its radiator fin
    for sx in (-0.5, 0.5):
        mb.tube((xc + sx, 0, ztop + 0.16), (xc + sx, 0, ztop + 0.26), 0.03, M('titanium'), r2=0.005)   # cones
    for k in range(int(P.PACK_H / P.PANEL_H)):
        tilt = radians(1.8) * (1 if k % 2 == 0 else -1)
        mb_z = ztop - (k + 0.5) * P.PANEL_H
        panel(mb, (xc, 0, mb_z), P.PACK_W - 0.04, P.PANEL_H - 0.012, 0.018, tilt)
    mb.box((xc, 0, ztop - P.PACK_H - 0.03), 0.99, 0.03, 0.03, M('pack_frame'))


def rotating(mats):
    mb = MB()
    R = P.FACE / sqrt(3)
    # ---- mast lattice
    v0 = tri_pts(P.MAST_FOOT); v1 = tri_pts(P.MAST_TOP)
    for a, b in zip(v0, v1):
        mb.tube(a, b, P.CHORD_D / 2, M('cfrp'), n=10)
    z = P.MAST_FOOT
    k = 0
    while z < P.MAST_TOP - 1e-6:
        z2 = min(z + P.PANEL, P.MAST_TOP)
        pts0, pts1 = tri_pts(z), tri_pts(z2)
        for i in range(3):
            j = (i + 1) % 3
            a, b = (pts0[i], pts1[j]) if k % 2 == 0 else (pts0[j], pts1[i])
            mb.tube(a, b, P.DIAG_D / 2, M('cfrp'), n=6)
        for p in pts0:
            mb.box(p, 0.065, 0.065, 0.05, M('titanium'))
        z, k = z2, k + 1
    for zs in np.arange(P.MAST_FOOT, P.MAST_TOP + 0.01, P.SECTION):
        pts = tri_pts(zs)
        for i in range(3):
            mb.tube(pts[i], pts[(i + 1) % 3], 0.03, M('titanium'), n=6)
            mb.tube(pts[i] - (0, 0, 0.06), pts[i] + (0, 0, 0.06), P.CHORD_D / 2 + 0.012, M('titanium'), n=10)
    mb.box((0, 0, P.MAST_FOOT), 0.8, 0.8, 0.04, M('titanium'))                         # foot plate
    for zc in (P.STRUT_COLLAR, P.UPPER_COLLAR):                                          # roller bands
        mb.ring((0, 0, 0), 0.86, 0.9, zc - 0.3, zc + 0.3, M('stainless'), n=64)
    # ---- rotating base frame: ring, spokes, battery, cabinet, bot dock
    zf = P.BASE_FRAME_Z
    mb.ring((0, 0, 0), 1.38, 1.5, zf - 0.06, zf + 0.06, M('titanium'), n=48)
    for p in tri_pts(zf):
        d = p / np.linalg.norm(p[:2] + 1e-9)
        mb.box_between(p, np.array([1.42 * d[0], 1.42 * d[1], zf]), 0.05, 0.05, M('titanium'))
    mb.box((0.0, 1.15, zf + 0.35), 0.45, 0.22, 0.3, M('white_coat'))                    # battery
    mb.box((0.0, 1.38, zf + 0.35), 0.4, 0.01, 0.25, M('osr_radiator'))
    mb.box((-1.0, -0.75, zf + 0.4), 0.25, 0.3, 0.35, M('white_coat'))                    # power cabinet
    mb.box((1.05, -0.7, zf + 0.06), 0.3, 0.3, 0.02, M('safety_yellow'))                  # bot dock
    # ---- spreaders and diamond stays (fore/aft = local y)
    for sy in (-1, 1):
        tip = np.array([0, sy * P.SPREADER_HALF, P.SPREADER_Z])
        mb.tube((0, sy * 0.5, P.SPREADER_Z), tip, 0.05, M('cfrp'), n=10)
        mb.box(tip, 0.08, 0.08, 0.08, M('titanium'))
        mb.tube((0, sy * 0.55, P.DIAMOND_LOW), tip, P.ROD_D / 2 + 0.002, M('rod_jacket'), n=6)
        mb.tube(tip, (0, sy * P.CROWN_STAY_ARM, P.MAST_TOP + 0.1), P.ROD_D / 2 + 0.002, M('rod_jacket'), n=6)
        for sx in (-1, 1):                                                                 # braces
            mb.tube((sx * 18.55, 0, P.YARD_Z - 0.05), tip, P.ROD_D / 2 + 0.002, M('rod_jacket'), n=6)
    # ---- yard truss
    Z0, Z1, hy = P.YARD_Z, P.YARD_Z + P.YARD_DEPTH, P.YARD_WIDTH / 2
    for sx in (-1, 1):
        xa, xb = sx * 0.9, sx * P.YARD_HALF
        for y in (-hy, hy):
            for zz in (Z0, Z1):
                mb.tube((xa, y, zz), (xb, y, zz), P.YARD_CHORD_D / 2, M('cfrp'), n=8)
        n = int((P.YARD_HALF - 0.9) / 0.7)
        for i in range(n):
            x0, x1 = sx * (0.9 + 0.7 * i), sx * (0.9 + 0.7 * (i + 1))
            for y in (-hy, hy):
                za, zb = (Z0, Z1) if i % 2 == 0 else (Z1, Z0)
                mb.tube((x0, y, za), (x1, y, zb), 0.02, M('cfrp'), n=6)
            for zz in (Z0, Z1):
                mb.tube((x0, -hy, zz), (x1, hy, zz), 0.015, M('cfrp'), n=5)
            for y in (-hy, hy):
                for zz in (Z0, Z1):
                    mb.box((x0, y, zz), 0.045, 0.045, 0.045, M('titanium'))
        # walkway grating, toe boards, rail stanchions + fall-arrest rail (yellow)
        xm = (xa + xb) / 2
        mb.box((xm, 0, Z1 + 0.05), abs(xb - xa) / 2, hy + 0.02, 0.012, M('grating'))
        for y in (-hy - 0.02, hy + 0.02):
            mb.box((xm, y, Z1 + 0.11), abs(xb - xa) / 2, 0.004, 0.06, M('aluminium'))
        for xs in np.arange(1.0, P.YARD_HALF, 2.0):
            mb.tube((sx * xs, hy + 0.05, Z1 + 0.04), (sx * xs, hy + 0.05, Z1 + 1.14), 0.02, M('safety_yellow'), n=6)
        mb.tube((xa, hy + 0.05, Z1 + 1.14), (xb, hy + 0.05, Z1 + 1.14), 0.03, M('safety_yellow'), n=8)
        # tip frame with lift outriggers
        mb.box((sx * 18.6, 0, Z0 + 0.4), 0.05, hy + 0.05, 0.45, M('titanium'))
        mb.box((sx * 18.55, 0, Z0), 0.06, P.OUTRIGGER + 0.04, 0.05, M('titanium'))
        # topping lifts: two rods splayed to the outriggers
        for sy in (-1, 1):
            mb.tube((sx * 0.2, sy * 0.03, P.MAST_TOP - 0.08), (sx * P.LIFT_TIP, sy * P.OUTRIGGER, Z0 + 0.04),
                    P.ROD_D / 2 + 0.002, M('rod_jacket'), n=6)
            mb.box((sx * P.LIFT_TIP, sy * P.OUTRIGGER, Z0 + 0.15), 0.025, 0.025, 0.1, M('stainless'))
    for zz in (Z0, Z1):
        mb.ring((0, 0, 0), 0.82, 0.95, zz - 0.06, zz + 0.06, M('titanium'), n=48)
    mb.box((0, 0, Z1 + 0.05), 0.95, hy + 0.02, 0.012, M('grating'))
    mb.box((-1.55, 0, Z1 + 0.35), 0.55, 0.22, 0.28, M('silver_mli'))                     # reel garage
    # ---- hangers, reel sockets, packs
    for sx in (-1, 1):
        for i in range(P.N_PACKS):
            xc = sx * (P.PACK_C0 + P.PACK_PITCH * i)
            mb.box((xc, 0, Z0 - 0.09), P.HANGER_L / 2, 0.04, 0.06, M('titanium'))
            for xs in (-0.7, 0.7):
                mb.box((xc + xs, 0, Z0 - 0.02), 0.06, hy + 0.04, 0.015, M('titanium'))
            mb.box((xc, 0, Z1 + 0.12), 0.12, 0.15, 0.055, M('aluminium'))
            if sx == -1 and i == P.LOWERED_PACK:
                for dx in (-0.8, 0.8):
                    mb.tube((xc + dx, 0, Z0 - 0.12), (xc + dx, 0, P.LOWERED_TOP + 0.2), 0.003, M('rope'), n=5)
                pack(mb, xc, P.LOWERED_TOP)
            else:
                pack(mb, xc, P.PACK_TOP)
    # ---- masthead: crown plate, cruciform arms, boss, instrument post, platform, rail
    zt = P.MAST_TOP
    mb.box((0, -0.1, zt + 0.025), 0.78, 0.55, 0.025, M('titanium'))
    mb.tube((0, 0, zt + 0.05), (0, 0, zt + 0.22), 0.12, M('titanium'), n=16, caps=True)
    for sy in (-1, 1):
        mb.box_between((0, sy * 0.1, zt + 0.12), (0, sy * P.CROWN_STAY_ARM, zt + 0.12), 0.05, 0.06, M('titanium'))
    for sx in (-1, 1):
        mb.box_between((sx * 0.1, 0, zt + 0.1), (sx * 0.26, 0, zt + 0.0), 0.06, 0.05, M('titanium'))
    mb.tube((0, 0, zt + 0.22), (0, 0, P.POST_TOP), 0.04, M('aluminium'), n=10)
    mb.box((0, 0.06, P.POST_TOP - 0.1), 0.12, 0.12, 0.07, M('pack_frame'))                # camera
    mb.tube((0, 0.14, P.POST_TOP - 0.1), (0, 0.2, P.POST_TOP - 0.1), 0.04, M('bot_joint'), n=10)
    for sx in (-1, 1):
        mb.tube((0, 0, P.POST_TOP - 0.4), (sx * 0.25, 0, P.POST_TOP - 0.4), 0.012, M('aluminium'), n=6)
        mb.box((sx * 0.25, 0, P.POST_TOP - 0.4), 0.05, 0.05, 0.05, M('gold_mli'))
    mb.tube((0, 0, P.POST_TOP), (0, 0, P.POST_TOP + 0.7), 0.012, M('white_coat'), n=6)
    mb.sphere((0, 0, P.POST_TOP + 0.74), 0.045, M('red_light'))
    mb.box((0, 0, zt + 0.33), 0.1, 0.1, 0.05, M('silver_mli'))
    yb = R / 2 + 0.05
    mb.box((0.2, yb + 0.22, 106.6), 0.55, 0.21, 0.02, M('grating'))
    for xs in (-0.3, 0.7):
        mb.tube((xs, yb + 0.42, 106.6), (xs, yb + 0.42, 107.6), 0.02, M('safety_yellow'), n=6)
    mb.tube((-0.3, yb + 0.42, 107.6), (0.7, yb + 0.42, 107.6), 0.025, M('safety_yellow'), n=6)
    mb.tube((0.55, yb + 0.02, Z1 + 1.0), (0.55, yb + 0.02, 107.7), 0.025, M('safety_yellow'), n=6)
    # ---- bots: one kneeling at the port station, reel in its socket; one at the masthead
    xs5 = -(P.PACK_C0 + P.PACK_PITCH * P.LOWERED_PACK)
    bot(mb, (xs5 + 0.45, 0.05, Z1 + 0.07), pi, kneel=True)
    mb.box((xs5, 0, Z1 + 0.25), 0.15, 0.1, 0.09, M('silver_mli'))
    bot(mb, (0.25, yb + 0.25, 106.62), -pi / 2)
    ob = mb.build('rig_rotating', mats)
    ob.rotation_euler[2] = P.YARD_AZ
    return ob


def build(mats):
    global NAMES
    order = list(mats.keys())
    NAMES = {k: i for i, k in enumerate(order)}
    lst = [mats[k] for k in order]
    return fixed(lst), rotating(lst)
