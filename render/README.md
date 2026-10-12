# Render pipeline (rev 33)

Photoreal "vanity" images of the rig in a lunar south-pole setting, made with Blender's Cycles renderer driven from Python (`pip install bpy`). Everything is procedural and built from the design numbers, so a design change is one edit in `params.py` and a re-run.

| File | What it holds |
|---|---|
| `params.py` | Rig dimensions, the one source of truth for the 3D assets (mast, collars, struts, stays, yard, wings, masthead, base), plus scene layout: yard azimuth, Sun and Earth directions, the pack being swapped |
| `meshes.py` | Mesh builder: tubes, boxes, rings and spheres merged into a few objects with UVs in metres and per-face material slots; fast heightfield objects |
| `rig.py` | The assets. Fixed parts (base enclosure, struts with tent-pole joints, foot pads and tensioners, stays, V-links, ties, collars, landing trays, a spare folded pack, an astronaut for scale) and rotating parts (lattice mast with Ti nodes and joint bands, roller bands, base frame, spreaders, diamond stays, braces, yard truss, walkway and rail, hangers, 16 concertina packs, the masthead crown and instrument post, two service bots) |
| `materials.py` | The material library (below) |
| `textures.py` | Writes the texture maps in `textures/` with numpy (deterministic) |
| `environment.py` | Terrain, boulders, sky, Sun and Earth |
| `shots.py` | The camera list |
| `render_all.py` | Builds the scene and renders the shots into `../renders/` |

## Materials

All are Principled BSDF. UVs are in metres, so texture scales are repeats per metre.

| Material | Used for | Look |
|---|---|---|
| `regolith` | Terrain, boulders | Albedo ~0.12 with an 8 m albedo tile, a 50 m noise layer and crater-pitted bump. A **Lommel-Seeliger** term scales brightness by 0.35/(μ₀+μ+0.1), so the soil brightens at grazing light and view as real regolith does, unlike a Lambert surface |
| `sintered` | Foot pads | Dark, glassy sintered regolith |
| `cfrp` | Mast lattice, yard truss, spreaders | Near-black 2/2 twill (0.1 m tile) under a clear coat |
| `white_coat`, `rod_jacket` | Struts, top-rigging rod bundles | White thermal coating; the jackets are slightly glossier |
| `titanium` | Nodes, joint bands, crown, hangers, V-links, ring frames | Brushed anisotropic metal |
| `gold_mli`, `silver_mli` | Converters, pack heads, tensioners, sensor hubs, reel garage | Crinkled multilayer insulation (bump map) |
| `osr_radiator` | Base enclosure panels, battery radiator | Optical solar reflector: mirror-like, coated |
| `solar_cell` | Pack front | 16 x 8 cells per 2 x 1 m panel, busbars and fingers, under coverglass |
| `kapton` | Pack back, folded packs | Amber polyimide |
| `grating` | Walkways, masthead platform | Aluminium bar grating with an alpha mask |
| `safety_yellow` | Fall-arrest rails, bot dock | Anodised yellow |
| `stainless`, `rope`, `steel`, `aluminium` | Roller bands, ropes and stays, foundation frame, trays | Metals |
| `bot_shell`, `bot_joint`, `visor`, `suit` | Bots and the astronaut | White shells, dark joints, gold visors |
| `red_light` | Masthead obstacle light | Emissive |
| `earth` | Earth | Texture scaled to 0.22, so a sunlit Earth stays inside the exposure set for grazing-lit ground |

## Textures (`textures/`, made by `textures.py`)

`solar_cell.png` (one panel), `cfrp_twill.png` + `cfrp_twill_bump.png`, `grating_alpha.png`, `mli_bump.png`, `regolith_albedo.png` + `regolith_bump.png`, `earth.png` (stylised), `stars.png` (equirectangular, faint).

## Environment

- **Site:** a knoll ~170 m outside the rim crest of a 21 km crater, so the horizon toward the Sun stays below ~0.6°. The site is a peak of near-eternal light. There is a flat graded pad 48 m in radius.
- **Crater:** its inner wall drops ~30° into permanent shadow.
- **Terrain:** crater populations (1.5 to 900 m), band-limited relief and ~2,700 boulders.
- **Backdrop:** six distant massifs (1.4 to 4.2 km high, 26 to 60 km out). Lunar curvature drops the far terrain (r²/2R).
- **Sun:** 1.5° elevation, 0.53° disc. The array faces it, parked at the maintenance azimuth.
- **Earth:** 1.9° across, gibbous, 5.5° above the horizon, lit by the same Sun.
- **Stars:** a faint field. This is artistic licence: an exposure for a sunlit scene would show none.

## Running

```bash
pip install bpy numpy pillow
cd lunar-rotating-platform/render
python3 textures.py                 # once
python3 render_all.py               # all shots, final (128 samples)
python3 render_all.py --samples 64  # faster
python3 render_all.py --preview 03 05   # quick low-res check of chosen shots
```

On 4 CPU cores a final shot at 1920 x 1080 and 64 samples takes a few minutes.
