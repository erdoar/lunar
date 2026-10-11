# Generates base.svg (rev 20): single base bearing, drive, foundation and rotating base frame. Run: python3 make_base_svg.py
o = []
A = o.append
W, H = 1240, 760
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="12">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><pattern id="g" width="8" height="8" patternUnits="userSpaceOnUse"><path d="M0 8L8 0" stroke="#a08c6c"/></pattern>'
  '<pattern id="gr" width="6" height="6" patternUnits="userSpaceOnUse"><path d="M0 0H6M0 0V6" stroke="#9aa" stroke-width="0.8"/></pattern>'
  '<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker></defs>')
A('<style>.s{stroke:#222;stroke-width:1.5}.l{stroke:#555;stroke-width:1;fill:none}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:15px;font-weight:bold}</style>')
ROT, FIX = '#e67e22', '#7d8790'
k, cx, gy = 190, 490, 640
X = lambda m: cx + m * k
Z = lambda m: gy - m * k


def lab(x1, y1, x2, y2, lines, anchor='start'):
    A(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" class="l"/>')
    for j, t in enumerate(lines):
        A(f'<text x="{x2+(4 if anchor=="start" else -4):.0f}" y="{y2+4+j*14:.0f}" text-anchor="{anchor}">{t}</text>')


A('<text x="20" y="30" class="t">Section through the base (rev 20): fixed parts grey, turning parts orange</text>')
A(f'<rect x="{X(-2.2)}" y="{gy}" width="{4.4*k}" height="60" fill="url(#g)"/><line x1="{X(-2.2)}" y1="{gy}" x2="{X(2.2)}" y2="{gy}" stroke="#222"/>')
# pad + foundation frame
A(f'<rect x="{X(-1.0)}" y="{gy}" width="{2.0*k}" height="18" fill="#c9b79c" stroke="#222"/>')
A(f'<path d="M{X(-1.0)} {Z(0)} L{X(-0.45)} {Z(0.55)} H{X(0.45)} L{X(1.0)} {Z(0)} Z" fill="{FIX}" opacity="0.85" class="s"/>')
# tie lugs + ties
for sx in (-1, 1):
    A(f'<circle cx="{X(sx*0.9)}" cy="{Z(0.06)}" r="6" fill="#fff" class="s"/>')
    A(f'<line x1="{X(sx*0.9)}" y1="{Z(0.06)}" x2="{X(sx*2.2)}" y2="{Z(0.06)}" stroke="#c87f0a" stroke-width="2" stroke-dasharray="6 3" marker-end="url(#ar)"/>')
# spherical seat + cartridge housing (fixed)
A(f'<path d="M{X(-0.42)} {Z(0.55)} A{0.6*k} {0.25*k} 0 0 0 {X(0.42)} {Z(0.55)}" fill="#bbb" class="s"/>')
A(f'<rect x="{X(-0.42)}" y="{Z(0.95)}" width="{0.84*k}" height="{0.4*k}" fill="{FIX}" class="s"/>')
# plain sleeve (second path) + outer race (fixed during normal running) + rollers + inner race (turning, internal gear)
A(f'<rect x="{X(-0.36)}" y="{Z(0.92)}" width="{0.72*k}" height="{0.07*k}" fill="#e8d8a8" stroke="#222"/>')
A(f'<rect x="{X(-0.36)}" y="{Z(0.85)}" width="{0.72*k}" height="{0.12*k}" fill="#aab" stroke="#222"/>')
for i in range(7):
    A(f'<rect x="{X(-0.3+i*0.1)-5}" y="{Z(0.80)-5}" width="10" height="10" fill="#666" transform="rotate(45 {X(-0.3+i*0.1)} {Z(0.80)})"/>')
A(f'<rect x="{X(-0.33)}" y="{Z(0.75)}" width="{0.66*k}" height="{0.07*k}" fill="{ROT}" stroke="#222"/>')
# slip ring through the hollow centre
A(f'<rect x="{X(-0.08)}" y="{Z(1.25)}" width="{0.16*k}" height="{0.8*k}" fill="#bfa6d9" class="s"/>')
# worm drives + pinions
for sx in (-1, 1):
    A(f'<rect x="{X(sx*0.75)-30}" y="{Z(0.95)}" width="60" height="44" fill="#7fa3d6" class="s"/>')
    A(f'<line x1="{X(sx*0.75)}" y1="{Z(0.95)}" x2="{X(sx*0.75)}" y2="{Z(0.55)}" stroke="#555" stroke-width="4"/>')
    A(f'<circle cx="{X(sx*0.36)}" cy="{Z(0.73)}" r="9" fill="#ddd" class="s"/>')
    A(f'<line x1="{X(sx*0.36)}" y1="{Z(0.73)}" x2="{X(sx*0.68)}" y2="{Z(0.85)}" stroke="#555" stroke-width="3"/>')
# mast foot plate + bottom mast section (turning)
A(f'<rect x="{X(-0.45)}" y="{Z(1.02)}" width="{0.9*k}" height="{0.07*k}" fill="{ROT}" class="s"/>')
A(f'<rect x="{X(-0.7)}" y="{Z(2.9)}" width="{1.4*k}" height="{1.88*k}" fill="none" stroke="{ROT}" stroke-width="4"/>')
for z in (1.3, 1.9):
    A(f'<line x1="{X(-0.7)}" y1="{Z(z)}" x2="{X(0.7)}" y2="{Z(z+0.6)}" stroke="{ROT}" stroke-width="1.5"/>')
A(f'<path d="M{X(-0.45)} {Z(1.09)} L{X(-0.7)} {Z(1.3)} M{X(0.45)} {Z(1.09)} L{X(0.7)} {Z(1.3)}" stroke="{ROT}" stroke-width="4"/>')
# rotating base frame at 1.5 m with winch + power, grating, brush skirt
A(f'<rect x="{X(-1.5)}" y="{Z(1.5)}" width="{3.0*k}" height="10" fill="url(#gr)" stroke="{ROT}" stroke-width="2"/>')
A(f'<rect x="{X(0.85)}" y="{Z(1.5)-48}" width="80" height="48" fill="#7fa3d6" class="s"/><text x="{X(0.85)+40}" y="{Z(1.5)-20}" text-anchor="middle" font-size="11" style="stroke:none" fill="#fff">winch</text>')
A(f'<rect x="{X(-1.35)}" y="{Z(1.5)-40}" width="70" height="40" fill="#bfa6d9" class="s"/><text x="{X(-1.35)+35}" y="{Z(1.5)-16}" text-anchor="middle" font-size="11" style="stroke:none">power</text>')
for sx in (-1, 1):
    A(f'<line x1="{X(sx*1.5)}" y1="{Z(1.47)}" x2="{X(sx*1.5)}" y2="{Z(1.0)}" stroke="#999" stroke-width="3" stroke-dasharray="3 2"/>')
    A(f'<line x1="{X(sx*0.7)}" y1="{Z(1.5)}" x2="{X(sx*1.2)}" y2="{Z(1.25)}" stroke="{ROT}" stroke-width="2"/>')
# jack frame (fixed, stays)
A(f'<rect x="{X(-1.25)}" y="{Z(2.4)}" width="{2.5*k}" height="{1.85*k}" fill="none" stroke="#2e7d32" stroke-width="2" stroke-dasharray="7 4"/>')
# halyard entry
A(f'<path d="M{X(0.95)} {Z(1.5)-48} L{X(0.7)} {Z(2.0)} L{X(0)} {Z(2.2)} V{Z(2.9)}" fill="none" stroke="#c0392b" stroke-width="2"/>')
A(f'<circle cx="{X(0.7)}" cy="{Z(2.0)}" r="5" fill="#fff" class="s"/>')
# labels (left / right)
lab(X(-0.42), Z(0.4), X(-1.6), Z(0.55), ['Spherical seat (±1°)'], 'end')
lab(X(-0.9), Z(0.2), X(-1.6), Z(0.25), ['Foundation frame on a', '~2 x 2 m sintered pad'], 'end')
lab(X(-0.9), Z(0.06), X(-1.6), Z(-0.08), ['Tie lugs: 3 ground ties', 'from the strut feet'], 'end')
lab(X(-0.1), Z(1.0), X(-1.6), Z(1.0), ['Slip ring / rotary transformer', 'through the hollow centre'], 'end')
lab(X(-0.75), Z(0.95), X(-1.6), Z(0.8), ['Worm-drive motor (x2),', 'self-locking, slip clutch'], 'end')
lab(X(-1.35), Z(1.6), X(-1.6), Z(1.75), ['Rotating base frame Ø3 m', '(grating walkway)'], 'end')
lab(X(-1.25), Z(2.3), X(-1.6), Z(2.35), ['Jack frame: erection,', 'then bearing swaps'], 'end')
lab(X(0.36), Z(0.8), X(1.6), Z(0.95), ['Crossed-roller ring Ø0.6 m:', 'turning inner race + gear (orange),', 'rollers, outer race'])
lab(X(0.36), Z(0.89), X(1.6), Z(0.6), ['Plain sleeve: 2nd rotation path'])
lab(X(0.45), Z(1.05), X(1.6), Z(1.3), ['Mast foot plate on the', 'rotating race (~9.9 kN)'])
lab(X(0.7), Z(2.0), X(1.6), Z(2.1), ['Halyards enter the mast via', 'a side window + deflection sheave'])
lab(X(1.5), Z(1.2), X(1.6), Z(1.55), ['Brush skirt over the bearing'])
lab(X(0.7), Z(2.7), X(1.6), Z(2.75), ['Bottom mast section (turns)'])
# right info column
ix = 1010
A(f'<text x="{ix}" y="70" font-weight="bold">Numbers</text>')
info = ['Load on the bearing ~9.9 kN', '(ring rated well over 100 kN)', 'Running torque ~35 N·m', '(bearing ~15 + collars ~20)', 'Slip clutch ~250 N·m;',
        'collar interlock ~200 N·m', 'Pad pressure ~2.5 kPa', 'Bearing ~1 m above regolith', '', 'Bearing swap: jack frame lifts',
        'the mast ~10 mm; cartridge', 'slides out on rails; ~1 shift']
for j, t in enumerate(info):
    A(f'<text x="{ix}" y="{92+j*16}" font-size="12">{t}</text>')
A('</svg>')
open('base.svg', 'w').write('\n'.join(o))
