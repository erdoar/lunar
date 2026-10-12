"""Mesh builder: accumulates tubes, boxes and custom geometry with UVs in metres and per-face material slots,
then emits one Blender object. Thousands of members become a handful of objects, which keeps Cycles fast.
"""
import numpy as np
import bpy


def _frame(d):
    """Two unit vectors perpendicular to direction d."""
    d = d / np.linalg.norm(d)
    a = np.array([0, 0, 1.0]) if abs(d[2]) < 0.9 else np.array([1.0, 0, 0])
    u = np.cross(d, a); u /= np.linalg.norm(u)
    return u, np.cross(d, u)


class MB:
    def __init__(self):
        self.v, self.f, self.uv, self.mat, self.smooth = [], [], [], [], []
        self.nv = 0

    def add(self, verts, faces, uvs, mat, smooth=False):
        """verts (n,3); faces list of index tuples (local); uvs list of per-loop (u,v) tuples matching faces."""
        verts = np.asarray(verts, float)
        self.v.append(verts)
        for fc, fu in zip(faces, uvs):
            self.f.append([i + self.nv for i in fc])
            self.uv.append(fu)
            self.mat.append(mat)
            self.smooth.append(smooth)
        self.nv += len(verts)

    def tube(self, a, b, r, mat, n=8, caps=False, r2=None):
        a, b = np.asarray(a, float), np.asarray(b, float)
        d = b - a
        L = np.linalg.norm(d)
        if L < 1e-6:
            return
        u, w = _frame(d)
        r2 = r if r2 is None else r2
        ang = np.linspace(0, 2 * np.pi, n, endpoint=False)
        ring = np.cos(ang)[:, None] * u + np.sin(ang)[:, None] * w
        verts = np.vstack([a + r * ring, b + r2 * ring])
        faces, uvs = [], []
        circ = 2 * np.pi * r
        for i in range(n):
            j = (i + 1) % n
            faces.append((i, j, n + j, n + i))
            u0, u1 = circ * i / n, circ * (i + 1) / n
            uvs.append(((u0, 0), (u1, 0), (u1, L), (u0, L)))
        if caps:
            faces.append(tuple(range(n - 1, -1, -1)))
            uvs.append(tuple((r * np.cos(t), r * np.sin(t)) for t in ang[::-1]))
            faces.append(tuple(range(n, 2 * n)))
            uvs.append(tuple((r * np.cos(t), r * np.sin(t)) for t in ang))
        self.add(verts, faces, uvs, mat, smooth=True)

    def box(self, c, hx, hy, hz, mat, ax=None):
        """Box centred at c with half extents along local axes ax = (ex, ey, ez) (default world axes)."""
        c = np.asarray(c, float)
        ex, ey, ez = (np.eye(3) if ax is None else [np.asarray(e, float) / np.linalg.norm(e) for e in ax])
        verts = np.array([c + sx * hx * ex + sy * hy * ey + sz * hz * ez
                          for sz in (-1, 1) for sy in (-1, 1) for sx in (-1, 1)])
        faces = [(0, 2, 3, 1), (4, 5, 7, 6), (0, 1, 5, 4), (2, 6, 7, 3), (0, 4, 6, 2), (1, 3, 7, 5)]
        X, Y, Z = 2 * hx, 2 * hy, 2 * hz
        uvs = [((0, 0), (0, Y), (X, Y), (X, 0)), ((0, 0), (X, 0), (X, Y), (0, Y)),
               ((0, 0), (X, 0), (X, Z), (0, Z)), ((0, 0), (0, Z), (X, Z), (X, 0)),
               ((0, 0), (0, Z), (Y, Z), (Y, 0)), ((0, 0), (Y, 0), (Y, Z), (0, Z))]
        self.add(verts, faces, uvs, mat)

    def box_between(self, a, b, hw, hh, mat, up=(0, 0, 1)):
        """Rectangular bar from a to b, half width hw, half height hh (height axis nearest to `up`)."""
        a, b = np.asarray(a, float), np.asarray(b, float)
        d = b - a
        L = np.linalg.norm(d)
        ex = d / L
        upv = np.asarray(up, float)
        ez = upv - ex * np.dot(upv, ex)
        if np.linalg.norm(ez) < 1e-6:
            ez = np.array([1.0, 0, 0]) - ex * ex[0]
        ez /= np.linalg.norm(ez)
        ey = np.cross(ez, ex)
        self.box((a + b) / 2, L / 2, hw, hh, mat, (ex, ey, ez))

    def ring(self, c, r_in, r_out, z0, z1, mat, n=48):
        """Annular ring (rectangular section) about the vertical axis through c."""
        c = np.asarray(c, float)
        ang = np.linspace(0, 2 * np.pi, n, endpoint=False)
        cs, sn = np.cos(ang), np.sin(ang)
        verts = []
        for r, z in ((r_in, z0), (r_out, z0), (r_out, z1), (r_in, z1)):
            verts += [c + (r * a, r * b, z) for a, b in zip(cs, sn)]
        faces, uvs = [], []
        for k in range(4):
            for i in range(n):
                j = (i + 1) % n
                p = k * n
                q = ((k + 1) % 4) * n
                faces.append((p + i, p + j, q + j, q + i))
                s0, s1 = 2 * np.pi * r_out * i / n, 2 * np.pi * r_out * (i + 1) / n
                uvs.append(((s0, 0), (s1, 0), (s1, 0.3), (s0, 0.3)))
        self.add(np.array(verts), faces, uvs, mat)

    def sphere(self, c, r, mat, n=12):
        c = np.asarray(c, float)
        verts, faces, uvs = [], [], []
        for i in range(n // 2 + 1):
            th = np.pi * i / (n // 2)
            for j in range(n):
                ph = 2 * np.pi * j / n
                verts.append(c + r * np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)]))
        for i in range(n // 2):
            for j in range(n):
                a, b = i * n + j, i * n + (j + 1) % n
                faces.append((a, a + n, b + n, b))
                uvs.append(((j, i), (j, i + 1), (j + 1, i + 1), (j + 1, i)))
        self.add(np.array(verts), faces, uvs, mat, smooth=True)

    def grid(self, verts, nx, ny, uvs_v, mat, smooth=True):
        """Regular grid of (ny, nx) vertices given flat; uvs_v (n,2) per vertex."""
        faces, uvs = [], []
        for j in range(ny - 1):
            for i in range(nx - 1):
                a = j * nx + i
                q = (a, a + 1, a + nx + 1, a + nx)
                faces.append(q)
                uvs.append(tuple(tuple(uvs_v[k]) for k in q))
        self.add(verts, faces, uvs, mat, smooth)

    def build(self, name, materials, collection=None):
        verts = np.vstack(self.v) if self.v else np.zeros((0, 3))
        me = bpy.data.meshes.new(name)
        me.from_pydata(verts.tolist(), [], self.f)
        me.update()
        uvl = me.uv_layers.new(name='UVMap')
        flat = [uv for fu in self.uv for uv in fu]
        uvl.data.foreach_set('uv', np.asarray(flat, float).ravel())
        me.polygons.foreach_set('material_index', self.mat)
        me.polygons.foreach_set('use_smooth', self.smooth)
        for m in materials:
            me.materials.append(m)
        ob = bpy.data.objects.new(name, me)
        (collection or bpy.context.scene.collection).objects.link(ob)
        return ob


def fast_grid_object(name, X, Y, Z, material, uv_scale=1.0, collection=None, mask=None):
    """Large heightfield as one object built with foreach_set (fast for 10^5+ verts).

    X, Y, Z: (ny, nx) arrays. mask: optional (ny-1, nx-1) bool to drop faces.
    """
    ny, nx = Z.shape
    verts = np.column_stack([X.ravel(), Y.ravel(), Z.ravel()])
    idx = np.arange(ny * nx).reshape(ny, nx)
    q = np.stack([idx[:-1, :-1], idx[:-1, 1:], idx[1:, 1:], idx[1:, :-1]], -1).reshape(-1, 4)
    if mask is not None:
        q = q[~mask.ravel()]
    me = bpy.data.meshes.new(name)
    me.vertices.add(len(verts))
    me.vertices.foreach_set('co', verts.astype(np.float32).ravel())
    me.loops.add(q.size)
    me.loops.foreach_set('vertex_index', q.ravel())
    me.polygons.add(len(q))
    me.polygons.foreach_set('loop_start', np.arange(0, q.size, 4))
    me.update(calc_edges=True)
    uv = me.uv_layers.new(name='UVMap')
    uv.data.foreach_set('uv', (verts[q.ravel(), :2] * uv_scale).astype(np.float32).ravel())
    me.polygons.foreach_set('use_smooth', np.ones(len(q), bool))
    me.materials.append(material)
    ob = bpy.data.objects.new(name, me)
    (collection or bpy.context.scene.collection).objects.link(ob)
    return ob
