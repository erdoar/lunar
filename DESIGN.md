# Lunar polar rotating solar platform: concept design (rev 4, tall mast on a strut tripod)

A small turntable on a circular rail that turns a very tall mast, with the solar array at the top, for a lunar polar crater-rim or ridge site (e.g. Shackleton rim, Malapert, Connecting Ridge). This is a first-pass concept with sizing estimates. Numbers are starting points to refine, not verified engineering.

**Revision history**
- Rev 1: Ø42 m twin-rail turntable carrying a 30 m panel wall.
- Rev 2: rail ring cut to Ø12 m for logistics; cable-stayed rig that uses low gravity and no wind; human-supervised installation equipment.
- Rev 3: array raised to ~100 m to clear terrain and neighbour shadows; mast braced by stationary ground guys through roller collars; lowerable solar curtains.
- **Rev 4 (this):** the ground guys and their tension anchors are replaced by a **strut tripod**. Three rigid struts run from a **mid-height collar** down to foot pads on the surface. Each foot is wire-braced up to an **upper collar** and tied **horizontally back to the platform's kingpin foundation**. It is a closed, pre-tensioned truss: no ground anchor ever has to resist being pulled up, and there are 2 collars instead of 3.

![Platform layout: elevation and plan](platform-layout.svg)

## 1. Why it rotates, and why it must be tall

At the poles the Sun stays within ~1.5° of the horizon and goes once around it each lunar day (29.5 Earth days). So the array must stand **vertical** and turn about a vertical axis **once every 29.5 days** (~0.51°/hour), always in the same direction.

At such low Sun angles every bump shades a long way: a 10 m rise casts a shadow ~380 m long at 1.5°, and a 100 m object ~3.8 km. On crater rims and ridges, how many hours of sunlight a point gets rises steeply with height above the ground, because the line to the Sun clears more of the far terrain. So the array top is pushed up as far as structure, installation and site allow. Published illumination models of polar sites, and tower concepts such as Honeybee Robotics' LUNARSABER (~100 m), point to the same order of height.

**How to set the height for a real site:** run a horizon/illumination analysis on LOLA elevation data for the exact spot, for array-top heights of, say, 20 to 200 m. Plot hours of sunlight per year against height and pick the knee of the curve. The structure in this document scales across that range (section 3).

## 2. Using low gravity and no wind

| Load | Earth | Moon | Effect on design |
|---|---|---|---|
| Wind | Governs tall masts | **None** | A slender 100 m+ mast and a 1,000 m² sail with almost no lateral load |
| Gravity | 9.81 m/s² | **1.62 m/s² (1/6)** | Mast and strut compression, wire tension, jacks and bearings are 1/6 the size |
| Seismic | Varies | Shallow moonquakes, small accelerations | Main lateral load; carried by the strut tripod |
| Thermal | Moderate | Large swings and one-sided sunlight | Thermal bow of the mast; use CFRP, keep the gradient steady (below) |
| Rotation dynamics | n/a | 0.51°/h | Negligible; ramp the drive steps gently |

How the design uses this:

1. **A slender braced mast.** Without wind and in 1/6 g, a light lattice mast needs only a little lateral bracing to reach 100 m or more. Its practical limit is set by the site, installation and shading, not strength.
2. **The bracing doesn't rotate.** A stationary **strut tripod** holds the mast through two **roller collars**, and the mast turns inside them. This keeps the base ring small (Ø12 m) while the bracing spreads wide (feet at 30 m).
3. **A closed truss, so no tension anchors.** Each bracing plane is a triangle: strut (compression), wire (tension) and the mast between the two collars. A horizontal tie from each foot to the kingpin foundation closes it at ground level. The three ties pull on the kingpin from 120° apart, so they cancel. The foot pads only ever push down on the ground. Holding up-pull in loose regolith is hard; bearing down on it is easy.
4. **The array sits above all the bracing.** It sweeps a 17 m radius circle from 67 to 100 m. The upper collar is at 62 m, so the turning array never meets a strut or wire. Above the collar the mast is braced by its own rotating **diamond stays** (spreaders and stays that turn with the mast, as on a racing yacht).
5. **Thin roll-out blankets** (~0.5 to 1 kg/m² with harness). In 1/6 g with no wind they hang flat under light tension.
6. **Balanced rig.** The array is one plane through the mast, left and right equal, so its centre of mass stays on the axis.
7. **Steady sunlight makes thermal bow predictable.** Because the rig tracks the Sun, the same mast face is always sunlit, so the bow is nearly constant and can be trimmed out with wire tension. The mast sits behind the blanket, so its top section is in shade. CFRP tubes (α ≈ 0 to 1x10⁻⁶ /K) keep the bow to a few centimetres. The same 35 m length in aluminium would bow ~0.9 m.
8. **Light installation gear.** The whole mast plus array (~5 t) weighs about 8 kN on the Moon, so a modest jack at deck level can raise all of it (section 7).

