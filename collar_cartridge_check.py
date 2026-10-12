# Rev 29: collar roller cartridge detail. Sizing checks: loads, contact stress, roller taper, friction cases, springs.
# Run: python3 collar_cartridge_check.py
from math import pi, sqrt, atan, degrees

R_band = 0.975                     # m, band outer radius (band Ø1.95 m)
r_thr = 0.935                      # m, mean radius of the thrust running faces
D_roll, W_roll = 0.100, 0.030      # m, roller diameter and face width
n = 6

# ---------- 1. Loads per roller (from section 4)
F_up = (3 * 1.5 * 0.899 + 0.25) / n          # kN, upper collar, per upper thrust roller
F_st = 5.7 / n                               # kN, strut collar, per lower thrust roller
for name, F in (('upper collar thrust', F_up), ('strut collar thrust', F_st)):
    print(f'{name}: {F:.2f} kN per roller, {F*n/(n-1):.2f} kN with one cartridge out')
F_max = 1.15e3                               # N, design case (one cartridge out, strut collar)
F_rad = 250                                  # N, radial roller preload
print()

# ---------- 2. Tapered thrust rollers: roll without spin on a flat annulus
half = atan((D_roll / 2) / r_thr)
print(f'thrust roller taper: half-angle {degrees(half):.2f} deg, cone apex on the mast axis -> no spin')
print(f'(a straight {W_roll*1e3:.0f} mm roller would scrub +/-{W_roll/2/r_thr:.1%} across its face)\n')

# ---------- 3. Hertz contact, crowned Si3N4 tyre on a 440C running strip
E1, v1, E2, v2 = 310e9, 0.27, 200e9, 0.28
Es = 1 / ((1 - v1**2) / E1 + (1 - v2**2) / E2)
Rx, Ry = D_roll / 2, 0.200                   # rolling radius and crown radius
Re = sqrt(Rx * Ry)
a = (3 * F_max * Re / (4 * Es)) ** (1 / 3)
p0 = 3 * F_max / (2 * pi * a**2)
print(f'contact: E* {Es/1e9:.0f} GPa, crown R {Ry*1e3:.0f} mm; at {F_max/1e3:.2f} kN: radius {a*1e3:.2f} mm, peak {p0/1e6:.0f} MPa')
print('  (hardened 440C strip and Si3N4 tyre both run routinely at 1.5-2.5 GPa)\n')

# ---------- 4. Collar friction torque: normal, one bearing locked (sleeve path), one roller skidding
N_up = n * F_up * 1e3 + n * F_rad            # N, upper collar: thrust + radial preload
mu_eff = 0.0015                              # hybrid dry-lubricated bearing + rolling loss, referred to the tyre
T_norm = N_up * mu_eff * R_band
mu_sleeve, r_sleeve = 0.15, 0.010
mu_sl_eff = mu_sleeve * r_sleeve / (D_roll / 2)
T_sleeve = T_norm + F_max * mu_sl_eff * R_band
mu_skid = 0.30
T_skid = T_norm + F_max * mu_skid * R_band
print(f'upper collar normal friction torque: ~{T_norm:.0f} N.m (design note says ~10 N.m)')
print(f'one roller on its sleeve path (mu {mu_sleeve} at r {r_sleeve*1e3:.0f} mm): ~{T_sleeve:.0f} N.m -> runs on, alarm only')
print(f'one roller skidding (both paths locked, mu {mu_skid}): ~{T_skid:.0f} N.m -> above the 200 N.m interlock: drive stops\n')

# ---------- 5. Bearing and roller life
turns_day = 2 * pi * R_band / (pi * D_roll)
print(f'roller turns: {turns_day:.0f} per lunar day, ~{turns_day*12.4:.0f} per year, ~{turns_day*12.4*10:,.0f} in 10 years')
C_6004 = 9.4e3
L10 = (C_6004 / F_max) ** 3 * 1e6
print(f'hybrid 6004-size bearing (C ~{C_6004/1e3:.1f} kN): L10 at {F_max/1e3:.2f} kN = {L10:.1e} turns -> margin x{L10/(turns_day*12.4*10):,.0f}')
print('  (dry-film life, not fatigue, is what the vacuum life test must prove)\n')

# ---------- 6. Springs and release travel
k_rad = 10e3                                 # N/m, radial swing-arm spring
print(f'radial roller: {F_rad:.0f} N preload, {k_rad/1e3:.0f} N/mm, +/-10 mm float -> {F_rad-k_rad*0.01:.0f} to {F_rad+k_rad*0.01:.0f} N')
print('thrust rollers: Belleville stacks preloaded to 300 N, 1.5 mm to a hard stop;')
print('  the loaded roller sits on its stop (rigid), the unloaded one keeps 300 N so nothing rattles in a quake')
print('release cam (90 deg, bot hex tool): thrust rollers retract 3 mm, radial roller 15 mm -> cartridge slides out free\n')

# ---------- 7. Thermal: steel running strips on a Ti band
L = 2 * pi * r_thr
dT = 200
d = L * (10.1e-6 - 8.6e-6) * dT
print(f'440C strips on a Ti band, {dT} K swing: {d*1e3:.1f} mm mismatch round the ring -> 6 strip segments, scarf joints, ~{d/6*1e3:.1f} mm each')

# ---------- 8. Mass and collar sensor hub
m = 3.0 + 3 * 0.55 + 0.8 + 0.4
print(f'\ncartridge mass ~{m:.1f} kg (C-frame 3.0, rollers 3 x 0.55, springs and cam 0.8, sensors 0.4); 12 fitted + 2 spares')
P_hub = 5.0
print(f'collar sensor hub ~{P_hub:.0f} W: 48 h of darkness = {P_hub*48:.0f} Wh battery, charged by a ring of small cells on the collar')
