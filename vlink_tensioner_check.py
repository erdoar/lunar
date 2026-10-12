# Rev 30: V-link and stay tensioner detail. Sizing checks.
# Run: python3 vlink_tensioner_check.py
from math import atan, atan2, cos, sin, hypot, degrees, pi

sig = 5.67e-8
# ---------- 1. V-plate: geometry, stress, mass
L_v, s_p, t, w = 1.0, 0.4, 0.008, 0.030      # m: hinge axis to apex, pin spacing, plate thickness, leg width
half = atan((s_p / 2) / L_v)
leg = hypot(L_v, s_p / 2)
for T in (1.5e3, 3.0e3, 6.0e3):
    F_leg = T / 2 / cos(half)
    print(f'V-plate at {T/1e3:.1f} kN: {F_leg:.0f} N per leg, {F_leg/(w*t)/1e6:.1f} MPa in a {w*1e3:.0f} x {t*1e3:.0f} mm leg')
m = 2 * leg * w * t * 4430 + 0.35
print(f'legs {leg:.2f} m long, half-angle {degrees(half):.1f} deg; Ti-6Al-4V mass ~{m:.1f} kg with bosses\n')

# ---------- 2. Load pins: what the couple looks like
R_FOOT, Z_C, R_C = 30.0, 62.0, 1.45
beta = atan2(Z_C, R_FOOT - R_C)
r_a = R_C + L_v * cos(beta)
for M in (10, 200, 500):
    F_t = M / (3 * r_a)
    c = F_t * L_v / s_p
    print(f'collar torque {M:>3} N.m: tangential pull at each apex {F_t:5.1f} N -> pin couple +/-{c:5.1f} N')
print('-> the doc\'s "+/-0.2 kN at 200 N.m" corrects to ~+/-90 N (0.2 kN is the 500 N.m figure)')
print('load pins, 2-axis, 3 kN range at 0.1% = 3 N: resolve ~7 N.m of collar torque; 200 N.m is ~30x the resolution\n')

# ---------- 3. Stay cable: stiffness and thermal swing
L_s = hypot(R_FOOT - r_a, Z_C - L_v * sin(beta))
EA = 100e9 * 14e-6                           # 6 mm 7x19 stainless: E_rope ~100 GPa on ~14 mm2 of metal
k_c = EA / L_s
print(f'stay {L_s:.1f} m, EA {EA/1e6:.1f} MN, axial stiffness {k_c/1e3:.1f} kN/m; stretch at 1.5 kN {1.5e3/k_c*1e3:.0f} mm, at 3 kN {3e3/k_c*1e3:.0f} mm')
for name, a, e in (('bare stainless', 0.40, 0.30), ('white coated', 0.20, 0.85)):
    T_sun = (a * 1361 / (pi * e * sig)) ** 0.25    # thin wire lit side-on by the horizontal Sun
    T_shade = 100
    dT = T_sun - T_shade
    dL = L_s * 17.3e-6 * dT
    print(f'{name}: sunlit ~{T_sun:.0f} K, shade ~{T_shade} K, swing {dT:.0f} K -> {dL*1e3:.0f} mm, '
          f'passive tension swing +/-{k_c*dL/2/1e3:.1f} kN if held rigid')
tau = (0.14 * 500) / (0.85 * 4 * sig * 250**3 * pi * 0.006)
print(f'wire thermal time constant ~{tau/60:.0f} min; shadows sweep at 0.51 deg/h -> changes over tens of minutes or more')
print('CFRP mast and struts barely move (alpha ~0), so only the steel stays and ties drift\n')

# ---------- 4. Tensioner = the foot winch: drum, worm, buffer, servo
D_d, i_w, i_p = 0.30, 50, 30
T_max = 3.0e3
tq = T_max * D_d / 2
print(f'drum Ø{D_d} m: {tq:.0f} N.m at {T_max/1e3:.0f} kN; worm {i_w}:1 (self-locking) x planetary {i_p}:1 -> motor ~{tq/(i_w*i_p*0.35*0.9):.2f} N.m')
v = 0.5e-3
print(f'trim speed {v*1e3:.1f} mm/s = {v/(pi*D_d)*i_w*i_p*60:.0f} motor rpm; a ~250 mm thermal change is followed in <10 min of motor time')
k_b = 40e3
k_s = 1 / (1 / k_c + 1 / k_b)
print(f'Belleville buffer {k_b/1e3:.0f} kN/m, +/-15 mm: series stiffness {k_s/1e3:.1f} kN/m; between trims (deadband 0.1 kN) the stay drifts {0.1e3/k_s*1e3:.0f} mm')
print('servo: hold 1.5 kN (or 3 kN "stiff" mode) +/-0.1 kN; power ~10 W average per foot from the fixed side, base battery backed\n')

# ---------- 5. Foot node force balance (per bracing plane, from section 3)
T_s, T_t = 1.5, 1.0                          # kN stay, tie
C = 2.5                                      # kN strut compression (both tubes)
ang_s = beta
b_strut = atan2(35.0, R_FOOT - 4.0)
Fh = -T_t - T_s * cos(ang_s) + C * cos(b_strut)          # outward positive: stay and tie pull in, strut pushes out
Fv = T_s * sin(ang_s) - C * sin(b_strut)
print(f'foot: stay {T_s} kN at {degrees(ang_s):.0f} deg, strut {C} kN at {degrees(b_strut):.0f} deg, tie {T_t} kN horizontal')
print(f'  net on the foot: horizontal {Fh:+.2f} kN (small: carried by pad friction, trimmed out with the tie), vertical {Fv:+.2f} kN (negative = pressing down on the pad)')
print('rule: keep strut compression > ~1.2 x stay tension so the pad never lifts; the foot servos keep that ratio')