## 3. Reference configuration (100 m baseline)

| Item | Rev 3 value |
|---|---|
| Array top / bottom | **100 m / 70 m** above the deck |
| Mast | 105 m triangular CFRP lattice (Ti nodes), 1.2 to 1.5 m face, ~25 kg/m (~2.5 t), built in 3 m sections |
| Solar curtains | 8 vertical curtains, each ~4 m x 30 m, total 34 m x 30 m ≈ **1,000 m²** |
| Power (30% cells, 1,361 W/m², ~85% system) | **~350 kWe** |
| Top / bottom yards | 34 m, at 100 m and 70 m |
| Roller collars (stationary) | **Strut collar at 35 m**, **upper collar at 62 m** |
| Struts | 3 at 120°, CFRP tube Ø0.3 m x 2 mm, **46 m** long, ~3 kg/m (~140 kg each), ball joints at both ends |
| Foot pads | 3 at **30 m radius**, ~1 m² sintered or gabion pad, compression only (~0.5 kN) |
| Wires | Foot to upper collar, 69 m, 6 mm stainless wire rope (UV-proof), doubled for redundancy, ~1.5 kN pretension |
| Ties | Foot to kingpin foundation, horizontal at ground level (passing under the raised rail), ~1 kN |
| Upper bracing (rotating) | Diamond stays: spreaders ±6 m at 81 m, stays from 62 m to the mast top |
| Rail ring | Ø12 m single rail, 12 segments of π m, 8 bogies (unchanged from rev 2) |
| Rotating mass | ~11.5 t (mast 2.5 t, array + yards 2 t, deck 4 t, bogies 1.5 t, kingpin 1 t, diamond stays 0.5 t) |
| Lunar weight on the ring | ~19 kN; the pre-tensioned tripod lifts the mast very slightly (~1.5 kN), so the ring carries a little less |
| Maintenance azimuth | Mast parked so the array lies **between** bracing planes (e.g. 30°/210° when the struts are at 0°/120°/240°) |

**Scaling to other heights** (rough; same array, CFRP mast; struts sized for ~4x buckling margin):

| Array top | Upper collar | Strut collar | Foot radius | Strut length | Mast mass | Lunar weight |
|---|---|---|---|---|---|---|
| 60 m | 22 m | 12 m | ~12 m | ~17 m | 1.2 t | ~16 kN |
| **100 m** | **62 m** | **35 m** | **30 m** | **46 m** | **2.5 t** | **~19 kN** |
| 150 m | 112 m | 60 m | ~50 m | ~78 m | 4.8 t | ~23 kN |
| 200 m | 162 m | 85 m | ~70 m | ~110 m | 8 t | ~29 kN |

Above ~150 m the struts get long enough that they need a larger lattice section or a mid-length brace. In practice the height is limited by:
- **Footprint**: the ridge must be ~2x the foot radius wide. That is smaller than the guy anchor footprint in rev 3, but ridges are often only a few hundred metres across.
- **Installation time** at the jack.
- **Sightlines to other collectors**: a taller rig shades more of the ridge.

**Pre-tension (100 m case).** Tighten the wire to ~1.5 kN and the tie to ~1 kN. That puts ~2.5 kN of compression in the strut (buckling load ~10 kN) and leaves each foot pressing ~0.5 kN on its pad. Keep strut compression above ~1.2x the wire tension so the feet never lift. Load cells on every wire and tie show the rig's state.

## 4. Mast, collars and curtains

![Roller collar: plan and section](collar.svg)

