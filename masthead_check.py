# Rev 33: masthead and topping lift detail. Sizing checks.
# Run: python3 masthead_check.py
from math import atan2, sin, cos, tan, hypot, pi, sqrt, degrees

g = 1.62
# ---------- 1. Topping lift geometry (line of action from the crown axis point to the yard tip outrigger)
Z_HEAD, Z_TIP, R_TIP = 108.0, 100.0, 18.5      # m: crown node, bottom-chord tip node, tip radius
ang = atan2(Z_HEAD - Z_TIP, R_TIP)
L = hypot(Z_HEAD - Z_TIP, R_TIP)
print(f'lift {L:.2f} m long at {degrees(ang):.1f} deg below horizontal; crown tang pin 0.2 m out on the line')

# ---------- 2. Loads (same arm model as top_yard_detail_check.py)
centres = [2.8 + 2.1 * i for i in range(8)]
m_pack, m_hanger, r_root = 150, 8, 0.7
m_yard, m_walk = 12 * 18.7 + 15, 4 * 18.7
Lr = R_TIP - r_root
mom = sum((m_pack + m_hanger) * g * c for c in centres) + (m_yard + m_walk) * g * 18.7 / 2
W = (8 * (m_pack + m_hanger) + m_yard + m_walk) * g
R = (mom - W * r_root) / Lr
T = R / sin(ang)
m_bot = 70 + 14                                # bot + reel at the outer station
dR = m_bot * g * (centres[-1] - r_root) / Lr
T_max = (R + dR) / sin(ang)
print(f'tip reaction {R/1e3:.2f} kN -> lift {T/1e3:.2f} kN static ({T/2/1e3:.2f} kN per rod); '
      f'with a bot + reel at the outer station {T_max/1e3:.2f} kN')
dRp = m_pack * g * (centres[-1] - r_root) / Lr
dT = dRp / sin(ang)
print(f'one outer pack off: lift changes by {dT:.0f} N; the 2 load pins on a lift read {dT/2:.0f} N each (10 kN pins, 0.1% = 10 N)\n')

# ---------- 3. Rod bundles: strength, shipping coil, dynamics
d_r, n_r = 0.003, 7                            # 7 x Ø3 mm pultruded rods per bundle, in a white jacket
A_b = n_r * pi * d_r**2 / 4
A_8 = pi * 0.008**2 / 4
F_b = 2000e6 * A_b * 0.9                       # 90% termination efficiency (potted cone)
print(f'bundle 7 x Ø3 mm: {A_b*1e6:.1f} mm2 (one Ø8 mm rod is {A_8*1e6:.1f}); breaks at ~{F_b/1e3:.0f} kN')
print(f'factor {F_b/(T_max/2):.0f} per rod at the worst case; one rod alone holding the whole lift: {F_b/T_max:.0f}')
D_coil = 1.4                                   # m, coil to fit a 1.5 m freight module
for nm, d in (('Ø8 mm solid rod', 0.008), ('Ø3 mm rod in a bundle', 0.003)):
    print(f'coiled to Ø{D_coil} m: {nm} bending strain {d/D_coil*100:.2f}% (ultimate ~1.6%)')
print(f'a 20 m lift is {L/(pi*D_coil):.1f} turns; a 27 m diamond-stay leg {27/(pi*D_coil):.1f} turns\n')
mu = A_b * 1600 + 0.02                         # kg/m per bundle with jacket
f1 = 1 / (2 * L) * sqrt(T / 2 / mu)
sag = mu * g * L**2 / (8 * T / 2)
print(f'per bundle {mu*1e3:.0f} g/m: first string mode {f1:.1f} Hz, sag {sag*1e3:.0f} mm; lift {2*mu*L:.1f} kg + fittings')
k_r = 140e9 * A_b / L
print(f'one bundle {k_r/1e3:.0f} kN/m: a 1 mm length mismatch shifts {k_r*1e-3:.0f} N between the pair')
tq = T_max / 2 * (0.0015 / (2 * pi) + 0.15 * 0.015 / (2 * cos(pi / 6)))
print(f'M16 x 1.5 barrel adjuster: 1/8 turn = {k_r*0.0015/8:.0f} N; ~{tq:.1f} N.m to turn at the worst-case load (a bot can trim it)\n')

