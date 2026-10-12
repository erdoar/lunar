# Rev 31: strut A-frame and foot pad detail. Sizing checks.
# Run: python3 strut_foot_check.py
from math import pi, sqrt, atan, atan2, degrees, radians, cos, sin

g = 1.62
# ---------- 1. Tube section and buckling
D, t, E, rho = 0.30, 0.002, 110e9, 1600       # m, m, Pa (axial-dominated layup), kg/m3
A = pi * D * t
I = pi / 8 * D**3 * t
L = 46.0
m_l = A * rho
P_cr = pi**2 * E * I / L**2
P_tube = 1.25e3
print(f'tube Ø{D} x {t*1e3:.0f} mm: A {A*1e6:.0f} mm2, I {I:.2e} m4, {m_l:.1f} kg/m, {m_l*L:.0f} kg per tube')
print(f'Euler, pinned, {L:.0f} m: {P_cr/1e3:.1f} kN per tube; load {P_tube/1e3:.2f} kN -> margin {P_cr/P_tube:.1f}')
kj = 0.85
print(f'with 14 sleeve joints (EI knockdown {kj}): {kj*P_cr/1e3:.1f} kN -> margin {kj*P_cr/P_tube:.1f}')
print(f'both tubes buckling together out of the A plane: {2*kj*P_cr/1e3:.1f} kN vs {2*P_tube/1e3:.1f} kN -> no lacing needed')
s_ax = P_tube / A
s_cr = 0.3 * E * t / (D / 2)
print(f'wall stress {s_ax/1e6:.2f} MPa; local shell buckling (0.3 Et/R knockdown) {s_cr/1e6:.0f} MPa: not a concern\n')

# ---------- 2. Sag, thermal bow, amplification, frequency
b = atan2(35.0, 30.0 - 4.0)
w = m_l * g * cos(b)
sag = 5 * w * L**4 / (384 * E * I * kj)
bow = 0.5e-6 * 100 / D * L**2 / 8            # alpha_axial 0.5e-6, 100 K across the tube (one-sided Sun)
amp = 1 / (1 - P_tube / (kj * P_cr))
print(f'strut at {degrees(b):.0f} deg: self-weight sag {sag*1e3:.0f} mm, thermal bow {bow*1e3:.0f} mm (white coat halves it)')
print(f'amplified by compression x{amp:.2f}: ~{(sag+bow)*amp*1e3:.0f} mm; bending stress {(w*L**2/8)*amp/(I/(D/2))/1e6:.1f} MPa')
f = (pi / 2) * sqrt(E * I * kj / (m_l * L**4))
print(f'first bending frequency ~{f:.2f} Hz\n')

# ---------- 3. A-frame geometry and end rotations during the scissor erection
half = atan(1.5 / L)
print(f'A-frame: tubes spread +/-1.5 m at the top over {L:.0f} m -> {2*degrees(half):.1f} deg included at the foot')
print(f'scissor erection: strut swings from flat (0 deg) to {degrees(b):.0f} deg -> each end turns ~{degrees(b):.0f} deg about a tangential axis')
print('-> a hinge pin carries that swing; a spherical bushing (+/-5 deg) takes only misalignment\n')

# ---------- 4. Tent-pole sleeve joint
M_er = m_l * g * L**2 / 8                    # strut horizontal on its dolly during erection (worst bending)
ov = 0.30
F_b = M_er / (0.67 * ov)
print(f'erection, strut flat: midspan moment {M_er:.0f} N.m; 0.3 m spigot overlap -> bearing couple {F_b/1e3:.1f} kN (Ti spigot, CFRP socket)')
print('internal steel cord ~1 kN only closes the joints against rattle; the overlap carries the bending')
print(f'segments: 15 x ~3.1 m per tube, {15*3.1:.1f} m; ~{15*2*3:.0f} segments for 3 A-frames\n')

# ---------- 5. Foot pad: bearing, sliding, socket
N = 0.64e3
Fh = 0.14e3
mu = 0.5
print(f'pad load {N/1e3:.2f} kN down, {Fh/1e3:.2f} kN sideways static; friction alone {mu*N/1e3:.2f} kN (margin {mu*N/Fh:.1f})')
q = 12e3 * 0.1                               # rough quake: ~0.1 m/s2 on ~12 t of rig and bracing, ~1.2 kN lateral shared by 3 feet
print(f'a quake adds up to ~{q/3/1e3:.1f} kN per foot sideways -> friction alone is marginal: add a cone in a sintered socket')
cone = 30
print(f'cone half-angle {cone} deg in a sintered socket: sideways capacity ~{N*(1/sin(radians(cone))*mu + cos(radians(cone)))/1e3:.1f} kN+ (self-centring, like the pivot)')
A_pad = 1.2 * 1.2
print(f'pad {A_pad:.2f} m2 sintered, 0.3 m thick: bearing pressure {N/A_pad:.0f} Pa (trivial); settlement taken by the servo tensioners')
m_d = 2 * m_l * L / 2 + 25
print(f'erection dolly: foot carries ~{m_d*g:.0f} N; drag at mu 0.5 ~{0.5*m_d*g:.0f} N, well within the tie winch')
