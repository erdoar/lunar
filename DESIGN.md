# Lunar polar rotating solar platform: concept design (rev 2, compact ring)

A small turntable on a circular rail that carries a tall, cable-stayed solar array, for a lunar polar site (e.g. Shackleton rim, Malapert, Connecting Ridge). This is a first-pass concept with sizing estimates. Numbers are starting points to refine, not verified engineering.

**Rev 2 changes:** for logistics and construction reasons the rail ring is cut from Ø42 m (two rails) to **Ø12 m (one rail)**. The array is now much wider and taller than the ring. That only works because the Moon has **low gravity and no wind**, and the design is built around using both as fully as possible (section 2). The installation equipment is custom and human supervised (section 6).

![Platform layout: plan and elevation](platform-layout.svg)

## 1. Why it rotates, and how fast

At the poles the Sun stays within ~1.5° of the horizon and goes once around the horizon each lunar day (synodic, 29.5 Earth days). So the panels must:

- stand **vertical**, and
- turn about a vertical axis **once every 29.5 days**: about **0.51°/hour**, continuously, in one direction.

Height also pays: a few tens of metres above the local ground clears nearby terrain shadows and gives noticeably more hours of sunlight at most polar sites.

## 2. Using low gravity and no wind

On Earth a 40 m wide vertical sail on a 12 m base would blow over. On the Moon the only loads are:

| Load | Earth | Moon | Effect on design |
|---|---|---|---|
| Wind | Governs everything | **None** | Huge flat area costs almost nothing in structure; no flutter, no gust factor |
| Gravity | 9.81 m/s² | **1.62 m/s² (1/6)** | Members, stays, jacks and bearings are 1/6 the size for the same mass |
| Seismic | Varies | Shallow moonquakes, small accelerations | Main lateral load case; handled by symmetry, stays and uplift rollers |
| Thermal | Moderate | Large swings (~40 K to ~330 K) | Stays need spring tensioners; joints need float |
| Rotation dynamics | n/a | 0.51°/h: negligible | Only the start/stop steps matter; ramp them gently |

How the design uses this:

1. **Tension structure, sailing-ship rig.** A central mast holds horizontal yards; the solar blanket hangs from the top yard and is tensioned down to a bottom yard, like a square sail. Thin cables and booms carry everything; there are almost no bending members.
2. **Thin flexible solar blankets** (roll-out, ROSA-type, ~0.5 to 1 kg/m² including harness) instead of rigid panels. In 1/6 g with no wind they hang flat under light tension.
3. **Symmetry puts the centre of mass on the axis.** The array is one plane through the mast, left and right wings balanced. The ring only carries vertical load and small moments, so it can be small.
4. **The array overhangs the ring.** A 40 m wide blanket sits on a 12 m ring. Tipping needs a lateral acceleration of about g x r / h(CoM) = 1.62 x 6 / 18 ≈ **0.5 m/s²**, far above expected moonquake shaking, and uplift rollers add a positive lock on top.
5. **Low natural frequency is acceptable.** With no wind there is nothing to excite the rig except the drive and quakes. Drive in small steps with smooth acceleration ramps (seconds to minutes), never sudden starts.
6. **Light installation gear.** A jack or winch lifts 6x the mass it could on Earth. A 3 t mast weighs only ~4.9 kN on the Moon: hand-winch territory.

## 3. Reference configuration