# ---------- 4. Walkway clearance: the two rods splay to outriggers either side of the walkway
y_head, y_tip = 0.03, 0.55                     # m: rod half-spacing at the crown tang and at the tip outrigger
z_walk = 100.84                                # walkway grating top
bot_h, bot_w = 1.8, 0.30                       # bot envelope: 1.8 m tall, ±0.30 m
worst = 9
for i in range(1, 1000):
    x = R_TIP * i / 1000
    z = Z_HEAD - (Z_HEAD - Z_TIP) * x / R_TIP
    y = y_head + (y_tip - y_head) * x / R_TIP
    h = z - z_walk
    if 0 <= h <= bot_h:
        worst = min(worst, y - bot_w)
x_head = (Z_HEAD - z_walk - bot_h) / ((Z_HEAD - Z_TIP) / R_TIP)
x_down = (Z_HEAD - z_walk) / ((Z_HEAD - Z_TIP) / R_TIP)
print(f'on the centreline the lift would pass {bot_h} m above the walkway at {x_head:.1f} m and reach it at {x_down:.1f} m:')
print(f'  stations 14.35 to 17.5 m would sit under it -> split each lift: its 2 rods splay to ±{y_tip} m outriggers at the tip')
print(f'  closest approach to a ±{bot_w} m x {bot_h} m bot envelope: {worst*1e3:.0f} mm (at head height); below walkway level beyond {x_down:.1f} m')
y_rail = y_head + (y_tip - y_head) * (Z_HEAD - z_walk - 1.1) / (Z_HEAD - Z_TIP)
print(f'  at rail height (1.1 m) the rod is {y_rail:.2f} m out, {(y_rail-0.30)*1e3:.0f} mm outside the rail trolley line')
lat = (T_max / 2) * (y_tip - y_head) / L
print(f'  each rod pulls the outrigger inward by {lat:.0f} N (the pair cancels across the tip frame); a broken rod leaves the other carrying the tip at {y_tip} m: {R*y_tip:.0f} N.m of arm torsion\n')

# ---------- 5. Masthead: crown loads, imbalance, deflection
T_ds, a_ds = 1.0e3, atan2(6 - 0.95, 27.0)     # diamond stay pre-tension; from a crown arm at 0.95 m to the spreader tip
V = 2 * T * sin(ang) + 2 * T_ds * cos(a_ds) + 60 * g
print(f'crown: 2 lifts + 2 diamond stays + ~60 kg of crown and instruments -> {V/1e3:.1f} kN down the masthead')
print(f'stay arms 0.95 m out (clear of the lattice by the 0.81 m vertex): {T_ds*cos(a_ds)*0.95:.0f} N.m at each arm root')
dH = dT * cos(ang) + m_bot * g * (centres[-1] - r_root) / Lr / tan(ang)
M = dH * 8.0
A_c = pi * 0.100 * 0.003                       # assumed mast chords Ø100 x 3 mm CFRP
Rc = 1.4 / sqrt(3)
I = 1.5 * A_c * Rc**2
d = dH * 8.0**3 / (3 * 110e9 * I)
print(f'worst imbalance (outer pack off one side, bot at the other tip): {dH:.0f} N sideways at the crown,')
print(f'  {M/1e3:.1f} kN.m at the yard; chord force ~{M/(1.5*Rc):.0f} N; crown moves {d*1e3:.1f} mm (bending, Ø100 x 3 chords assumed)')
print(f'horizon from the crown: {sqrt(2*1737.4e3*108)/1e3:.1f} km to the ground, {sqrt(2*1737.4e3*109.5)/1e3+sqrt(2*1737.4e3*2)/1e3:.1f} km to a 2 m rover mast from the 109.5 m post top')
