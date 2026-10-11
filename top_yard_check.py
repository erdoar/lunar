# Top yard sizing (rev 17). Run: python3 top_yard_check.py
import math
g = 1.62
WING = 1370.0            # kg per wing (8 packs + top bar)
YARD = 400.0             # kg, 34 m truss
R_IN, R_OUT, R_TIP = 2.0, 17.0, 17.0
for head in (5.0, 8.0):  # masthead height above the yard
    V = WING * g / 2 / 1000 + YARD / 2 * g / 1000 / 2       # kN at the tip: outer halyard + half of the half-yard weight
    ang = math.atan2(head, R_TIP)
    T = V / math.sin(ang); C = T * math.cos(ang)
    print(f'masthead {head:.0f} m above yard: lift angle {math.degrees(ang):.1f} deg, topping lift {T:.2f} kN, yard compression {C:.2f} kN')
H = WING * g / 2 / 1000
print(f'halyard tension (wing hanging) {H:.2f} kN each; 4 halyards {4*H:.1f} kN')
v = 0.1
P = 4 * H * 1000 * v / 0.7
print(f'hoist power at {v} m/s, 70% efficient: {P:.0f} W')
D = 0.4
rpm = v / (math.pi * D) * 60
Tq = 4 * H * 1000 * D / 2
print(f'traction sheave D={D} m: {rpm:.1f} rpm, shaft torque {Tq:.0f} N.m; motor 3000 rpm -> ratio {3000/rpm:.0f}:1, motor torque {Tq/(3000/rpm)/0.7:.1f} N.m')
stroke = 100 - 2.5
L_out = 100 + 17 + stroke; L_in = 100 + 2 + stroke
print(f'halyard lengths: outer {L_out:.0f} m, inner {L_in:.0f} m (stroke {stroke:.1f} m)')
# yard truss buckling between mast and tip (pinned-pinned 17 m), 3 CFRP chords 40x2 mm, depth 0.8 m
A = math.pi * 0.040 * 0.002; E = 100e9
I = 2 * A * 0.4**2      # two chords at +/-0.4 m (weak-axis depth 0.5 m similar)
Pcr = math.pi**2 * E * I / 17**2
print(f'yard truss Euler (17 m, depth 0.8 m) {Pcr/1000:.0f} kN')
print(f'panel tilt need: cos(1.5 deg) = {math.cos(math.radians(1.5))*100:.3f}% -> no elevation-angle drive needed')