| Item | Rev 2 value |
|---|---|
| Rail ring | **Ø12 m, single rail**, 12 identical segments, each π m (3.14 m) long |
| Bogies | **8** captive bogies, 2 wheels each (16 wheels) |
| Deck | Ø12 m ring girder + spokes, 4 bolted quarter-sections (fit a lander) |
| Mast | 45 m triangular truss, built in 3 m sections |
| Spreaders | 2 levels, ±8 m, to widen stay angles (as on a sailing boat) |
| Yards | Top yard at 40 m and bottom yard at 15 m, each 40 m long |
| Solar blanket | 40 m x 25 m = **1,000 m²**, one active face |
| Power (30% cells, 1,361 W/m², ~85% system) | **~350 kWe** (same as rev 1) |
| Rotating mass | ~12 t (blanket 1 t, yards 1 t, mast 3 t, stays/spreaders 0.5 t, deck 4 t, bogies 1.5 t, kingpin/slip ring 1 t) |
| Lunar weight | 12 t x 1.62 ≈ **19.5 kN** (rev 1: 97 kN) |
| Wheel load | ~1.2 kN nominal, 4 kN design (x3, one bogie removed) |
| Centre of mass | ~18 m above the deck, on the axis |

**Stays.** Forestay/backstay pairs run from the mast top and spreader tips to the deck ring rim, front and back. Topping lifts run from the mast top to the yard tips. Each stay has a **spring tensioner and load cell** at the deck end to take thermal length change (a 45 m steel stay changes ~50 mm over 100 K) and to show the rig's state.

## 4. Running gear (low friction, dust tolerant)

![Bogie and rail: side view and cross-section](bogie-rail.svg)

**Wheels**
- Flanged steel wheels, ~250 mm diameter (loads are now small), through-hardened bearing steel or a coated Ti wheel.
- **Avoid like-on-like metals** in vacuum (cold welding): hardened steel wheel on a ceramic or DLC-coated rail head (or Si₃N₄ rollers on steel).
- Hybrid ceramic bearings with **dry lubrication** (sputtered MoS₂/WS₂, PTFE-composite cages). No grease or oil.
- Labyrinth seals plus bellows boots.
- Rolling resistance Crr ~0.001 to 0.003: at 19.5 kN that is **20 to 60 N** total.

**Bogies**
- 2-wheel **equaliser** bogies, spring-loaded so both wheels share load.
- **Uplift rollers** under the rail head (captive bogie) for quakes and handling.
- **Side guide rollers** are optional: the kingpin centres the deck, so the bogies can float radially (±20 mm) for thermal movement.
- **Dust scrapers and brushes** ahead of each wheel, both directions.
- Standard **4-bolt kinematic mount** with captive bolts and a grapple fixture. One bogie ≈ 60 to 80 kg on Earth, about 12 kg-weight on the Moon: **one person can handle it**.

**Centring, drive, power transfer**
- Central **kingpin** with a slewing bearing (~1.2 m) takes radial loads and the mast base moment from quakes. It is also the survey datum for building the ring (section 6).
- **Drive**: 2 of the 8 bogies are drive bogies (a pinion on a rack on the rail web, or friction wheels); one is enough to turn the platform.
- Running power is milliwatts. Size the drive for breakaway in dust (~20x running force, ~1 kN tangential): a few hundred watts.
- Power crosses the rotation through a **slip ring or rotary transformer** in the kingpin.

## 5. Track (raised, segmented, swappable)

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
3. Unbolt, lift out, drop in the spare, level against the radius arm (section 6), remove the bridge.
4. If only the running surface is damaged, swap just the rail head strip (~10 kg).

**Spares on site**: 2 bogies, 2 rail segments, 6 rail head strips, 1 drive unit, slip-ring brush cartridges, 2 stays with tensioners, 1 blanket roll section.

## 6. Installation equipment and sequence (human supervised)

Everything is built at or near ground level and then raised. A crew member (EVA, or from a pressurised rover nearby) supervises each step, checks readouts and approves every hold point. Machines do the lifting and positioning.

