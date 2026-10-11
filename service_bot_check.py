# Rev 22: service bots replace the halyards. Sizing checks for the climb, the portable reel hoist and the balance.
# Run: python3 service_bot_check.py
from math import sqrt

g = 1.62                     # m/s², Moon
bot, reel, pack = 70.0, 12.0, 140.0   # kg: humanoid-class bot, portable reel hoist, folded concertina pack
H_yard, H_tray = 100.0, 1.5  # m

# 1. Clear core inside the triangular mast lattice (members on the faces only)
for face in (1.2, 1.4):
    r_in = face / (2 * sqrt(3))              # inscribed radius at the chord centrelines
    clear = 2 * (r_in - 0.06)                # less chord/node half-depth
    print(f'mast face {face} m: inscribed Ø{2*r_in:.2f} m, clear core ~Ø{clear:.2f} m')
print('humanoid ~0.45 m shoulders x 0.3 m deep: needs the 1.4 m face over the full height\n')

# 2. Climb (bot + reel on its back) and fall consequences
m = bot + reel
E = m * g * H_yard
print(f'climb {H_yard:.0f} m with reel: {m*g:.0f} N, {E/1e3:.1f} kJ = {E/3600:.1f} Wh (x5 for losses ~{5*E/3600:.0f} Wh)')
t_fall = sqrt(2 * H_yard / g)
print(f'unarrested fall from {H_yard:.0f} m: {t_fall:.1f} s, impact {g*t_fall:.0f} m/s -> captive fall-arrest trolley always\n')

# 3. Portable reel hoist
T = pack * g                                 # N, pack weight on the line
line_d, line_break, line_kgm = 2.5, 3.5e3, 0.025   # mm, N, kg/m (7x19 stainless)
L = H_yard + 5
v, eta, drum = 0.1, 0.6, 0.12                # m/s, efficiency, drum Ø m
print(f'pack on the line: {T:.0f} N; 2.5 mm stainless rope breaks ~{line_break/1e3:.1f} kN -> factor {line_break/T:.0f}')
print(f'line {L:.0f} m, {L*line_kgm:.1f} kg; drum Ø{drum} m: torque {T*drum/2:.0f} N.m, {v/(3.1416*drum)*60:.0f} rpm')
print(f'power at {v} m/s: {T*v:.0f} W mech, ~{T*v/eta:.0f} W electric; energy per 100 m {T*H_yard/3600:.1f} Wh')
t_move = (H_yard - H_tray) / v / 60
print(f'lower or hoist {H_yard-H_tray:.0f} m at {v} m/s: {t_move:.0f} min\n')

# 4. Swap time (one pack, one bot)
climb_v = 0.15                               # m/s inside the mast, clipped on
t = 2 * H_yard / climb_v / 60 + 2 * 17 / 0.3 / 60 + 2 * t_move + 20
print(f'one swap: climb up/down {2*H_yard/climb_v/60:.0f} min, walk out/back {2*17/0.3/60:.0f} min, lower+hoist {2*t_move:.0f} min,'
      f' rig/unrig + ground handling ~20 min -> ~{t/60:.1f} h')
print(f'first fit of 16 packs: hoist only ~{16*(t_move+15)/60:.0f} h with one bot, half that with two\n')

# 5. Balance about the mast (wing plane), worst cases
r_pack, r_tip = 16.0, 17.0
M_pack = T * r_pack / 1e3
M_bot = (bot + reel) * g * r_tip / 1e3
print(f'outer pack missing: {M_pack:.1f} kN.m; bot+reel at a yard tip: {M_bot:.1f} kN.m')
print(f'worst (pack off one side, bot at the other tip): {M_pack+M_bot:.1f} kN.m vs quake case ~12 kN.m')
print('while the pack hangs on the line its weight is still on the yard: no imbalance until it lands')
# yard point load
print(f'yard tip point load, bot + reel + pack on line: {(bot+reel+pack)*g:.0f} N (wing ~2.2 kN per side)')
