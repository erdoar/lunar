# Deck spoke sizing (rev 19). Run: python3 spoke_check.py
import math
g = 1.62
E = 120e9                       # CFRP tube, longitudinal (UD-dominated)
rho = 1600.0
L = 5.2                         # m, hub edge (r 0.8) to bogie pivot (r 6.0)


def tube(d, t):
    A = math.pi * d * t
    I = math.pi / 8 * d**3 * t
    return A, I


# ---- main spoke: rigid at the hub, pinned on the bogie; hub load W/3 enters at the root, bogie reaction at the tip
W_hub = 8.9 + 0.3 * g + (0.15 + 0.1) * g        # mast foot + hub + winch/power share (kN)
P = W_hub / 3
w = 0.020 * g                                   # 20 kg/m self weight incl. fittings, kN/m
M = P * L + w * L**2 / 2
print(f'MAIN: hub share {P:.2f} kN, root moment {M:.1f} kN.m')
Ac, Ic = tube(0.050, 0.002)
for d in (1.0,):
    # triangular section: 2 top chords, 1 bottom chord; lever ~ depth
    Fb = M / d; Ft = Fb / 2
    Pcr = math.pi**2 * E * Ic / 0.8**2
    print(f'  depth {d} m at root: bottom chord tension {Fb:.1f} kN ({Fb*1e3/Ac/1e6:.0f} MPa), top chords {Ft:.1f} kN compression each; '
          f'chord buckling over 0.8 m panel {Pcr/1e3:.0f} kN (x{Pcr/1e3/Ft:.0f})')
# tip deflection: tapered 1.0 -> 0.4 m, use average depth 0.7 m, triangle: I ~ 2/3 * A * d^2 (approx, two top + one bottom)
d_avg = 0.7
I_tr = (Ac * (2 * d_avg / 3)**2) + 2 * Ac * (d_avg / 3)**2
EI = E * I_tr
delta = P * 1e3 * L**3 / (3 * EI)
print(f'  truss EI (avg depth 0.7 m) {EI:.2e} N.m2; deflection at the bogie end {delta*1000:.1f} mm (L/{L/delta:.0f})')
# lateral: drive force share at the tip
F_lat = 0.5
print(f'  lateral design load {F_lat} kN at tip -> {F_lat*L:.1f} kN.m; top chords 0.5 m apart -> {F_lat*L/0.5:.1f} kN')
# mass build-up per metre
chords = 3 * Ac * rho
diag_A, _ = tube(0.030, 0.0015)
diags = 3.75 * diag_A * rho
nodes = 3 * 1.5 / 0.8
print(f'  mass/m: chords {chords:.2f}, diagonals {diags:.2f}, Ti nodes {nodes:.1f}, fittings ~4 -> {chords+diags+nodes+4:.1f} kg/m (carry 20 kg/m)')

# ---- light spoke: cantilever from the hub; ring girder segment + gratings + live load
q = (15 * 3.14 + 0.24e3 / 9 + 60) * g / 1000    # ring girder share, grating share, misc -> kN
live = 0.5                                     # suited astronaut / robot at the tip, kN (~300 kg)
tray = 2 * 0.23 / 2                            # 2 landed packs on the inboard tray strip, half to this spoke
Pl = q + live + tray
Ml = Pl * L
print(f'LIGHT: tip load {Pl:.2f} kN, root moment {Ml:.1f} kN.m')
Ac2, Ic2 = tube(0.035, 0.0015)
dl = 0.35
print(f'  depth {dl} m: chord force {Ml/dl:.1f} kN; panel buckling {math.pi**2*E*Ic2/0.6**2/1e3:.0f} kN')
I2 = Ac2 * (2 * dl / 3)**2 + 2 * Ac2 * (dl / 3)**2
print(f'  tip deflection {Pl*1e3*L**3/(3*E*I2)*1000:.1f} mm')