| # | Equipment | What it does |
|---|---|---|
| E1 | **Kingpin driver** | Small drill/ground-screw rig that sets the central kingpin foundation. The kingpin becomes the datum for everything else. |
| E2 | **Radius arm ("compass")** | A 6 m arm that rotates on the kingpin, with a laser level, encoder and a pier socket at its tip. It places every pier at exactly r = 6 m and the right height. Because the ring is small, one rigid arm replaces a survey crew. |
| E3 | **Rail-riding installer cart** | Rides on the rail already installed, carries the next segment and pier, and places them at the open end of the ring under the radius arm's guidance. Later it becomes the **maintenance cart** (jacking, bogie and segment swaps). |
| E4 | **Mast jack-up frame** | Sits on the deck around the kingpin. It lifts the whole mast one section (3 m) and a new section is pinned in at the bottom. All mast assembly happens at deck height, so no crane. Lifting the full 3 t mast needs only ~5 kN of jack force. |
| E5 | **Rigging winches with load cells** | Tension the stays, raise the yards and deploy the blanket. Tensions are shown on a tablet for the supervisor. |
| E6 | **Regolith compaction plate** | Vibratory plate to prepare pier pads; optional microwave sintering head. |

**Sequence**
1. Survey and clear a ~16 m circle. Set the kingpin (E1).
2. Mount the radius arm (E2) on the kingpin and set the 12 piers.
3. Lay the 12 rail segments with the installer cart (E3), checking each against the radius arm. Hold point: ring flat to ±2 mm.
4. Place 8 bogies on the rail, then the 4 deck quarter-sections on the bogies and kingpin. Bolt and check the deck turns freely by hand.
5. Install the jack-up frame (E4). Fit the top mast section with the **top yard folded vertically** alongside it and the **blanket rolls** stowed on the yard.
6. Jack the mast up section by section, adding spreaders and stays as each level passes deck height. Tension the stays progressively (E5).
7. At full height, swing the top yard horizontal with its halyards and set the topping lifts.
8. Unroll the blankets downward from the top yard. In 1/6 g and no wind they hang straight and do not flap. Attach them to the bottom yard and tension (E5).
9. Connect the harness to the slip ring, commission the drive, start tracking.

Every part is designed for this: captive fasteners only, one tool size, alignment cones on every joint, grapple fixtures, and no part over ~150 kg-weight on the Moon (~900 kg mass) without lifting gear.

## 7. Environment checklist

| Hazard | Response |
|---|---|
| Temperature swings | Spring tensioners on stays, radial float in bogies, rail expansion joints; materials tough at cryogenic temperatures (austenitic stainless, Ti-6Al-4V, Al-Li) |
| Cold welding in vacuum | Dissimilar or coated mating surfaces, dry lubricants |
| Abrasive, electrostatic dust | Raised rail, scrapers, labyrinth seals, overhanging skirt, keep rover traffic away; blanket mounted high, above most lofted dust |
| Moonquakes | Symmetric balanced rig, stays, uplift rollers, kingpin moment capacity |
| Micrometeoroids | Blanket made of replaceable strings/sections; stays sized with margin and redundant pairs |
| Regolith settlement | Adjustable piers, periodic re-leveling with the radius arm |
| Shading between rigs | Rigs on a shared ridge spaced ~10x blanket height apart along the Sun's path |

## 8. Alternatives worth comparing

- **No rail, kingpin only:** the rig is balanced, so a single large slewing bearing could carry it. The rail ring adds tipping stiffness and redundancy, and gives the installer and maintenance cart a track. Worth a trade study.
- **NASA VSAT-style mast** (single tall tracking mast with a rotating array at the top): rotate only the array, not the base. Lighter base, but the rotating joint is 40 m up, which makes it harder to service.
- **Fixed multi-face arrays:** no moving parts, about 1/3 to 1/2 of the energy.

## 9. Next steps

1. Fix the site and power target; that sets mast height and blanket size.
2. Rig analysis: stay pre-tension, thermal cases, modal analysis, moonquake response, the jack-up stages.
3. Wheel/rail and bearing tests in vacuum with regolith simulant (LHS-1, NU-LHT) across the temperature range.
4. Prototype the radius arm and installer cart; rehearse the whole build on Earth with suited operators (with a 1/6 g offload rig for the lifting steps).
5. Packaging: deck quarters, mast sections and rail segments to fit the lander.
