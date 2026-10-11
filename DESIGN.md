# Lunar polar rotating solar platform: concept design

A large turntable on circular rails carrying a tall scaffold of solar panels, for a lunar polar site (e.g. Shackleton rim, Malapert, Connecting Ridge). This is a first-pass concept with sizing estimates. Numbers are starting points to refine, not verified engineering.

## 1. Why it rotates, and how fast

At the poles the Sun stays within ~1.5° of the horizon and goes once around the horizon each lunar day (synodic, 29.5 Earth days). So the panels must:

- stand **vertical** (tilt only ±2°), which makes the scaffold tall rather than wide, and
- turn about a vertical axis **once every 29.5 days**: about **0.51°/hour**, continuously, in one direction.

That speed is extremely slow. Friction barely matters for running power; it matters for **breakaway (stick-slip) torque, wear from dust, and cold welding**. The design is built around those.

## 2. Reference configuration

| Item | Baseline value |
|---|---|
| Track diameter | 40 m (2 concentric rails at 38 m and 42 m) |
| Scaffold | Twin vertical panel walls, back to back, 36 m wide x 30 m tall, on a space-frame truss |
| Panel area | ~2 x 1,000 m² (one face sunlit; the back face can be bifacial or radiator) |
| Power (30% cells, 1,361 W/m², ~85% system) | ~350 kWe from one face |
| Total rotating mass | ~60 t (truss 25 t, panels 15 t, deck 15 t, bogies 5 t) |
| Lunar weight | 60 t x 1.62 m/s² ≈ **97 kN** |
| Bogies | 24 bogies (12 per rail), 2 load wheels each = **48 load wheels** |
| Nominal wheel load | ~2.0 kN (~200 kg-force) |
| Design wheel load | 6 kN (x3 for uneven load, dynamic, one neighbour bogie removed) |

Twin back-to-back walls keep the centre of mass on the axis and balance the overturning moment; a single wall would put a large eccentric load on one side of the ring.

```
             Sun (on horizon, moving around)
                 ->
   +----------------------------------+   <- panel wall A (30 m tall)
   |##################################|
   |##################################|   <- space-frame truss between walls
   |##################################|   <- panel wall B
   +================+=================+   <- rotating deck (ring girder)
   [B]   [B]   [B]  | kingpin  [B]  [B]   <- bogies on two rails
 ==rail==rail=======O=====rail===rail===  <- raised rail on piers, 0.6 m above regolith
```

## 3. Running gear (low friction, dust tolerant)

![Bogie and rail: side view and cross-section](bogie-rail.svg)

**Wheels**
- Flanged steel wheels, ~400 mm diameter, through-hardened bearing steel (or Ti wheel with a hard coating). Wheel load is low, so wheels can be light.
- **Avoid like-on-like metals** in vacuum (cold welding). Pair a hardened steel wheel with a rail head of a different material or coating: e.g. ceramic (TiN / DLC / Al₂O₃ plasma spray) on the rail head, or silicon nitride rollers on a steel rail.
- Bearings: hybrid ceramic (Si₃N₄ balls, steel races) with **dry lubrication** (sputtered MoS₂ or WS₂, or PTFE-composite cages). No grease or oil: they outgas, freeze and collect dust.
- Sealed bearings with **labyrinth seals plus bellows boots**. Contact seals wear quickly in regolith.
- Rolling resistance with dry hard surfaces: Crr ~0.001 to 0.003. At 97 kN that is **100 to 300 N** total resistance.

**Bogies**
- Each bogie is a **swing-arm (equaliser) pair** of 2 wheels, spring-loaded so all wheels share load over uneven rail.
- **Radial float** of ±50 mm, so thermal expansion of the deck vs. the cold rail is taken in the bogie, not in the structure.
- **Uplift rollers** under the rail head (captive bogie), to resist tipping from moonquakes, off-centre loads and handling.
- **Side guide rollers** on the inner rail only; the outer rail is free radially. This avoids binding.
- **Dust scrapers and brushes** ahead of each wheel in both directions; a soft brush plus a hard skid.
- Standard **4-bolt kinematic interface** (cone, V-groove, flat) to the deck, with captive bolts and a robot grapple fixture. One bogie = one replaceable unit (~150 to 200 kg).

**Centring and drive**
- Central **kingpin** (large slewing bearing, ~2 m) takes radial loads only; vertical load goes to the rails. This keeps the ring concentric even if rail segments shift a little.
- **Drive**: 4 friction or pinion drive bogies (redundant, 2 needed). A rack on the inner rail gives positive drive without slip in dust; a friction drive is simpler but can slip.
- Running power: 300 N x (40 m x π / 29.5 d) ≈ 300 N x 0.05 mm/s ≈ **15 mW**. The drive is sized for **breakaway and dust**: assume 20x running force, ~6 kN tangential, still under 1 kW of motors.
- Drive by **stepping** (move a few cm, stop) rather than truly continuous creep; this avoids stick-slip chatter and lets you clean between moves.

