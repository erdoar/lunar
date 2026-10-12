"""Materials board: every library material on a tilted swatch under a studio key light, labelled.

Run: python3 material_board.py   (writes ../renders/materials_board.jpg)
"""
import os
import sys
from math import radians

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import numpy as np
import bpy
from mathutils import Vector
from PIL import Image, ImageDraw, ImageFont
import materials
from meshes import MB

COLS, CELL, PX = 6, 1.2, 300
OUT = os.path.join(HERE, '..', 'renders', 'materials_board.jpg')


def main():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    sc.render.engine = 'CYCLES'
    sc.cycles.device = 'CPU'
    sc.cycles.samples = 48
    sc.cycles.use_denoising = True
    sc.view_settings.view_transform = 'Filmic'
    mats = materials.library()
    names = [n for n in mats if n != 'earth']
    rows = (len(names) + COLS - 1) // COLS
    mb = MB()
    tilt = radians(35)
    ax = (np.array([1.0, 0, 0]), np.array([0, np.cos(tilt), np.sin(tilt)]), np.array([0, -np.sin(tilt), np.cos(tilt)]))
    for i, n in enumerate(names):
        cx, cy = (i % COLS) * CELL, -(i // COLS) * CELL
        mb.box((cx, cy, 0), 0.45, 0.45, 0.04, i, ax)
        mb.tube((cx + 0.3, cy - 0.32, 0.12), (cx + 0.3, cy - 0.32, 0.36), 0.09, i, n=24, caps=True)
    mb.build('swatches', [mats[n] for n in names])
    w = bpy.data.worlds.new('studio')
    sc.world = w
    w.node_tree.nodes['Background'].inputs['Color'].default_value = (0.02, 0.02, 0.025, 1)
    w.node_tree.nodes['Background'].inputs['Strength'].default_value = 1.0
    key = bpy.data.lights.new('key', 'SUN'); key.energy = 3.5; key.angle = radians(2)
    ko = bpy.data.objects.new('key', key); sc.collection.objects.link(ko)
    ko.rotation_euler = (radians(50), radians(-20), radians(-30))
    cam = bpy.data.cameras.new('cam'); cam.type = 'ORTHO'
    co = bpy.data.objects.new('cam', cam); sc.collection.objects.link(co)
    W, H = COLS * CELL, rows * CELL
    cam.ortho_scale = max(W, H)
    co.location = ((COLS - 1) * CELL / 2, -(rows - 1) * CELL / 2, 20)
    sc.camera = co
    sc.render.resolution_x, sc.render.resolution_y = int(COLS * PX), int(rows * PX)
    tmp = '/tmp/materials_board.png'
    sc.render.filepath = tmp
    bpy.ops.render.render(write_still=True)
    im = Image.open(tmp).convert('RGB')
    d = ImageDraw.Draw(im)
    try:
        font = ImageFont.truetype('DejaVuSans.ttf', 18)
    except OSError:
        font = ImageFont.load_default()
    for i, n in enumerate(names):
        x, y = (i % COLS) * PX + 10, (i // COLS) * PX + PX - 30
        d.text((x, y), n, fill=(235, 235, 235), font=font)
    im.save(OUT, quality=90)
    print('wrote', OUT)


if __name__ == '__main__':
    main()
