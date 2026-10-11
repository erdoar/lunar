# Generates platform-layout.svg (plan + elevation). Run: python3 make_layout_svg.py
import math
o=[];A=o.append
W,H=1120,700
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="13">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker>'
  '<pattern id="g" width="8" height="8" patternUnits="userSpaceOnUse"><path d="M0 8L8 0" stroke="#a08c6c"/></pattern></defs>')
A('<style>.s{stroke:#222;stroke-width:2}.l{stroke:#555;stroke-width:1;fill:none}text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:17px;font-weight:bold}</style>')
cx,cy,k=330,360,11.5
A('<text x="30" y="34" class="t">Plan view (from above)</text>')
for R,n in((19,40),(21,44)):
    r=R*k
    A(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#c0392b" stroke-width="4"/>')
    for i in range(n):
        a=2*math.pi*i/n
        A(f'<line x1="{cx+(r-6)*math.cos(a):.1f}" y1="{cy+(r-6)*math.sin(a):.1f}" x2="{cx+(r+6)*math.cos(a):.1f}" y2="{cy+(r+6)*math.sin(a):.1f}" stroke="#222" stroke-width="1.2"/>')
A(f'<circle cx="{cx}" cy="{cy}" r="{20*k}" fill="none" stroke="#9fb4c7" stroke-width="{3*k}" opacity="0.45"/>')
for ring in(19,21):
    for i in range(12):
        d=i*30+(15 if ring==21 else 0)
        a=math.radians(d); x=cx+ring*k*math.cos(a); y=cy+ring*k*math.sin(a)
        col='#4a9' if ring==19 and d%90==0 else '#e0a040'
        A(f'<rect x="-7" y="-11" width="14" height="22" rx="3" fill="{col}" class="s" transform="translate({x:.1f},{y:.1f}) rotate({d})"/>')
for d in range(0,360,45):
    a=math.radians(d)
    A(f'<line x1="{cx}" y1="{cy}" x2="{cx+19*k*math.cos(a):.1f}" y2="{cy+19*k*math.sin(a):.1f}" stroke="#7d8fa0" stroke-width="3"/>')
w=18*k
for dy in(-26,18): A(f'<rect x="{cx-w}" y="{cy+dy}" width="{2*w}" height="8" fill="#2c4a7a" class="s"/>')
for i in range(12):
    x=cx-w+i*2*w/12
    A(f'<line x1="{x:.1f}" y1="{cy-18}" x2="{x+2*w/12:.1f}" y2="{cy+18}" stroke="#555"/>')
A(f'<circle cx="{cx}" cy="{cy}" r="13" fill="#fff" class="s"/><circle cx="{cx}" cy="{cy}" r="5" fill="#222"/>')
r=25*k
A(f'<path d="M{cx+r*math.cos(math.radians(-60)):.0f} {cy+r*math.sin(math.radians(-60)):.0f} A{r} {r} 0 0 1 {cx+r*math.cos(math.radians(-25)):.0f} {cy+r*math.sin(math.radians(-25)):.0f}" fill="none" stroke="#222" stroke-width="2" marker-end="url(#ar)"/>')
A(f'<text x="{cx+175}" y="{cy-255}">Rotates 1 rev / 29.5 days</text>')
A(f'<circle cx="{cx}" cy="48" r="14" fill="#f5b700" class="s"/><line x1="{cx}" y1="66" x2="{cx}" y2="{cy-36}" stroke="#f5b700" stroke-width="3" stroke-dasharray="8 5" marker-end="url(#ar)"/>')
A(f'<text x="{cx-22}" y="53" text-anchor="end">Sun on horizon, circles</text><text x="{cx-22}" y="68" text-anchor="end">once per lunar day</text>')
def lab(x1,y1,x2,y2,lines,anchor='start'):
    A(f'<path d="M{x1:.0f} {y1:.0f}L{x2} {y2}" class="l"/>')
    for j,t in enumerate(lines): A(f'<text x="{x2+(4 if anchor=="start" else -4)}" y="{y2+4+j*15}" text-anchor="{anchor}">{t}</text>')
lab(cx+60,cy-26,cx+60,cy-90,["Panel wall A"])
lab(cx+40,cy+26,cx+40,cy+90,["Panel wall B","(truss between walls)"])
lab(cx-9,cy+9,cx-60,cy+150,["Kingpin: slewing","bearing + slip ring"],'end')
a=math.radians(200); lab(cx+21*k*math.cos(a),cy+21*k*math.sin(a),20,cy+250,["Outer rail Ø42 m","44 x 3 m segments"])
a=math.radians(230); lab(cx+19*k*math.cos(a),cy+19*k*math.sin(a),20,cy-275,["Inner rail Ø38 m","40 x 3 m segments"])
L=H-22
A(f'<rect x="30" y="{L-12}" width="14" height="14" fill="#e0a040" class="s"/><text x="50" y="{L}">Load bogie (12 per rail)</text>')
A(f'<rect x="220" y="{L-12}" width="14" height="14" fill="#4a9" class="s"/><text x="240" y="{L}">Drive bogie (4, inner rail)</text>')
A(f'<line x1="420" y1="{L-5}" x2="446" y2="{L-5}" stroke="#c0392b" stroke-width="4"/><text x="452" y="{L}">Rail (ticks = segment joints)</text>')
ox,gy,e=715,600,8
A(f'<text x="{ox}" y="34" class="t">Elevation (facing the panels)</text>')
A(f'<rect x="{ox-15}" y="{gy}" width="{W-ox}" height="40" fill="url(#g)"/><line x1="{ox-15}" y1="{gy}" x2="{W}" y2="{gy}" class="s"/>')
mid=ox+21*e
for R in(-21,-19,19,21):
    x=mid+R*e
    A(f'<rect x="{x-3}" y="{gy-12}" width="6" height="12" fill="#ccc" class="s"/><rect x="{x-5}" y="{gy-17}" width="10" height="5" fill="#c0392b"/><rect x="{x-6}" y="{gy-28}" width="12" height="11" fill="#e0a040" class="s"/>')
dt=gy-48
A(f'<rect x="{mid-21*e}" y="{dt}" width="{42*e}" height="20" fill="#9fb4c7" class="s"/><rect x="{mid-8}" y="{dt+20}" width="16" height="28" fill="#fff" class="s"/>')
top=dt-30*e
A(f'<rect x="{mid-18*e}" y="{top}" width="{36*e}" height="{30*e}" fill="#2c4a7a" class="s"/>')
for i in range(1,6): A(f'<line x1="{mid-18*e}" y1="{top+i*5*e}" x2="{mid+18*e}" y2="{top+i*5*e}" stroke="#7fa3d6"/>')
for i in range(1,12): A(f'<line x1="{mid-18*e+i*3*e}" y1="{top}" x2="{mid-18*e+i*3*e}" y2="{dt}" stroke="#7fa3d6"/>')
A(f'<path d="M{mid-18*e} {top-14}H{mid+18*e}" class="l" marker-start="url(#ar)" marker-end="url(#ar)"/><text x="{mid}" y="{top-20}" text-anchor="middle">36 m</text>')
A(f'<path d="M{mid+21*e+14} {top}V{dt}" class="l" marker-start="url(#ar)" marker-end="url(#ar)"/><text x="{mid+21*e+20}" y="{(top+dt)/2}">30 m</text>')
A(f'<path d="M{mid-21*e} {gy+22}H{mid+21*e}" stroke="#222" marker-start="url(#ar)" marker-end="url(#ar)"/><rect x="{mid-30}" y="{gy+13}" width="60" height="18" fill="#fff"/><text x="{mid}" y="{gy+27}" text-anchor="middle">Ø42 m</text>')
hx=mid+21*e+22
A(f'<circle cx="{hx}" cy="{gy-17}" r="2.2" fill="#222"/><line x1="{hx}" y1="{gy-15}" x2="{hx}" y2="{gy-6}" stroke="#222" stroke-width="1.5"/><path d="M{hx-3} {gy}L{hx} {gy-6}L{hx+3} {gy}" stroke="#222" fill="none" stroke-width="1.5"/>')
A(f'<text x="{hx-30}" y="{gy+48}" font-size="11">2 m person</text>')
A(f'<path d="M{mid-21*e+6} {dt+30}L{ox-5} {dt-60}" class="l"/><text x="{ox}" y="{dt-66}" font-size="12">Bogies on raised rail</text>')
A(f'<text x="{ox}" y="{L}">Panels vertical: Sun is ~0–1.5° above horizon</text>')
A('</svg>')
open('platform-layout.svg','w').write('\n'.join(o))