**Roller collars.** Each collar is a stationary ring around the mast, made of 3 bolted 120° segments so it can be fitted around the mast. At that height the mast carries a circular **collar band**: a Ti box ring bolted to the three mast legs, with ceramic/DLC-coated running faces on the top, outside and underside.

The collar holds **6 identical roller cartridges**. Each is a C-frame that wraps the band edge, like a base bogie wraps its rail. It carries three rollers:
- an **upper thrust roller**: the upper collar is pulled down by the wires,
- a **radial guide roller**: holds the mast sideways,
- a **lower thrust roller**: the strut collar is pushed up by the struts, and it also resists quake uplift.

So one cartridge design serves both collars. Each cartridge slides out radially on rails through a window in the collar ring. A preload spring gives ±10 mm of float for thermal mismatch, it has 2 captive bolts, and it has a grapple fixture for the climber robot. The collar works with any one cartridge removed.

The rollers use the same technology as the bogies (dry-lubricated hybrid bearings, dissimilar surfaces). The collars carry only light loads (pre-tension and quake loads), so the heavy, critical parts stay at ground level: vertical load, drive and slip ring. Dust is far lower at height.

A **transport clamp pin** in each cartridge locks the collar to the band during jack-up (section 7) and is pulled once the collar is at height.

**Curtains instead of one blanket.** The array is 8 vertical curtains, 4 m wide. Each hangs from its own **halyard on the top yard** and is tensioned down to the bottom yard. To repair one (for example after a micrometeoroid strike):
1. Rotate the mast to the **maintenance azimuth**, so the array lies between the bracing planes.
2. Release the curtain's bottom tension lines.
3. Lower it on its halyard, in front of the bottom yard, straight down to the ground. No strut, wire or tie lies in that vertical plane, and the innermost curtain starts 2 m from the mast to clear the collars.
4. Swap the curtain (or a section) at ground level and haul it back up.

Nobody has to climb for the most common repair.

**Mast climber robot.** A small robot climbs the lattice to inspect it, swap collar roller cartridges, re-tension diamond stays and service the yards. It is teleoperated with a human supervising, and it doubles as an installation tool (section 7).

## 4b. Shading between collectors

When several rigs share a ridge, one shades another when the Sun lines up behind it. The shade lasts roughly (array width / spacing in degrees + 0.53° Sun disc) / 0.51° per hour, once per lunar day for each neighbour that can line up:

| Spacing | Shade per alignment | Share of the lunar day lost |
|---|---|---|
| 200 m | ~20 h | ~2.9% |
| 340 m (10x width) | ~12 h | ~1.7% |
| 500 m | ~9 h | ~1.2% |
| 1,000 m | ~5 h | ~0.7% |

Layout rules:
- **Space rigs ≥10x the array width apart.**
- **Put them on a line along the ridge crest**, so they line up with the Sun only twice per lunar day.
- **Stagger the heights** of neighbours by more than the array height, so their arrays don't overlap in the sky. Then a neighbour's shadow is only its thin mast, which costs well under 1%.

## 5. Running gear at ground level (low friction, dust tolerant)

![Bogie and rail: side view and cross-section](bogie-rail.svg)

**Wheels**
- Flanged steel wheels, ~250 mm diameter (loads are now small), through-hardened bearing steel or a coated Ti wheel.
- **Avoid like-on-like metals** in vacuum (cold welding): hardened steel wheel on a ceramic or DLC-coated rail head (or Si₃N₄ rollers on steel).
- Hybrid ceramic bearings with **dry lubrication** (sputtered MoS₂/WS₂, PTFE-composite cages). No grease or oil.
- Labyrinth seals plus bellows boots.
- Rolling resistance Crr ~0.001 to 0.003: at ~19 kN  that is **30 to 90 N** total.

**Bogies**
- 2-wheel **equaliser** bogies, spring-loaded so both wheels share load.
- **Uplift rollers** under the rail head (captive bogie) for quakes and handling.
- **Side guide rollers** are optional: the kingpin centres the deck, so the bogies can float radially (±20 mm) for thermal movement.
- **Dust scrapers and brushes** ahead of each wheel, both directions.
- Standard **4-bolt kinematic mount** with captive bolts and a grapple fixture. One bogie ≈ 60 to 80 kg on Earth, about 12 kg-weight on the Moon: **one person can handle it**.

