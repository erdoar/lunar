# Torsional stiffness of the upper collar with a Y-bridle per bracing plane:
# one cable from the foot to a free split node J, then two legs from J to the tips of two
# hinged arms (V) on the collar. J's position is solved (static condensation), so the result
# includes the junction sliding. Compared with two independent cables (rev 7) and one radial cable.
# Run: python3 bridle_check.py
import numpy as np

EA = 100e9 * 18e-6            # 6 mm rope
FOOT_R, ZC = 30.0, 62.0       # foot radius, collar height
RT, ST = 8.0, 3.0             # arm tip: radial reach, tangential half-spread


def rot(p, th):
    c, s = np.cos(th), np.sin(th)
    return np.array([c * p[0] - s * p[1], s * p[0] + c * p[1], p[2]])


def plane_members(f, T):
    """Return member list for one plane at azimuth 0. f: split position from tips (0) to foot (1)."""
    F = np.array([FOOT_R, 0, 0.0])
    T1, T2 = np.array([RT, ST, ZC]), np.array([RT, -ST, ZC])
    M = (T1 + T2) / 2
    J = M + f * (F - M)
    u_leg = (T1 - J) / np.linalg.norm(T1 - J)
    u_main = (F - J) / np.linalg.norm(F - J)
    cos_a = -np.dot(u_leg, u_main)            # half-angle between the legs, seen from J
    T_leg = T / (2 * cos_a)
    return F, T1, T2, J, T_leg


def energy(th, uJs, f, T):
    U = 0.0
    for i, az in enumerate((0, 2 * np.pi / 3, 4 * np.pi / 3)):
        F, T1, T2, J, Tl = plane_members(f, T)
        R = lambda p: rot(p, az)
        F, T1, T2, J = R(F), R(T1), R(T2), R(J)
        Jd = J + uJs[3 * i:3 * i + 3]
        for a, b, t0, a0, b0 in ((F, Jd, T, F, J), (rot(T1, th), Jd, Tl, T1, J), (rot(T2, th), Jd, Tl, T2, J)):
            L0 = np.linalg.norm(a0 - b0); L = np.linalg.norm(a - b); d = L - L0
            U += t0 * d + 0.5 * EA / L0 * d * d
    return U


def k_condensed(f, T, h=1e-4):
    n = 10                                    # theta + 3 x (J displacement)
    x0 = np.zeros(n)
    def U(x): return energy(x[0], x[1:], f, T)
    Hm = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            e_i = np.eye(n)[i] * h; e_j = np.eye(n)[j] * h
            Hm[i, j] = (U(x0 + e_i + e_j) - U(x0 + e_i - e_j) - U(x0 - e_i + e_j) + U(x0 - e_i - e_j)) / (4 * h * h)
    Ktt, Ktu, Kuu = Hm[0, 0], Hm[0, 1:], Hm[1:, 1:]
    return Ktt - Ktu @ np.linalg.solve(Kuu, Ktu)


if __name__ == '__main__':
    print('split position f (0 = at the arm tips, 1 = at the foot) vs torsional stiffness, kN.m/rad')
    for T in (1500, 3000, 5000):
        row = [f'{k_condensed(f, T)/1000:7.1f}' for f in (0.1, 0.3, 0.5, 0.7, 0.9)]
        print(f'T = {T/1000:.1f} kN per plane: f=0.1..0.9 ->', ' '.join(row))
    print('reference: 2 independent cables (rev 7) ~322; single radial cable ~2.9')
