# Rev 22/23: service bots replace the halyards. Sizing checks for the climb, the twin-rope reel hoist, pack spin and balance.
# Run: python3 service_bot_check.py
from math import sqrt

g = 1.62                     # m/s², Moon
bot, reel, pack = 70.0, 14.0, 140.0   # kg: humanoid-class bot, twin-rope reel hoist (chest pack), folded concertina pack
H_yard, H_tray = 100.0, 1.5  # m

# 1. Clear core inside the triangular mast lattice (members on the faces only)
for face in (1.2, 1.4):
    r_in = face / (2 * sqrt(3))              # inscribed radius at the chord centrelines
    clear = 2 * (r_in - 0.06)                # less chord/node half-depth
    print(f'mast face {face} m: inscribed Ø{2*r_in:.2f} m, clear core ~Ø{clear:.2f} m')
print('humanoid ~0.45 m shoulders x 0.3 m deep: needs the 1.4 m face over the full height\n')

# 2. Climb (bot + reel as a chest pack, when one has to go up) and fall consequences
m = bot + reel
E = m * g * H_yard
print(f'climb {H_yard:.0f} m carrying a reel (it is normally parked at the top): {m*g:.0f} N, {E/1e3:.1f} kJ = {E/3600:.1f} Wh (x5 for losses ~{5*E/3600:.0f} Wh)')
t_fall = sqrt(2 * H_yard / g)
print(f'unarrested fall from {H_yard:.0f} m: {t_fall:.1f} s, impact {g*t_fall:.0f} m/s -> captive fall-arrest trolley always\n')

# 3. Twin-rope reel hoist: 2 ropes on one shaft (equal stroke) to the two ends of the pack head
T = pack * g                                 # N, pack weight, shared by the 2 ropes
line_break, line_kgm = 2.4e3, 0.016          # N, kg/m (2 mm 7x19 stainless)
L = H_yard + 8
v, eta, drum = 0.1, 0.6, 0.10                # m/s, efficiency, drum Ø m
print(f'pack {T:.0f} N on 2 ropes ({T/2:.0f} N each); 2 mm stainless breaks ~{line_break/1e3:.1f} kN -> factor {line_break/(T/2):.0f}')
print(f'ropes 2 x {L:.0f} m, {2*L*line_kgm:.1f} kg; drums Ø{drum} m: torque {T*drum/2:.0f} N.m, {v/(3.1416*drum)*60:.0f} rpm')
print(f'power at {v} m/s: {T*v:.0f} W mech, ~{T*v/eta:.0f} W electric; energy per 100 m {T*H_yard/3600:.1f} Wh')
t_move = (H_yard - H_tray) / v / 60
print(f'lower or hoist {H_yard-H_tray:.0f} m at {v} m/s: {t_move:.0f} min\n')

# 3b. Spin: a single rope gives no torsional restraint; two ropes d apart (bifilar) do
d = 1.6                                      # m, eye spacing on the 2 m pack head
I = pack * 2.0**2 / 12                       # kg m², pack about its vertical axis
k_lay = 0.07                                 # rope torque ~ k_lay * T * d_rope (regular lay)
tq = 2 * k_lay * (T / 2) * 0.002
for Lr in (100, 30, 5, 1):
    kt = T * d * d / (4 * Lr)
    print(f'bifilar at {Lr:>3} m: stiffness {kt:6.1f} N.m/rad, twist from same-hand lay torque {tq/kt*57.3:4.1f} deg,'
          f' period {2*3.1416*(I/kt)**0.5:4.1f} s')
print('opposite-hand pair: lay torques cancel; flared guide forks square the last few degrees\n')

# 4. Swap time (one pack, one bot)
climb_v = 0.15                               # m/s inside the mast, clipped on
t = 2 * H_yard / climb_v / 60 + 2 * 18.7 / 0.3 / 60 + 2 * t_move + 15
print(f'one swap: climb up/down {2*H_yard/climb_v/60:.0f} min, walk out/back {2*17/0.3/60:.0f} min, lower+hoist {2*t_move:.0f} min,'
      f' rig/unrig + ground handling ~15 min -> ~{t/60:.1f} h')
print(f'first fit of 16 packs: hoist only ~{16*(t_move+15)/60:.0f} h with one bot, half that with two\n')

# 5. Balance about the mast (wing plane), worst cases
r_pack, r_tip = 17.5, 18.7                  # rev 32: outer hanger centre and yard tip
M_pack = T * r_pack / 1e3
M_bot = (bot + reel) * g * r_tip / 1e3
print(f'outer pack missing: {M_pack:.1f} kN.m; bot+reel at a yard tip: {M_bot:.1f} kN.m')
print(f'worst (pack off one side, bot at the other tip): {M_pack+M_bot:.1f} kN.m vs quake case ~12 kN.m')
print('while the pack hangs on the line its weight is still on the yard: no imbalance until it lands')
# yard point load
print(f'yard tip point load, bot + reel + pack on line: {(bot+reel+pack)*g:.0f} N (wing ~2.2 kN per side)')

# 6. Power: bots recharge from a storage battery on the rotating base frame (rev 24)
bot_batt = 2.0                               # kWh, humanoid-class pack
swap_kwh = 1.2 * 0.35                        # ~1.2 h at ~350 W average (motion, compute, heaters)
dark_h, dark_w = 48, 250                     # longest dark spell to ride through; reels, garage, sensors, survival heat
base = 2 * bot_batt + dark_h * dark_w / 1e3 + 4
print(f'one swap uses ~{swap_kwh:.2f} kWh of a {bot_batt} kWh bot battery (~{swap_kwh/bot_batt:.0%})')
print(f'base battery: 2 full bot charges {2*bot_batt:.0f} kWh + {dark_h} h dark at {dark_w} W {dark_h*dark_w/1e3:.0f} kWh + margin -> ~{base:.0f} kWh')
print(f'mass at ~120 Wh/kg packed, heated and boxed: ~{base*1e3/120:.0f} kg; bot charge at 1 kW: ~{bot_batt:.0f} h')