**Centring, drive, power transfer**
- Central **kingpin** with a slewing bearing (~1.2 m) takes radial loads and the mast base moment from quakes. It is also the survey datum for building the ring (section 7).
- **Drive**: 2 of the 8 bogies are drive bogies (a pinion on a rack on the rail web, or friction wheels); one is enough to turn the platform.
- Running power is milliwatts. Size the drive for breakaway in dust (~20x running force, ~1 kN tangential): a few hundred watts.
- Power crosses the rotation through a **slip ring or rotary transformer** in the kingpin.

## 6. Track (raised, segmented, swappable)

- **Raised rail** on piers ~0.5 m above the regolith, away from near-surface dust and with room to work underneath.
- Rail: hollow box beam with a bolted, replaceable **rail head strip**.
- **12 identical segments**, π m long. Each sits on 2 piers that are shared with its neighbours at the joints, so **12 piers** in all, plus 4 kingpin anchors.
- **Angled (scarf) joints** with slotted holes for ~3 to 5 mm expansion each.
- **Piers** have leveling screws (±50 mm) on sintered-regolith pads, helical ground screws, or regolith-filled gabion bags.
- An overhanging **skirt or brush seal** on the deck keeps falling dust off the rail head.

**Replacing a bogie** (N+2: runs with any 2 non-adjacent bogies removed)
1. Stop the drive and lock it.
2. Jack the deck ~10 mm at the hard-points either side of the bogie.
3. Undo 4 captive bolts, slide the bogie out radially, slide the spare in (the kinematic mount self-locates), torque, lower.

**Replacing a rail segment**
1. Rotate so the segment is between two bogies. Bogie spacing is 4.7 m against 3.14 m segments, so there is margin.
2. Clamp the **bridging rail** (6.3 m, two segment lengths) across it if the platform must keep moving.
3. Unbolt, lift out, drop in the spare, level against the radius arm (section 7), remove the bridge.
4. If only the running surface is damaged, swap just the rail head strip (~10 kg).

**Spares on site**: 2 bogies, 2 rail segments, 6 rail head strips, 1 drive unit, slip-ring brush cartridges, 2 collar roller cartridges, 1 wire and 1 tie with tensioners, 1 strut section, 2 blanket curtains.

## 7. Installation equipment and sequence (human supervised)

Everything is assembled at deck level and raised. A crew member (EVA, or in a pressurised rover nearby) supervises each step and signs off every hold point. Machines do the lifting.

| # | Equipment | What it does |
|---|---|---|
| E1 | **Kingpin driver** | Sets the central kingpin foundation: the datum for everything else. |
| E2 | **Radius arm ("compass")** | 6 m arm on the kingpin with a laser level, encoder and pier socket. It places and levels the 12 rail piers. With an extension and laser rangefinder, it also lays out the 3 foot-pad sites at 30 m. |
| E3 | **Rail-riding installer cart** | Lays rail segments from the installed rail; later the maintenance cart (jacking, bogie and segment swaps). |
| E4 | **Foot-pad and tie layer** | Compacts or sinters the 3 foot pads and lays the 3 ground ties from the kingpin foundation out to the feet, under the raised rail. No pull-out anchors needed. |
| E5 | **Mast jack-up frame** | Sits on the deck around the kingpin and lifts the whole mast one 3 m section at a time; the new section is pinned in at the bottom. Peak lift is ~8 kN (whole mast + array) plus bracing pre-tension. |
| E6 | **Tie and wire winches with load cells** | One at each foot. They control the ties (which pull the strut feet in as the mast rises) and the wires, and keep the mast plumb. Tensions are shown live on a supervisor tablet. |
| E7 | **Mast climber robot** | Fits and checks the diamond stays and collar cartridges at height. Later used for inspection and maintenance. |
| E8 | **Curtain winch** | Raises and lowers curtains on their halyards (also used for repairs). |

