# Base spherical pivot sizing (rev 21): hard convex ball (fixed) under a concave dry-lubricated wear cup (turning).
# Run: python3 pivot_check.py
import math
N = 9.9e3                     # N, net vertical load on the pivot
R = 0.25                      # m, ball radius
a_in, a_out = math.radians(5), math.radians(35)     # contact annulus half-angles (small apex relief)
# projected contact area of the annulus
r_in, r_out = R * math.sin(a_in), R * math.sin(a_out)
A = math.pi * (r_out**2 - r_in**2)
p = N / A
# friction torque: uniform pressure over the projected annulus, effective radius 2/3 (r_o^3 - r_i^3)/(r_o^2 - r_i^2)
r_eff = 2 / 3 * (r_out**3 - r_in**3) / (r_out**2 - r_in**2)
print(f'contact annulus r {r_in*1000:.0f}–{r_out*1000:.0f} mm, area {A*1e4:.0f} cm², mean pressure {p/1e6:.2f} MPa, r_eff {r_eff*1000:.0f} mm')
for mu in (0.03, 0.08, 0.15):
    print(f'  mu {mu}: friction torque {mu*N*r_eff:.0f} N.m')
cup_depth = R * (1 - math.cos(a_out))
print(f'cup depth {cup_depth*1000:.0f} mm; the cup lifts out upward through the foot plate (rev 26), so the jack only unloads the pivot (~10 mm)')
# sliding distance and Archard wear
s_year = 2 * math.pi * r_eff * 365.25 / 29.53          # m per Earth year at r_eff
for k in (1e-15, 1e-14, 1e-13):                         # m^3/(N.m): clean MoS2 composite in vacuum ... dusty third-body
    V = k * N * s_year * 10
    print(f'  k {k:.0e} m3/N.m: wear depth after 10 years {V/A*1e6:.3f} um')
print(f'sliding distance {s_year:.1f} m per year')
