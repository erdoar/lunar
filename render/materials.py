"""Material library for the rig renders (Cycles, Principled BSDF).

Every mesh carries UVs in metres, so each texture's `scale` below is in repeats per metre.
"""
import os
from math import cos, sin
import bpy
import params as P

TEX = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'textures')

# name: (base colour, metallic, roughness, extras)
LIBRARY = {
    'regolith':      dict(color=(0.115, 0.11, 0.10), rough=1.0, diffuse_rough=1.0, spec=0.15, lommel=True,
                          albedo_tex=('regolith_albedo.png', 1 / 8), bump_tex=('regolith_bump.png', 1 / 8, 0.8, 0.12),
                          noise=(0.02, 0.35)),
    'regolith_pad':  dict(color=(0.085, 0.082, 0.078), rough=0.95, diffuse_rough=1.0, spec=0.2,
                          bump_tex=('regolith_bump.png', 1 / 2, 0.2)),
    'sintered':      dict(color=(0.07, 0.065, 0.06), rough=0.55, spec=0.45, bump_tex=('mli_bump.png', 2.0, 0.15)),
    'cfrp':          dict(color=(0.05, 0.05, 0.053), rough=0.38, coat=0.6, coat_rough=0.12,
                          color_tex=('cfrp_twill.png', 10.0), bump_tex=('cfrp_twill_bump.png', 10.0, 0.08)),
    'white_coat':    dict(color=(0.82, 0.82, 0.8), rough=0.5, spec=0.4),
    'rod_jacket':    dict(color=(0.86, 0.86, 0.84), rough=0.4, spec=0.5),
    'titanium':      dict(color=(0.58, 0.56, 0.53), metal=1.0, rough=0.3, aniso=0.5),
    'aluminium':     dict(color=(0.88, 0.88, 0.9), metal=1.0, rough=0.22),
    'steel':         dict(color=(0.42, 0.42, 0.43), metal=0.9, rough=0.45),
    'stainless':     dict(color=(0.75, 0.74, 0.72), metal=1.0, rough=0.25),
    'gold_mli':      dict(color=(1.0, 0.70, 0.30), metal=1.0, rough=0.16, bump_tex=('mli_bump.png', 3.0, 0.5)),
    'silver_mli':    dict(color=(0.92, 0.92, 0.94), metal=1.0, rough=0.14, bump_tex=('mli_bump.png', 3.0, 0.5)),
    'osr_radiator':  dict(color=(0.9, 0.92, 0.95), metal=0.85, rough=0.06, coat=1.0, coat_rough=0.02),
    'solar_cell':    dict(color=(1, 1, 1), rough=0.12, spec=0.6, coat=1.0, coat_rough=0.02,
                          color_tex=('solar_cell.png', (0.5, 1.0))),
    'kapton':        dict(color=(0.72, 0.36, 0.05), rough=0.3, spec=0.5, sheen=0.3),
    'pack_frame':    dict(color=(0.05, 0.05, 0.055), rough=0.45, coat=0.4),
    'radiator_black': dict(color=(0.02, 0.02, 0.022), rough=0.5),
    'safety_yellow': dict(color=(0.95, 0.62, 0.04), rough=0.4, spec=0.4),
    'grating':       dict(color=(0.8, 0.8, 0.82), metal=1.0, rough=0.35, alpha_tex=('grating_alpha.png', 1 / 0.3)),
    'collar_white':  dict(color=(0.78, 0.79, 0.8), rough=0.35, coat=0.3),
    'teal_anod':     dict(color=(0.08, 0.42, 0.40), metal=1.0, rough=0.3),
    'bot_shell':     dict(color=(0.86, 0.86, 0.84), rough=0.32, coat=0.5, coat_rough=0.1),
    'bot_joint':     dict(color=(0.04, 0.04, 0.045), rough=0.55),
    'visor':         dict(color=(1.0, 0.72, 0.28), metal=1.0, rough=0.04),
    'suit':          dict(color=(0.9, 0.9, 0.88), rough=0.75, sheen=0.4),
    'rope':          dict(color=(0.7, 0.7, 0.68), metal=1.0, rough=0.35),
    'red_light':     dict(color=(0.3, 0.0, 0.0), rough=0.4, emit=((1.0, 0.08, 0.04), 40.0)),
    'earth':         dict(color=(1, 1, 1), rough=0.75, spec=0.3, color_tex=('earth.png', 1.0), color_mult=0.22),
}


