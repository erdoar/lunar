# Rev 28: pack converter and hanger connector. Sizing checks.
# Run: python3 pack_converter_check.py
sig = 5.67e-8
S, eff = 1361, 0.30

# ---------- 1. Cell temperature and strings
q = S * (0.90 - eff)                       # W/m2 absorbed and not converted (absorptance ~0.90)
T = (q / (2 * 0.85 * sig)) ** 0.25         # flat panel radiating from both faces to a cold sky
print(f'panel temperature facing the low Sun: ~{T-273:.0f} C')
cell_A, Vmp25, dV = 0.0064, 2.35, -0.006   # 8 x 8 cm triple-junction cell, V/C
Vmp = Vmp25 + dV * (T - 298)
Imp = cell_A * S * eff / Vmp
n_ser, n_str_panel = 136, 2
V_str = n_ser * Vmp
print(f'cell Vmp {Vmp:.2f} V, Imp {Imp:.2f} A; string of {n_ser} cells: {V_str:.0f} V; 2 strings per 2 m2 panel ({2*n_ser*cell_A/2:.0%} packing)')
bands = [8, 8, 7, 7]                       # panels per MPPT band, top to bottom
P_tot = 0
for j, n in enumerate(bands):
    I = n * n_str_panel * Imp
    P = V_str * I
    P_tot += P
    print(f'  band {j+1}: {n} panels, {n*n_str_panel} strings in parallel, {I:.1f} A at {V_str:.0f} V = {P/1e3:.1f} kW')
print(f'pack ~{P_tot/1e3:.1f} kW at the converter input; banded by height because terrain shade rises from the bottom\n')

# ---------- 2. Converter chain and device derating
V_link, V_out_half = 450, 500
eta_boost, eta_dab = 0.992, 0.988
eta = eta_boost * eta_dab
loss = P_tot * (1 - eta)
print(f'4 interleaved boost MPPT stages {V_str:.0f} -> {V_link} V ({eta_boost:.1%}); dual active bridge, 2 secondaries stacked to +/-500 V ({eta_dab:.1%})')
print(f'overall {eta:.1%}; loss {loss:.0f} W; output {P_tot*eta/1e3:.1f} kW, {P_tot*eta/1000:.1f} A at 1 kV')
for name, v, rating in (('boost and primary bridge', V_link, 1200), ('each secondary bridge', V_out_half, 1200)):
    print(f'  {name}: {v} V on {rating} V SiC = {v/rating:.0%} of rating (single-event burnout derating target <= 50%)')
print()

# ---------- 3. Radiator on the pack head
T_rad = 333                                 # K, ~60 C plate
T_sink = 200
q_r = 0.85 * sig * (T_rad**4 - T_sink**4)
A_need = loss / q_r
print(f'radiator at {T_rad-273} C to a {T_sink} K sink: {q_r:.0f} W/m2 per face -> {A_need:.2f} m2 needed')
fin = 2.0 * 0.45
print(f'hinged fin 2.0 x 0.45 m, both faces, view factor ~0.6: {2*fin*0.6:.2f} m2 effective; ~4 kg with embedded heat pipes')
print('keep-warm when the array is dark: ~5 W per pack from the bus side, 16 packs = 80 W from the base battery\n')

# ---------- 4. Hanger connector
I_pin = P_tot * eta / 1000
R_c = 0.2e-3
print(f'power contacts: {I_pin:.0f} A each (rated 30 A); contact loss {2*I_pin**2*R_c:.2f} W')
F_c = 12
print(f'mating force: 5 contacts x ~{F_c} N = {5*F_c} N, from the reel hoist (pack weight {140*1.62:.0f} N, reel stalls ~2x)')
print('pin lengths: PE longest (make first, break last), +/- middle, 2 pilots 4 mm shorter (make last, break first)')
v_hoist = 0.01                              # m/s creep speed in the last 50 mm
print(f'at the {v_hoist*1e3:.0f} mm/s final creep, 4 mm of pilot lead = {0.004/v_hoist*1e3:.0f} ms before power pins move (e-fuse opens in <1 ms)')
print('clearance +/- 40 mm, creepage >= 25 mm (ribbed insulator); 500 V to PE')
