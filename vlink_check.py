# Upper-collar twist ("wind-up") stiffness with a V-link torque lever (rev 14).
# One stay cable per bracing plane runs from the foot to the apex of a V-link hinged on two close,
# horizontally aligned pins on the upper collar. Under tension the V aligns with the cable, so the cable
# effectively attaches at a larger radius r_a. Twist resistance is geometric (pre-tension x geometry):
#     k = 3 * T * R_foot * r_a / L_cable       (per collar, N.m/rad)
# The V's in-plane lever turns the cable's sideways (tangential) pull into a couple at its two pins.
# Run: python3 vlink_check.py
import math

R_FOOT, Z_C, R_C = 30.0, 62.0, 1.45       # foot radius, collar height, pin radius (m)
PIN_SPACING = 0.4                         # m, the two close joints


def vlink(L, T):
    beta = math.atan2(Z_C, R_FOOT - R_C)                  # cable slope from horizontal
    r_a = R_C + L * math.cos(beta)
    z_a = Z_C - L * math.sin(beta)
    L_c = math.hypot(R_FOOT - r_a, z_a)
    k = 3 * T * R_FOOT * r_a / L_c
    return r_a, k


if __name__ == '__main__':
    print('V length L (hinge axis to shackle hole) vs collar twist stiffness')
    for T in (1500, 3000):
        for L in (0.0, 0.5, 1.0, 2.0, 3.0):
            r_a, k = vlink(L, T)
            M = 500.0                                     # N.m, partly seized roller
            F_t = M / (3 * r_a)                           # tangential pull per V at the apex
            couple = F_t * L / PIN_SPACING if L else 0
            print(f'T={T/1000:.1f} kN  L={L:.1f} m: r_a={r_a:.2f} m, k={k/1000:5.1f} kN.m/rad, '
                  f'twist at 10 N.m {math.degrees(10/k):.2f} deg, at 500 N.m {math.degrees(M/k):.1f} deg, '
                  f'pin couple at 500 N.m +/-{couple:.0f} N')