def _img(nodes, fname, colorspace='sRGB'):
    n = nodes.new('ShaderNodeTexImage')
    path = os.path.join(TEX, fname)
    img = bpy.data.images.get(fname) or bpy.data.images.load(path, check_existing=True)
    img.colorspace_settings.name = colorspace
    n.image = img
    return n


def _uv(nodes, links, scale):
    tc = nodes.new('ShaderNodeTexCoord')
    mp = nodes.new('ShaderNodeMapping')
    sc = scale if isinstance(scale, tuple) else (scale, scale)
    mp.inputs['Scale'].default_value = (sc[0], sc[1], 1)
    links.new(tc.outputs['UV'], mp.inputs['Vector'])
    return mp.outputs['Vector']


def _lommel(nodes, links, color_in):
    """Scale albedo by 0.5/(mu0 + mu): the Lommel-Seeliger law that makes regolith bright at grazing light
    and grazing view, unlike a Lambert surface. mu0 uses the scene's single Sun direction."""
    geo = nodes.new('ShaderNodeNewGeometry')
    sun = nodes.new('ShaderNodeCombineXYZ')
    sx, sy, sz = cos(P.SUN_EL) * cos(P.SUN_AZ), cos(P.SUN_EL) * sin(P.SUN_AZ), sin(P.SUN_EL)
    sun.inputs['X'].default_value, sun.inputs['Y'].default_value, sun.inputs['Z'].default_value = sx, sy, sz
    mu0 = nodes.new('ShaderNodeVectorMath'); mu0.operation = 'DOT_PRODUCT'
    links.new(geo.outputs['Normal'], mu0.inputs[0]); links.new(sun.outputs['Vector'], mu0.inputs[1])
    mu = nodes.new('ShaderNodeVectorMath'); mu.operation = 'DOT_PRODUCT'
    links.new(geo.outputs['Normal'], mu.inputs[0]); links.new(geo.outputs['Incoming'], mu.inputs[1])
    a = nodes.new('ShaderNodeMath'); a.operation = 'MAXIMUM'; a.inputs[1].default_value = 0.0
    links.new(mu0.outputs['Value'], a.inputs[0])
    b = nodes.new('ShaderNodeMath'); b.operation = 'MAXIMUM'; b.inputs[1].default_value = 0.0
    links.new(mu.outputs['Value'], b.inputs[0])
    add = nodes.new('ShaderNodeMath'); add.operation = 'ADD'
    links.new(a.outputs[0], add.inputs[0]); links.new(b.outputs[0], add.inputs[1])
    add2 = nodes.new('ShaderNodeMath'); add2.operation = 'ADD'; add2.inputs[1].default_value = 0.1
    links.new(add.outputs[0], add2.inputs[0])
    div = nodes.new('ShaderNodeMath'); div.operation = 'DIVIDE'; div.inputs[0].default_value = 0.35
    links.new(add2.outputs[0], div.inputs[1])
    mul = nodes.new('ShaderNodeMix'); mul.data_type = 'RGBA'; mul.blend_type = 'MULTIPLY'
    mul.inputs['Factor'].default_value = 1.0
    links.new(color_in, mul.inputs['A'])
    links.new(div.outputs[0], mul.inputs['B'])
    return mul.outputs['Result']


