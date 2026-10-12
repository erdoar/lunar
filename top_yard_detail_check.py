# Rev 32: top yard and pack hanger detail. Sizing checks (supersedes the halyard-era top_yard_check.py numbers).
# Run: python3 top_yard_detail_check.py
from math import atan2, sin, cos, hypot, pi, degrees

g = 1.62
# ---------- 1. Wing span: do 8 packs fit?
n, w_p, gap = 8, 2.0, 0.1
span = n * w_p + (n - 1) * gap
r_collar = 1.27                              # m, collar ring outer radius (cartridge grapple)
r_in = 1.8
r_out = r_in + span
print(f'8 packs of {w_p} m with {gap} m gaps need {span:.1f} m; the old 2-17 m span held only 15.0 m')
print(f'new wing: {r_in} to {r_out:.1f} m from the axis, {r_in-r_collar:.2f} m clear of the collar rings; hanger pitch {w_p+gap:.1f} m')
centres = [r_in + w_p / 2 + i * (w_p + gap) for i in range(n)]
print('hanger centres (m): ' + ', '.join(f'{c:.1f}' for c in centres))
r_tip, r_lift = r_out + 0.2, r_out
print(f'yard tip at ±{r_tip:.1f} m (lift attached at {r_lift:.1f} m): yard {2*r_tip:.1f} m long (was 34 m)\n')

# ---------- 2. Loads on one arm and the topping lift
m_pack, m_hanger = 150, 8
m_yard = 12 * r_tip + 15                     # kg per arm, truss at ~12 kg/m plus root node
m_walk = 4 * r_tip                           # walkway + rail
r_root = 0.7
mom = sum(m_pack * g * c for c in centres) + n * m_hanger * g * sum(centres) / n \
    + m_yard * g * r_tip / 2 + m_walk * g * r_tip / 2
L = r_lift - r_root
R_tip = (mom - (m_pack * n + m_hanger * n + m_yard + m_walk) * g * r_root) / L
W_arm = (m_pack * n + m_hanger * n + m_yard + m_walk) * g
head = 8.0
ang = atan2(head, r_lift)
T = R_tip / sin(ang)
C = T * cos(ang)
print(f'one arm: {W_arm/1e3:.2f} kN total; tip reaction {R_tip/1e3:.2f} kN; lift angle {degrees(ang):.1f} deg')
print(f'topping lift {T/1e3:.2f} kN (was ~3.0); yard compression {C/1e3:.2f} kN per arm (was ~2.7)')

# ---------- 3. Yard truss: chords, bending, buckling, deflection
D_c, t_c, E = 0.060, 0.002, 110e9
A_c = pi * D_c * t_c
depth, width = 0.8, 0.5
w = W_arm / L
M = w * L**2 / 8
F_ch = M / depth / 2                         # per chord (2 top, 2 bottom)
s_top = (F_ch + C / 4) / A_c
print(f'chords Ø{D_c*1e3:.0f} x {t_c*1e3:.0f} mm CFRP ({A_c*1e6:.0f} mm2): midspan moment {M/1e3:.1f} kN.m -> {F_ch/1e3:.1f} kN per chord'
      f' (+{C/4/1e3:.2f} kN axial); top chord {s_top/1e6:.0f} MPa')
I_s = 4 * A_c * (depth / 2)**2
I_w = 4 * A_c * (width / 2)**2
for nm, I in (('vertical', I_s), ('sideways', I_w)):
    print(f'arm buckling ({nm}, {L:.1f} m): {pi**2*E*I/L**2/1e3:.0f} kN vs {C/1e3:.1f} kN')
d = 5 * w * L**4 / (384 * E * I_s)
print(f'midspan deflection under the full wing {d*1e3:.0f} mm; a pack swap changes the tip load by {m_pack*g:.0f} N\n')

# ---------- 4. Top rigging: steel rope vs coated CFRP rod (thermal)
L_lift = hypot(r_lift, head)
for name, Ll in (('topping lift', L_lift), ('diamond stay, spreader to head', 27.0)):
    st = Ll * 17.3e-6 * 110                  # white-coated steel, ~110 K swing
    k_st = 100e9 * 14e-6 / Ll
    cf = Ll * 0.5e-6 * 110
    k_cf = 2 * 140e9 * 50e-6 / Ll
    print(f'{name} ({Ll:.1f} m): steel 6 mm {st*1e3:.0f} mm -> ±{k_st*st/2/1e3:.1f} kN if fixed; '
          f'2 x Ø8 mm CFRP rods {cf*1e3:.1f} mm -> ±{k_cf*cf/2/1e3:.2f} kN')
print(f'CFRP rod Ø8 mm breaks at ~{2000e6*50e-6/1e3:.0f} kN: factor ~{2000e6*50e-6/T:.0f} on the lift with one rod of the pair\n')

# ---------- 5. Pack hanger
L_h = 2.0
print(f'hanger: Ti box beam {L_h} m, bolted to both bottom chords at 2 nodes; pack {m_pack*g:.0f} N; latch rated 5 kN (~20x)')
print(f'16 hangers x ~{m_hanger} kg = {16*m_hanger} kg; packs ~{m_pack} kg each with converter')
print(f'balance: outer pack centre {centres[-1]:.1f} m -> {m_pack*g*centres[-1]/1e3:.1f} kN.m; bot+reel at the tip {84*g*r_tip/1e3:.1f} kN.m;'
      f' worst {(m_pack*g*centres[-1]+84*g*r_tip)/1e3:.1f} kN.m vs quake ~12')
