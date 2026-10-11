# Rev 26: base pivot and drive detail, and the removable protection enclosure. Sizing checks.
# Run: python3 base_drive_check.py
from math import pi, radians

g = 1.62
# ---------- 1. Drive train: motor -> planetary -> self-locking worm -> torque limiter -> pin wheel -> pin ring
D_ring, n_pins, n_wheel = 1.2, 96, 12
i_pl, i_worm = 50, 60
pitch = pi * D_ring / n_pins
i_ring = n_pins / n_wheel
i_tot = i_pl * i_worm * i_ring
print(f'pin ring Ø{D_ring} m, {n_pins} pins: pitch {pitch*1e3:.1f} mm; pin wheel {n_wheel} teeth, pitch Ø{pitch*n_wheel/pi*1e3:.0f} mm; ring ratio {i_ring:.0f}')
print(f'overall ratio motor -> mast {i_pl} x {i_worm} x {i_ring:.0f} = {i_tot:,.0f}')
eta = 0.85 * 0.35 * 0.95                     # planetary, self-locking worm, pin mesh
T_design, T_clutch, T_run = 500, 300, (50, 165)
print(f'motor torque at the {T_design} N.m design ring torque: {T_design/(i_tot*eta):.3f} N.m')
print(f'torque limiter on the pin-wheel hub: {T_clutch/i_ring:.1f} N.m (= {T_clutch} N.m at the ring)')
F = lambda T: T / (D_ring / 2)
print(f'mesh force: running {F(T_run[0]):.0f}-{F(T_run[1]):.0f} N, at the limiter {F(T_clutch):.0f} N, design {F(T_design):.0f} N')
print(f'hand drive at the worm shaft (bot hex tool): {i_worm*i_ring/360:.2f} turns per degree, '
      f'{T_design/(i_worm*i_ring*0.35*0.95):.1f} N.m at the design torque\n')

# ---------- 2. Tracking and slewing
rate = 360 / 708.7                           # deg/h, one turn per synodic month
step = 0.1
print(f'tracking {rate:.3f} deg/h: a {step} deg step every {step/rate*60:.0f} min, '
      f'{step/360*i_tot:.1f} motor turns per step (~0.4 s at 1,000 rpm)')
m_w, m_y, m_s = 2740, 400, 500               # kg: wings (2-17 m), yard (0-17 m), diamond stays/spreaders (~6 m)
I = m_w * (17**3 - 2**3) / (3 * 15) + m_y * 17**2 / 3 + m_s * 6**2 / 3 + 2700 * 0.5**2
slew = 5.0                                   # deg/min
w = radians(slew) / 60
T_acc = 100                                  # N.m spare for acceleration, kept below the 200 N.m collar interlock
print(f'inertia about the axis ~{I:,.0f} kg.m2; slew {slew} deg/min = {w*1e3:.2f} mrad/s, '
      f'motor {slew/360*i_tot:.0f} rpm, ramp {I*w/T_acc:.0f} s at {T_acc} N.m, KE {0.5*I*w*w:.2f} J')
print(f'parking 180 deg: {180/slew:.0f} min; motor power at the design torque while slewing {T_design*w/eta:.1f} W\n')

# ---------- 3. Pivot parts
R, t_dome = 0.25, 0.020
A_dome = 2 * pi * R**2 * (1 - 0.1736)        # cap to 80 deg
print(f'pivot ball as a {t_dome*1e3:.0f} mm steel dome shell on a Ti pedestal: ~{A_dome*t_dome*7800:.0f} kg')
A_cup = 2 * pi * R**2 * (1 - 0.819)          # cap to 35 deg
print(f'wear cup: Ti backing 8 mm ~{A_cup*0.008*4500:.1f} kg + 6 mm composite ~{A_cup*0.006*6000:.1f} kg + rim ~3 kg; rim Ø{2*0.264*0.574:.2f} m')
print('cup and ball both come out UPWARD through a Ø0.55 m opening in the foot plate into the mast core;'
      ' the jack only unloads the pivot (~10 mm lift)\n')

# ---------- 4. Slip ring heat (all array power crosses it)
P, V = 350e3, 600
I_ = P / V
brush = 0.6 * I_                             # two Ag-MoS2-graphite contact drops of ~0.3 V
ring = I_**2 * 0.3e-3
print(f'slip ring: {P/1e3:.0f} kW at {V} V DC = {I_:.0f} A; brush drop {brush:.0f} W + conductors {ring:.0f} W = ~{(brush+ring)/1e3:.2f} kW of heat')
print(f'brushes at ~5 A/cm2 (vacuum derating): ~{I_/5:.0f} cm2 per polarity, e.g. 24 brushes of 5 cm2\n')

# ---------- 5. Enclosure thermal balance
sig = 5.67e-8
r_t, h_t = 0.98, 0.62
A_wall = 2 * pi * r_t * h_t
A_lid = pi * (1.06**2 - 0.72**2)
A_rad = A_wall / 2                           # 3 of 6 wall panels are radiators
A_mli = A_wall / 2 + A_lid
T_in, T_sink = 253, 100                      # K: keep >= -20 C inside; cold polar sink
Q_mli = 0.03 * sig * A_mli * (T_in**4 - T_sink**4)
Q_louv = 0.15 * sig * A_rad * (T_in**4 - T_sink**4)
print(f'enclosure: wall {A_wall:.2f} m2 ({A_rad:.2f} m2 radiator), lid {A_lid:.2f} m2')
print(f'survival (array dark, louvres shut): MLI {Q_mli:.0f} W + radiators {Q_louv:.0f} W = ~{Q_mli+Q_louv:.0f} W of heaters;'
      f' 48 h = {(Q_mli+Q_louv)*48/1e3:.1f} kWh from the base battery')
Q = (brush + ring)
T_r = (Q / (0.8 * sig * A_rad) + 150**4) ** 0.25
print(f'operating: {Q:.0f} W through {A_rad:.2f} m2 of radiator (e 0.8, 150 K sink) -> radiator ~{T_r-273:.0f} C\n')

# ---------- 6. Dropped-object energy (outside the mast core)
for m in (0.5, 1.0, 5.0):
    print(f'{m} kg dropped from 100 m: {m*g*100:.0f} J at {(2*g*100)**0.5:.0f} m/s')