**Sequence**
1. Survey and clear the site. Set the kingpin (E1). Lay out the 3 foot sites with the radius arm (E2); prepare the pads and lay the ties (E4).
2. Set the 12 rail piers and lay the ring (E2, E3). Hold point: ring flat to ±2 mm.
3. Place 8 bogies and the 4 deck quarters. Check the deck turns by hand.
4. Fit the jack-up frame (E5). Assemble the **top assembly** at deck level: mast top section, diamond spreaders and stays, top yard folded vertically, curtains rolled on the top yard, bottom yard folded.
5. **Jack up, with a scissor action.** Each collar is fitted around the mast at deck level (3 segments), clamped to its band, and rides up with the mast.
   - The **upper collar** goes on first, with its 3 wires paid out from the foot winches as it rises. Until the struts are in, these wires act as light temporary guys (a few hundred N). Each foot winch is ballasted with regolith bags so it never needs a pull-out anchor.
   - When the strut band reaches the deck, the **strut collar** goes on. The 3 struts are pinned to it while lying flat on the ground, pointing outward, with their feet on skid dollies.
   - As the mast keeps rising, the struts swing up and the tie winches (E6) **pull the feet in** along the ground, from 46 m to their 30 m pads. Low gravity keeps the strut and dolly loads tiny.
   - At final height, the feet drop onto their pads and the ties and wires are tensioned. The clamp pins are pulled, and from then on the mast turns freely in both collars.
6. At full height, unfold the yards. Set the maintenance azimuth and lower the curtains one at a time onto the bottom yard, then tension them (E8).
7. Trim wire and tie tensions to plumb the mast and take out thermal bow. Connect the harness to the slip ring, commission the drive, start tracking.

Design rules for every part: captive fasteners, one tool size, alignment cones, grapple fixtures, and no single piece heavier than ~150 kg-weight on the Moon without lifting gear.

## 8. Environment checklist

| Hazard | Response |
|---|---|
| Terrain and neighbour shadows | Array at the top of a 100 m+ mast; site illumination study sets the height; spacing and stagger rules (section 4b) |
| Temperature swings, one-sided sunlight | CFRP mast and struts, mast behind the blanket, spring tensioners on wires and ties, steady sun-tracking gradient trimmed by wire tension |
| Cold welding in vacuum | Dissimilar or coated mating surfaces, dry lubricants on all rollers |
| Abrasive, electrostatic dust | Raised rail, scrapers, seals, skirt at ground level; collars and array are high above most lofted dust |
| Moonquakes | Strut tripod carries lateral load; balanced rig; lower thrust rollers in the collars and uplift rollers at the base |
| Micrometeoroids | Lowerable curtains; doubled wires; struts are thick-walled tubes, inspected by the climber |
| UV and radiation on cables | Steel wire rope or coated CFRP rod, not bare aramid or polymer fibre |
| Regolith settlement | Adjustable piers and foot pads; wire and tie tensions monitored with load cells and re-trimmed |

## 9. Alternatives worth comparing

- **Ground guys with tension anchors (rev 3):** 9 guys, 3 collars, anchors at 40 m. Needs proof-loaded pull-out anchors in regolith, which are uncertain and slow to install. The rev 4 tripod avoids them.
- **Rotate only the top** (VSAT / LUNARSABER style): a fixed tower with a slewing bearing and slip ring under the array at 70 to 100 m. No collars, but the heaviest moving parts are high up. This design keeps them at ground level.
- **No rail, kingpin only:** the rig is balanced and the tripod carries lateral load, so a single base slewing bearing may be enough. The rail adds redundancy and a track for the maintenance cart. Worth a trade study.
- **Several shorter rigs vs one tall one:** depends on the site's illumination-vs-height curve.

## 10. Next steps

1. **Site illumination study** on LOLA data: sunlight hours vs array height at candidate spots; pick the height.
2. Mast and tripod analysis: strut and mast buckling, pre-tension, thermal bow, moonquake response, every jack-up and scissor stage.
3. Collar roller design and vacuum/thermal tests, together with the bogie wheel/rail tests (LHS-1, NU-LHT simulants).
4. Prototype the jack-up with collars, the strut scissor and tie winches at small scale; rehearse with suited operators.
5. Curtain halyard and lowering trials; pick a blanket that tolerates repeated lowering.
6. Packaging: deck quarters, 3 m mast sections, rail segments, curtain rolls to fit the lander.
