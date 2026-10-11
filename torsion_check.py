# Rough torsional ("wind-up") stiffness of the stationary collars about the mast axis.
# Energy method: members modelled as axial springs with pre-tension; rigid arms and collar.
# Run: python3 torsion_check.py
import numpy as np
EA_wire = 100e9*18e-6      # 6 mm rope, ~18 mm2 metallic
EA_strut = 100e9*(np.pi*0.3*0.002)   # CFRP tube
def k_theta(members, h=1e-5):
    """members: list of (collar_point_fn(theta), ground_point, EA, pretension(+tension/-compression))"""
    def energy(th):
        U=0
        for P,G,EA,T0 in members:
            L0=np.linalg.norm(P(0)-G); L=np.linalg.norm(P(th)-G)
            d=L-L0
            U+=T0*d+0.5*EA/L0*d*d
        return U
    return (energy(h)-2*energy(0)+energy(-h))/h**2
def rot(p,th):
    c,s=np.cos(th),np.sin(th); return np.array([c*p[0]-s*p[1],s*p[0]+c*p[1],p[2]])
def feet(R=30): return [np.array([R*np.cos(a),R*np.sin(a),0]) for a in np.radians([90,210,330])]
F=feet()
def upper(a_half, r_c=1.45, T=1500):
    m=[]
    for f in F:
        u=f[:2]/np.linalg.norm(f[:2]); t=np.array([-u[1],u[0]])
        if a_half==0:
            pts=[np.r_[u*r_c,62]]; Tw=T
        else:
            pts=[np.r_[u*r_c+t*a_half,62],np.r_[u*r_c-t*a_half,62]]; Tw=T/2
        for p in pts:
            m.append((lambda th,p=p: rot(p,th), f, EA_wire*(2 if a_half==0 else 1), Tw))
    return k_theta(m)
def mid(b_half, r_c=1.45, C=2500):
    m=[]
    for f in F:
        u=f[:2]/np.linalg.norm(f[:2]); t=np.array([-u[1],u[0]])
        pts=[np.r_[u*r_c,35]] if b_half==0 else [np.r_[u*r_c+t*b_half,35],np.r_[u*r_c-t*b_half,35]]
        n=len(pts)
        for p in pts:
            m.append((lambda th,p=p: rot(p,th), f, EA_strut/n, -C/n))
    return k_theta(m)
for a in (0,3,6,8):
    print('upper collar, torque-arm half-length',a,'m: k =',round(upper(a)),'N.m/rad')
for b in (0,1.5,3):
    print('strut collar, A-frame half-width',b,'m: k =',round(mid(b)),'N.m/rad')
for M in (10,180,500):
    print('torque',M,'N.m -> twist deg: bare top',round(np.degrees(M/upper(0)),1),' top arms 6 m',round(np.degrees(M/upper(6)),3),' mid A-frame 3 m',round(np.degrees(M/mid(3)),3))

def gen(z, rc, a, EA, T, n_split):
    m=[]
    for f in F:
        u=f[:2]/np.linalg.norm(f[:2]); t=np.array([-u[1],u[0]])
        pts=[np.r_[u*rc+t*a,z],np.r_[u*rc-t*a,z]] if a>0 else [np.r_[u*rc,z]]
        for p in pts:
            m.append((lambda th,p=p: rot(p,th), f, EA/len(pts)*(2 if z==62 and a==0 else 1) if z==35 else EA*(2 if a==0 else 1), T/len(pts)))
    return k_theta(m)
print('--- clearance-limited geometries (tips within ~21 deg of plane)')
for rc,a in ((8,3),(7,2.5),(6,2)):
    k=gen(62,rc,a,EA_wire,1500,2); print('top arm to r',rc,'crossbar +/-',a,': k',round(k),'twist at 500 N.m deg',round(np.degrees(500/k),3),'tip az',round(np.degrees(np.arctan(a/rc)),1))
for rc,a in ((4,1.5),(3,1.2)):
    k=gen(35,rc,a,EA_strut,-2500,2); print('mid A-frame bracket r',rc,'+/-',a,': k',round(k),'tip az',round(np.degrees(np.arctan(a/rc)),1))
