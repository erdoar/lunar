# Generates strut-foot.svg (rev 31): A-frame elevation, tent-pole joint, end hinge, foot pad section and numbers.
# Run: python3 make_strut_foot_svg.py
from math import tan, radians

o = []
A = o.append
W, H = 1300, 930
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="12">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><pattern id="g" width="8" height="8" patternUnits="userSpaceOnUse"><path d="M0 8L8 0" stroke="#a08c6c"/></pattern>'
  '<pattern id="sn" width="6" height="6" patternUnits="userSpaceOnUse"><rect width="6" height="6" fill="#d8ccb4"/><circle cx="3" cy="3" r="1" fill="#a08c6c"/></pattern>'
  '<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker></defs>')
A('<style>.s{stroke:#222;stroke-width:1.3}.l{stroke:#555;stroke-width:1;fill:none}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:15px;font-weight:bold}</style>')
CF, TI, PIN, COL, STAY, TIE = '#5d6d7e', '#9fb3c8', '#c9a227', '#4a9', '#8e44ad', '#c87f0a'


def lab(x1, y1, x2, y2, lines, anchor='start'):
    A(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" class="l"/>')
    for j, t in enumerate(lines):
        A(f'<text x="{x2+(4 if anchor=="start" else -4):.0f}" y="{y2+4+j*14:.0f}" text-anchor="{anchor}" font-size="11.5">{t}</text>')


# ================= A. A-frame in its own plane =================
A('<text x="20" y="30" class="t">A. One A-frame, in its plane</text>')
A('<text x="20" y="48" font-size="11" fill="#555">width drawn x4</text>')
sy, sx, cx, foot_y = 12.0, 12.0 * 4, 150, 640
Y = lambda m: foot_y - m * sy
top = 46.0
A(f'<rect x="{cx-2.2*sx}" y="{Y(top)-26}" width="{4.4*sx}" height="16" fill="{COL}" opacity="0.6" class="s"/><text x="{cx}" y="{Y(top)-14}" text-anchor="middle" font-size="10.5" style="stroke:none">strut collar torque bracket</text>')
for side in (-1, 1):
    A(f'<line x1="{cx}" y1="{Y(0)}" x2="{cx+side*1.5*sx}" y2="{Y(top)}" stroke="{CF}" stroke-width="7"/>')
    for k in range(1, 15):
        f = k / 15
        x = cx + side * 1.5 * sx * f
        A(f'<line x1="{x-5}" y1="{Y(top*f)}" x2="{x+5}" y2="{Y(top*f)}" stroke="#fff" stroke-width="2"/>')
    A(f'<circle cx="{cx+side*1.5*sx}" cy="{Y(top)}" r="6" fill="{PIN}" class="s"/>')
A(f'<path d="M{cx-10} {Y(0)-18} L{cx} {Y(0)+4} L{cx+10} {Y(0)-18} Z" fill="{TI}" class="s"/><circle cx="{cx}" cy="{Y(0)+4}" r="6" fill="{PIN}" class="s"/>')
A(f'<path d="M{cx+1.5*sx+16} {Y(0)} V{Y(top)}" class="l" marker-start="url(#ar)" marker-end="url(#ar)"/><text x="{cx+1.5*sx+20}" y="{Y(23)}" font-size="11">~46 m</text>')
A(f'<path d="M{cx-1.5*sx} {Y(top)+18} H{cx+1.5*sx}" class="l" marker-start="url(#ar)" marker-end="url(#ar)"/><text x="{cx}" y="{Y(top)+32}" text-anchor="middle" font-size="11">3 m</text>')
lab(cx + 0.8 * sx, Y(top * 0.55), 240, Y(30), ['2 CFRP tubes', 'Ø0.3 m x 2 mm', '15 segments each'])
lab(cx, Y(0) - 8, 240, Y(4), ['Ti Y-fitting', '+ one hinge'])
A(f'<text x="20" y="{Y(0)+40}" font-size="11">No lacing: both tubes must buckle</text><text x="20" y="{Y(0)+54}" font-size="11">together out of plane (18.5 kN vs 2.5 kN).</text>')

# ================= B. tent-pole sleeve joint =================
A('<text x="380" y="30" class="t">B. Tent-pole sleeve joint (section)</text>')
k, jx, jy = 400, 400, 210
X = lambda m: jx + m * k
A(f'<rect x="{X(0)}" y="{jy-0.15*k}" width="{0.42*k}" height="{0.30*k}" fill="none" stroke="{CF}" stroke-width="5"/>')
A(f'<rect x="{X(0.30)}" y="{jy-0.15*k-3}" width="{0.42*k-0.30*k+0.30*k}" height="{0.30*k+6}" fill="none" stroke="{CF}" stroke-width="6" opacity="0.7"/>')
A(f'<rect x="{X(0.12)}" y="{jy-0.138*k}" width="{0.30*k}" height="{0.276*k}" fill="{TI}" opacity="0.7" class="s"/>')
A(f'<line x1="{X(0.0)}" y1="{jy}" x2="{X(0.72)}" y2="{jy}" stroke="#333" stroke-width="2" stroke-dasharray="8 3"/>')
A(f'<rect x="{X(0.40)}" y="{jy-0.15*k-14}" width="18" height="12" fill="#555"/><rect x="{X(0.20)}" y="{jy+0.15*k-2}" width="10" height="10" fill="{PIN}"/>')
A(f'<path d="M{X(0.12)} {jy+0.15*k+24} H{X(0.42)}" class="l" marker-start="url(#ar)" marker-end="url(#ar)"/><text x="{X(0.27)}" y="{jy+0.15*k+40}" text-anchor="middle" font-size="11">0.3 m overlap</text>')
lab(X(0.05), jy - 0.15 * k, X(0.0), jy - 0.15 * k - 30, ['segment n (CFRP)'], 'start')
lab(X(0.6), jy - 0.15 * k, X(0.55), jy - 0.15 * k - 30, ['segment n+1'], 'start')
lab(X(0.27), jy - 0.05 * k, X(0.80), jy - 0.10 * k, ['bonded Ti spigot', 'carries the bending'])
lab(X(0.65), jy, X(0.80), jy + 0.02 * k, ['steel cord ~1 kN', '(anti-rattle only)'])
lab(X(0.40) + 18, jy - 0.15 * k - 8, X(0.80), jy - 0.18 * k - 20, ['captive latch'])
lab(X(0.20) + 5, jy + 0.15 * k + 8, X(0.80), jy + 0.13 * k, ['alignment key'])

# ================= C. end hinge =================
A('<text x="380" y="420" class="t">C. End fitting: hinge for the swing, sphere for misalignment</text>')
hx, hy = 520, 560
A(f'<rect x="{hx-110}" y="{hy-60}" width="40" height="120" fill="{TI}" opacity="0.6" class="s"/><rect x="{hx+70}" y="{hy-60}" width="40" height="120" fill="{TI}" opacity="0.6" class="s"/>')
A(f'<rect x="{hx-60}" y="{hy-40}" width="120" height="80" fill="{TI}" class="s"/><circle cx="{hx}" cy="{hy}" r="30" fill="#ddd" stroke="#222"/>')
A(f'<rect x="{hx-130}" y="{hy-10}" width="260" height="20" fill="{PIN}" class="s"/>')
A(f'<path d="M{hx-40} {hy+40} L{hx-60} {hy+150} M{hx+40} {hy+40} L{hx+60} {hy+150}" stroke="{CF}" stroke-width="10"/>')
lab(hx - 90, hy - 60, hx - 160, hy - 90, ['clevis on the torque bracket', '(top) or the foot frame (foot)'], 'end')
lab(hx + 120, hy, hx + 150, hy - 70, ['hinge pin, tangential axis:', 'the ~53° erection swing', 'MoS₂ pin, polyimide-lined bore'])
lab(hx + 22, hy + 20, hx + 150, hy + 20, ['spherical bushing ±5°:', 'misalignment only'])
lab(hx + 55, hy + 120, hx + 150, hy + 110, ['tube end (CFRP)'])

# ================= D. foot pad section =================
A('<text x="880" y="30" class="t">D. Foot pad and frame (section)</text>')
fk, fx, fy = 190, 1090, 400
A(f'<rect x="{fx-1.1*fk}" y="{fy}" width="{2.2*fk}" height="70" fill="url(#g)"/>')
pw = 1.2 * fk
cd = 0.25 * fk * tan(radians(60)) * 0.35
A(f'<path d="M{fx-pw/2} {fy} H{fx-0.25*fk} L{fx} {fy+cd} L{fx+0.25*fk} {fy} H{fx+pw/2} V{fy+0.3*fk} H{fx-pw/2} Z" fill="url(#sn)" class="s"/>')
A(f'<path d="M{fx-0.24*fk} {fy-2} L{fx} {fy+cd-4} L{fx+0.24*fk} {fy-2} Z" fill="{TI}" class="s"/>')
A(f'<rect x="{fx-0.45*fk}" y="{fy-34}" width="{0.9*fk}" height="32" fill="{TI}" opacity="0.8" class="s"/>')
for dx in (-0.4, 0.4):
    A(f'<rect x="{fx+dx*fk-4}" y="{fy-6}" width="8" height="10" fill="#555"/>')
hxj, hyj = fx - 0.25 * fk, fy - 48
A(f'<circle cx="{hxj}" cy="{hyj}" r="10" fill="{PIN}" class="s"/>')
A(f'<line x1="{hxj}" y1="{hyj}" x2="{hxj-150}" y2="{hyj-200}" stroke="{CF}" stroke-width="11"/>')
dxs, dys = fx + 0.12 * fk, fy - 58
A(f'<circle cx="{dxs}" cy="{dys}" r="18" fill="#bbb" class="s"/><rect x="{dxs+20}" y="{dys-10}" width="34" height="20" fill="#7fa3d6" class="s"/>')
A(f'<line x1="{dxs-12}" y1="{dys-12}" x2="{dxs-12-100}" y2="{dys-12-215}" stroke="{STAY}" stroke-width="3"/>')
A(f'<rect x="{fx-0.62*fk}" y="{fy-26}" width="22" height="20" fill="#bbb" class="s"/><line x1="{fx-0.62*fk}" y1="{fy-16}" x2="{fx-1.1*fk}" y2="{fy-16}" stroke="{TIE}" stroke-width="3"/>')
A(f'<rect x="{fx+0.22*fk}" y="{fy-30}" width="26" height="22" fill="#f2c94c" class="s"/>')
A(f'<path d="M{fx-0.55*fk} {fy+80} h{0.5*fk} M{fx-0.55*fk+10} {fy+80} v-8 M{fx-0.05*fk-10} {fy+80} v-8" stroke="#888" stroke-width="3" stroke-dasharray="6 3"/>')
def num(n, x, y, px, py):
    A(f'<path d="M{px:.0f} {py:.0f}L{x:.0f} {y:.0f}" class="l"/><circle cx="{px:.0f}" cy="{py:.0f}" r="2" fill="#222"/>'
      f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="#fff" stroke="#222"/><text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-size="10.5" font-weight="bold" style="stroke:none">{n}</text>')
pts = [((hxj - 90, hyj - 120), (920, 140)), ((dxs - 70, dys - 160), (1010, 90)), ((hxj, hyj), (920, 300)),
       ((dxs, dys), (1230, 220)), ((fx + 0.22 * fk + 26, fy - 20), (1240, 300)), ((fx - 0.62 * fk, fy - 16), (920, 360)),
       ((fx + 0.4 * fk, fy - 2), (1240, 360)), ((fx, fy + cd / 2), (1240, 420)), ((fx + 0.5 * fk, fy + 0.25 * fk), (1240, 470)),
       ((fx - 0.3 * fk, fy + 80), (920, 470))]
for n, (p_, q_) in enumerate(pts, 1):
    num(n, q_[0], q_[1], p_[0], p_[1])
keyD = ['A-frame strut (53°)', 'Stay (65°)', 'Y-fitting hinge', 'Stay tensioner (worm drum)', 'Servo box + base cable',
        'Tie tensioner → centre', '3 levelling screws, shims', '30° cone in sintered socket', 'Pad 1.2 x 1.2 x 0.3 m', 'Erection sled (removed)']
for j, t in enumerate(keyD):
    col, row = divmod(j, 5)
    x0 = 880 + col * 205
    y0 = 520 + row * 22
    A(f'<circle cx="{x0}" cy="{y0}" r="9" fill="#fff" stroke="#222"/><text x="{x0}" y="{y0+4}" text-anchor="middle" font-size="10.5" font-weight="bold" style="stroke:none">{j+1}</text>')
    A(f'<text x="{x0+14}" y="{y0+4}" font-size="11">{t}</text>')

# ================= E. numbers =================
ex, ey = 880, 690
A(f'<text x="{ex}" y="{ey}" class="t">E. Numbers (strut_foot_check.py)</text>')
for j, t in enumerate(['Per tube: 1.25 kN, 0.7 MPa; buckling 9.2 kN with joints: margin 7.4',
                       'Sag 86 mm + Sun bow 44 mm, amplified to ~150 mm; ~6 MPa',
                       'First bending mode ~0.6 Hz',
                       'Erection (flat): 1.3 kN·m at midspan → 6.4 kN spigot couple',
                       'Pad: 0.64 kN down (0.44 kPa); friction 0.32 kN &lt; quake ~0.4 kN',
                       '→ cone in a socket: ~1.2 kN sideways',
                       'Sled drag ~0.13 kN during the scissor erection']):
    A(f'<text x="{ex}" y="{ey+22+j*18}" font-size="11.5">{t}</text>')
A('</svg>')
open('strut-foot.svg', 'w').write('\n'.join(o))