**Power and data across the rotation**
- Rotation is always one way, so cable wrap won't work for long. Use a **slip ring or rotary transformer at the kingpin**. A contactless rotary transformer avoids brush wear and dust. At ~350 kW, a DC slip ring with multiple redundant brushes in a sealed housing is the simpler choice.

## 4. Track (raised, segmented, swappable)

- **Raised rail** on piers ~0.6 m above the regolith. Most dust that moves near the surface (rover-kicked, electrostatically lofted) stays low. It also keeps the rail away from regolith creep and gives clearance to work underneath.
- Rail profile: a hollow steel or titanium box beam with a bolted, replaceable **rail head strip**.
- **Segments**: 3 m arcs (42 per inner ring, 44 per outer ring), all identical within each ring. Each segment sits on **2 adjustable piers** with leveling screws (±50 mm).
- **Joints**: angled (scarf) joints so the wheel never meets a square gap; slotted holes give ~5 mm expansion per joint. Steel across 150 K changes ~5.4 mm per 3 m segment, so each joint takes its own segment's movement.
- **Foundations**: one of
  - sintered or microwave-melted regolith pads,
  - helical ground screws (good in compacted regolith),
  - regolith-filled gabion bags with a leveling plate.
  Leveling is reset by robot via the pier screws, so foundation settlement is a maintenance task, not a failure.
- Covers: a **light skirt or brush seal** on the deck hangs over the rail head and catches falling dust. An electrodynamic dust shield (EDS) on the rail head is optional.

## 5. In-situ replacement

Design rule: **N+2 redundancy**. The platform keeps operating with any 2 non-adjacent bogies removed, and with any single rail segment removed.

**Replacing a bogie**
1. Stop rotation; lock the drive.
2. A robot (or crew) sets a **jack** on the deck hard-points either side of the bogie and lifts ~10 mm. Neighbouring bogies carry the load (that is why the design wheel load is 3x nominal).
3. Undo the 4 captive bolts; the grapple pulls the bogie radially outward on its guide rails.
4. Insert the spare; the kinematic mount self-locates; torque bolts; lower.

**Replacing a rail segment**
1. Rotate the platform so the segment is in the gap **between** two bogies (bogie spacing ~5 m > 3 m segment length, with margin).
2. Install a **bridging rail** (a stiff 6 m beam, carried by the robot) that clamps to the neighbouring segments, so the platform can still roll past if needed.
3. Unbolt the segment from its 2 piers; lift it off; place the new one; level it with the pier screws against a laser reference.
4. Remove the bridge. Or just replace the **rail head strip** (bolted, ~30 kg) if only the running surface is damaged.

**Spares on site**: 4 bogies, 4 rail segments, 20 rail head strips, 2 drive units, slip ring brush cartridges.

**Interfaces for robots**: every replaceable unit has a standard grapple fixture, captive fasteners (no loose nuts), one tool size, alignment pins and visual targets.

## 6. Environment checklist

| Hazard | Response |
|---|---|
| Temperature, roughly 40 K (shadow) to ~ +60 °C in sunlit polar areas | Radial float in bogies, expansion joints in rail, materials tough at cryogenic temperatures (austenitic stainless, Ti-6Al-4V, Al-Li; avoid ferritic steel near permanent shadow, it embrittles) |
| Cold welding in vacuum | Dissimilar or coated mating surfaces, dry lubricants |
| Abrasive, electrostatic dust | Raised rail, scrapers, labyrinth seals, overhanging skirt, stepping motion, keep rover traffic away |
| Moonquakes (shallow ones up to ~M5) | Uplift rollers, low natural frequency checked against the tall scaffold |
| Micrometeoroids | Replaceable panel strings; rail head strips are consumables |
| Settlement of regolith | Adjustable piers, periodic laser leveling |
| Shadowing between towers | Spacing rule ~10x tower height if several platforms share a ridge |

## 7. Alternatives worth comparing

- **Central slewing bearing only** (no rails): simpler for small arrays, but a 30 m tall wall puts a huge overturning moment on one bearing. Rails win at this size.
- **Fixed vertical arrays facing several directions** (no rotation): no moving parts, but about 1/3 to 1/2 of the energy of a tracking array.
- **Rotate panels on the scaffold instead of the whole platform**: many small actuators instead of one big turntable. More failure points, but each is small and easy to replace.
- **NASA VSAT-style mast**: a single tall tracking mast, already being developed; useful as a benchmark.

## 8. Next steps

1. Fix the site and power target; that sets height and diameter.
2. Structural model of the scaffold (modal analysis, moonquake, handling loads during jacking).
3. Wheel and rail material tests in vacuum with lunar regolith simulant (e.g. LHS-1, NU-LHT) at temperature extremes: wear rate, friction, cold welding.
4. Detailed bogie design and a robotic swap demonstration on Earth.
5. Mass and launch packaging: segment lengths should fit the lander fairing.
