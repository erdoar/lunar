"""Build the scene and render the vanity shots with Cycles.

Run (from this folder):
  python3 render_all.py                       # all shots, final quality, into ../renders/
  python3 render_all.py --preview 03 05       # quick low-res check of chosen shots
Needs: pip install bpy (Blender as a Python module), numpy, pillow. Run textures.py first.
"""
import argparse
import os
import sys
import time
from math import radians, atan2, hypot, degrees

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import numpy as np
import bpy
from mathutils import Vector
import params as P
import materials
import rig
import environment as env
from shots import SHOTS, around

OUT = os.path.join(HERE, '..', 'renders')


def setup(samples):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    sc.render.engine = 'CYCLES'
    sc.cycles.device = 'CPU'
    sc.cycles.samples = samples
    sc.cycles.use_adaptive_sampling = True
    sc.cycles.use_denoising = True
    sc.cycles.denoiser = 'OPENIMAGEDENOISE'
    sc.cycles.max_bounces = 4
    sc.cycles.diffuse_bounces = 2
    sc.cycles.glossy_bounces = 3
    sc.cycles.transparent_max_bounces = 8
    sc.view_settings.view_transform = 'Filmic'
    sc.view_settings.look = 'Medium High Contrast'
    sc.render.image_settings.file_format = 'JPEG'
    sc.render.image_settings.quality = 90
    return sc


def build_scene():
    t = time.time()
    mats = materials.library()
    rig.build(mats)
    env.terrain(mats)
    env.rocks(mats)
    env.sky(mats)
    print(f'scene built in {time.time()-t:.0f} s')


def camera(sc, shot):
    cam = bpy.data.cameras.new(shot['name'])
    ob = bpy.data.objects.new(shot['name'], cam)
    sc.collection.objects.link(ob)
    cam.clip_start, cam.clip_end = 0.05, 400e3
    tgt = Vector(shot['target'])
    if 'pos' in shot:
        pos = list(shot['pos'])
    else:
        pos = list(around(shot['target'], shot['az'], shot['el'] or 0, shot.get('dist', 300)))
    if shot.get('ortho'):
        cam.type = 'ORTHO'
        cam.ortho_scale = shot['scale']
        d = Vector(pos) - tgt
        pos = list(tgt + d.normalized() * 3000)
    else:
        cam.lens = shot.get('lens', 35)
    if shot.get('ground'):
        pos[2] = float(env.height(np.array([pos[0]]), np.array([pos[1]]))[0]) + shot.get('eye', 1.7)
    ob.location = pos
    aim = Vector(shot.get('aim', shot['target']))
    ob.rotation_euler = (aim - Vector(pos)).to_track_quat('-Z', 'Y').to_euler()
    sc.camera = ob
    return ob


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('shots', nargs='*', help='shot name prefixes (default: all)')
    ap.add_argument('--preview', action='store_true')
    ap.add_argument('--samples', type=int, default=128)
    a = ap.parse_args()
    sc = setup(16 if a.preview else a.samples)
    build_scene()
    os.makedirs(OUT, exist_ok=True)
    for shot in SHOTS:
        if a.shots and not any(shot['name'].startswith(s) for s in a.shots):
            continue
        camera(sc, shot)
        w, h = shot['res']
        f = 0.35 if a.preview else 1.0
        sc.render.resolution_x, sc.render.resolution_y = int(w * f), int(h * f)
        sc.view_settings.exposure = shot.get('exposure', 0.0)
        sc.render.filepath = os.path.join(OUT if not a.preview else '/tmp/claude-0/prev', shot['name'] + '.jpg')
        t = time.time()
        bpy.ops.render.render(write_still=True)
        print(f"{shot['name']}: {time.time()-t:.0f} s", flush=True)


if __name__ == '__main__':
    main()