def make(name, spec):
    m = bpy.data.materials.new(name)
    nt = m.node_tree
    nodes, links = nt.nodes, nt.links
    bsdf = nodes['Principled BSDF']
    bsdf.inputs['Base Color'].default_value = (*spec['color'], 1)
    bsdf.inputs['Metallic'].default_value = spec.get('metal', 0.0)
    bsdf.inputs['Roughness'].default_value = spec.get('rough', 0.5)
    bsdf.inputs['Specular IOR Level'].default_value = spec.get('spec', 0.5)
    bsdf.inputs['Diffuse Roughness'].default_value = spec.get('diffuse_rough', 0.0)
    bsdf.inputs['Coat Weight'].default_value = spec.get('coat', 0.0)
    bsdf.inputs['Coat Roughness'].default_value = spec.get('coat_rough', 0.03)
    bsdf.inputs['Anisotropic'].default_value = spec.get('aniso', 0.0)
    bsdf.inputs['Sheen Weight'].default_value = spec.get('sheen', 0.0)
    color_out = None
    if 'color_tex' in spec:
        f, s = spec['color_tex']
        t = _img(nodes, f)
        links.new(_uv(nodes, links, s), t.inputs['Vector'])
        color_out = t.outputs['Color']
    if 'albedo_tex' in spec:
        f, s = spec['albedo_tex']
        t = _img(nodes, f, 'Non-Color')
        links.new(_uv(nodes, links, s), t.inputs['Vector'])
        mul = nodes.new('ShaderNodeMix'); mul.data_type = 'RGBA'; mul.blend_type = 'MULTIPLY'
        mul.inputs['Factor'].default_value = 1.0
        mul.inputs['A'].default_value = (*[c * 1.5 for c in spec['color']], 1)
        links.new(t.outputs['Color'], mul.inputs['B'])
        color_out = mul.outputs['Result']
        if 'noise' in spec:                       # large-scale albedo variation (ray-ish streaks, mature soil)
            sc, amt = spec['noise']
            nz = nodes.new('ShaderNodeTexNoise')
            nz.inputs['Detail'].default_value = 6
            tc = nodes.new('ShaderNodeTexCoord')
            links.new(tc.outputs['Object'], nz.inputs['Vector'])
            nz.inputs['Scale'].default_value = sc
            mr = nodes.new('ShaderNodeMapRange')
            mr.inputs['To Min'].default_value = 1 - amt; mr.inputs['To Max'].default_value = 1 + amt
            links.new(nz.outputs['Fac'], mr.inputs['Value'])
            m2 = nodes.new('ShaderNodeMix'); m2.data_type = 'RGBA'; m2.blend_type = 'MULTIPLY'
            m2.inputs['Factor'].default_value = 1.0
            links.new(color_out, m2.inputs['A'])
            links.new(mr.outputs['Result'], m2.inputs['B'])
            color_out = m2.outputs['Result']
    if 'color_mult' in spec and color_out is not None:      # keep a sunlit Earth inside the exposure range
        cm = nodes.new('ShaderNodeMix'); cm.data_type = 'RGBA'; cm.blend_type = 'MULTIPLY'
        cm.inputs['Factor'].default_value = 1.0
        links.new(color_out, cm.inputs['A'])
        k = spec['color_mult']; cm.inputs['B'].default_value = (k, k, k, 1)
        color_out = cm.outputs['Result']
    if spec.get('lommel'):
        color_out = _lommel(nodes, links, color_out)
    if color_out is not None:
        links.new(color_out, bsdf.inputs['Base Color'])
    if 'bump_tex' in spec:
        f, s, strength = spec['bump_tex'][:3]
        dist = spec['bump_tex'][3] if len(spec['bump_tex']) > 3 else 0.02
        t = _img(nodes, f, 'Non-Color')
        links.new(_uv(nodes, links, s), t.inputs['Vector'])
        bump = nodes.new('ShaderNodeBump')
        bump.inputs['Strength'].default_value = strength
        bump.inputs['Distance'].default_value = dist
        links.new(t.outputs['Color'], bump.inputs['Height'])
        links.new(bump.outputs['Normal'], bsdf.inputs['Normal'])
    if 'alpha_tex' in spec:
        f, s = spec['alpha_tex']
        t = _img(nodes, f, 'Non-Color')
        links.new(_uv(nodes, links, s), t.inputs['Vector'])
        links.new(t.outputs['Color'], bsdf.inputs['Alpha'])
    if 'emit' in spec:
        col, st = spec['emit']
        bsdf.inputs['Emission Color'].default_value = (*col, 1)
        bsdf.inputs['Emission Strength'].default_value = st
    return m


def library():
    """Create every material once; returns {name: material}."""
    return {k: make(k, v) for k, v in LIBRARY.items()}
