# Rev 27: slip ring and power cabling. Sizing checks for bus voltage, conductors, losses, slip-ring rings and brushes.
# Run: python3 power_cabling_check.py
from math import pi

rho_al, rho_cu = 2.8e-8, 1.7e-8          # ohm.m at ~20 C (lower when cold: conservative)
dens_al = 2700
P_arr = 350e3                             # W at the base, peak
n_packs = 16
P_pack = 1361 * 0.30 * 60 * 0.95         # W, one 2 x 30 m pack at 30% cells, ~95% packing
print(f'one pack ~{P_pack/1e3:.1f} kW peak; 16 packs ~{16*P_pack/1e3:.0f} kW (~350 kW after losses)\n')

# ---------- 1. Bus voltage: trunk mass and loss down the 105 m mast (2 trunks, port + starboard)
L = 105.0
print('trunk choice (2 trunks, each carrying one wing, 1.1% loss target):')
for V in (600, 1000):
    I = P_arr / 2 / V
    A = 95e-6 if V == 1000 else 240e-6
    R = rho_al * L / A
    loss = 2 * (I**2 * 2 * R)
    mass = 2 * 2 * L * A * dens_al
    print(f'  {V:>5} V: {I:.0f} A per trunk, Al {A*1e6:.0f} mm2: loss {loss/1e3:.1f} kW ({loss/P_arr:.1%}), conductor mass {mass:.0f} kg')
V = 1000
print('-> bipolar +/-500 V DC (1 kV pole to pole, 500 V to structure)\n')

# ---------- 2. Pack converter, hanger connector, yard bus
I_pack = P_pack * 0.98 / V
print(f'pack converter (MPPT + isolated boost, ~98%): {I_pack:.0f} A at 1 kV; loss ~{P_pack*0.02/1e3:.2f} kW per pack')
I_wing = 8 * I_pack
A_yard = 50e-6
R_seg = rho_al * 1.9 / A_yard
loss_yard = sum(((8 - k) * I_pack)**2 * 2 * R_seg for k in range(8))
print(f'yard bus per wing: up to {I_wing:.0f} A at the root; Al {A_yard*1e6:.0f} mm2 tapered loss ~{2*loss_yard:.0f} W for both wings')
print(f'hanger connector: 2 x 30 A power pins + 2 pilot pins; e-fuse 40 A per hanger\n')

# ---------- 3. Slip ring (annular drum, mean diameter 0.93 m)
I_ring = P_arr / V
D_ring = 0.93
circ = pi * D_ring
for jd in (5.0,):
    A_b = I_ring / jd
    n = 16
    print(f'slip ring: {I_ring:.0f} A per pole; brushes at {jd} A/cm2 (vacuum derating): {A_b:.0f} cm2 -> {n} brushes of {A_b/n:.1f} cm2 per ring')
drop = 2 * 0.3 * I_ring
R_ring = 0.3e-3
print(f'losses: brush contact {drop:.0f} W + rings and leads {I_ring**2*R_ring:.0f} W = ~{(drop+I_ring**2*R_ring)/1e3:.2f} kW (rev 26 at 600 V: ~0.45 kW)')
rev_yr = 365.25 / 29.53
print(f'brush sliding: {rev_yr:.1f} turns/yr x {circ:.2f} m = {rev_yr*circ:.0f} m per year (brushes wear ~um per km)')
tilt = 0.017                                     # 1 deg
print(f'ring motion at 1 deg tilt: radial {0.25*tilt*1e3:.0f} mm (ring ~0.25 m above the ball centre), axial {D_ring/2*tilt*1e3:.0f} mm; plus 10 mm jack lift')
stack = 4 * 60 + 2 * 20
print(f'ring stack: 4 power-class rings x 60 mm + 2 signal rings x 20 mm = {stack} mm (space 280 mm)\n')

# ---------- 4. Efficiency chain and the service feeder
eta = 0.98 * (1 - 2 * loss_yard / P_arr) * (1 - 2 * (P_arr / 2 / V)**2 * 2 * rho_al * L / 95e-6 * 2 / P_arr) * (1 - (drop + I_ring**2 * R_ring) / P_arr)
print(f'pack converter -> yard -> trunks -> slip ring: ~{eta:.1%} delivered to the fixed side')
dT, alpha = 100, 23e-6
print(f'trunk thermal length change over {L:.0f} m for {dT} K: {L*alpha*dT*1e3:.0f} mm, taken in S-loops at the 36 section joints (~{L*alpha*dT*1e3/36:.0f} mm each)')
P_feed, V_feed = 400, 120
print(f'service feeder up the mast: {P_feed} W at {V_feed} V = {P_feed/V_feed:.1f} A; 2 x 4 mm2 Cu drop {P_feed/V_feed*2*rho_cu*L/4e-6:.1f} V')
mass = 2 * 2 * L * 95e-6 * dens_al * 1.35 + 2 * 2 * 17 * A_yard * dens_al * 1.35 + 60
print(f'cable mass: trunks + yard buses with insulation (x1.35) + trays/feeder/fibre ~60 kg = ~{mass:.0f} kg')
