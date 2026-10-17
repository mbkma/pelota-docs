---
title: Art and models
weight: 2
---

Everything you see in Pelota can use your help: the players, their clothes and rackets, the
court and the stadium. The source files (Blender files and textures) live in the
[pelota-files](https://github.com/mbkma/pelota-files) repository; the exported models and
textures go into the game.

{{< callout type="info" >}}
The game has a color palette for a consistent look: `assets/pelota_color_palette.gpl` (for GIMP,
Krita or Inkscape), also as `.png` and `.svg`.
{{< /callout >}}

## How a player's look is built

A player has a **body**: a rigged model exported from Blender with its meshes (body, shirt,
shorts, shoes, hair, ...). Players without a body of their own use the default body. Every body
has the same skeleton layout, so all animations play on every body (see
[Animation](../../how-it-works/animation/)).

On top of the body, each player has an **appearance** with the textures and colors of its parts.
Anything a player's appearance leaves empty is taken from the **base appearance**, so a new
player often only needs a few colors and textures.

| Part | Texture | Color |
|---|---|---|
| Body (skin and face) | skin texture | skin tint |
| Shirt, shorts, shoes | ✓ | tint (multiplies the texture; a plain color without one) |
| Hair | strand shape (alpha) | hair color |
| Racket | frame texture, strings texture | — |

The appearances are in `scenes/player/resources/appearances/`; open one in Godot's inspector to
see all fields. A player's body is set in their player data (`scenes/player/resources/data/`).

## Creating a player model

Players are made with **MPFB**, the MakeHuman add-on for Blender, which builds realistic people
with a ready rig.

{{% steps %}}

### Install Blender and MPFB

Install [Blender](https://www.blender.org/download/) (4.0 or newer). In Blender, open
**Edit → Preferences → Extensions**, search for **MPFB**, install and enable it.

### Install the MakeHuman assets

Download the
[system assets](https://files2.makehumancommunity.org/asset_packs/makehuman_system_assets/makehuman_system_assets_cc0.zip)
(CC0). In the MPFB side panel, go to **Settings → Assets** and point it at the ZIP file (no need
to unpack it).

### Start from the base player

Open
[`player/base_player.blend`](https://github.com/mbkma/pelota-files/raw/refs/heads/main/player/base_player.blend)
from pelota-files and select the human. It already has the game's rig and proportions.

### Shape the person

In MPFB's **Model** tab, adjust body (height, weight, muscle), face and skin. For a real
player, work from photos of the front and the side.

### Dress them

In **Apply Assets**, choose clothes and hair. Keep the clothes as separate meshes: the game
colors and textures shirt, shorts and shoes independently.

### Bake the animations

The game rig (`game-rig`) copies the MPFB control rig with bone constraints. Bake the actions you
want in the game onto it, one NLA track per animation named `g_<animation>` (for example
`g_forehand`). The export mutes the constraints, so only the baked tracks count.

### Share it

Open a pull request on [pelota-files](https://github.com/mbkma/pelota-files) with your `.blend`
file and a few renders, and describe the player. See the
[MPFB documentation](https://static.makehumancommunity.org/mpfb.html) for more.

{{% /steps %}}

## Getting a player into the game

Bodies and animations are exported with a script, never edited by hand in Godot. Everything
Godot needs to do with them (the skeleton mapping, the racket and head attachments, the animation
markers) happens on import, so exporting again is all it takes to update a player.

{{% steps %}}

### Add the player to the export list

In `tools/blender/player_assets.json`, add the body: the `.blend` file, the name of its rig, the
output file (`assets/models/players/<name>/<name>.glb`) and which Blender object is which mesh
slot (`Body`, `Shirt`, `Shorts`, `Shoes`, `Hair`; further meshes such as the eyes keep any name).

### Export

```sh
blender -b --python tools/blender/export_player_assets.py -- <name>
```

Without a name, every body and animation set in the list is exported. Paths in the list are
relative to the game's project folder, with pelota-files checked out next to it. The `.blend`
file is only read, never saved.

### Set up the import once

For a new body, open the exported `.glb` in Godot's import dock. Under **Skeleton → Retarget**,
set the bone map to `scenes/player/rig/game_rig_bone_map.tres`, and set the import script to
`scenes/player/rig/player_body_import.gd`. Use the existing materials in `assets/materials/` for
the meshes, then reimport. These settings are kept in the `.glb.import` file next to it, so
later exports reimport on their own.

### Give the player their body

Set the `.glb` as **Body** in the player's data.

{{% /steps %}}

## Rackets

All rackets share one model with two surfaces: the **frame** and the **strings**. A racket design
is just two textures painted on its UV layout. Start from `head_racket.png` and
`head_strings.png` in `assets/models/racket/textures/`. Each player's appearance names their two
racket textures; the player's racket and the spare rackets on their bench both show them.

## The stadium and props

The crowd models are Blender files in pelota-files. When you change
one, export it into the game's `assets/models/` folder (keeping the file name), bake the crowd
again (`scenes/environments/crowd/baker/crowd_baker.gd`, see the top of the file; a new person
also goes into `scenes/environments/crowd/spectators.tres`) and check it in the match scene: the TV camera view and a walk around the court with the free camera (press
<kbd>1</kbd> during a match to cycle cameras).

The stadium itself, Arthur Ashe Stadium, is built from code by
`scenes/environments/us_open/arthur_ashe/arthur_ashe_builder.gd`: its sizes, colors and shapes
are constants and functions there. Change them and run the builder again (see the top of the
file) to regenerate the stadium, its seats and the crowd's seating. The sponsors' logos are one
texture atlas, `scenes/environments/us_open/sponsor_logos.png`, listed in `us_open_logos.gd`
next to it. The court with its net (`scenes/court/court_model_builder.gd`), the umpire chair
(`scenes/match/umpire/umpire_chair_builder.gd`) and the TV cameras
(`scenes/environments/us_open/cameras/broadcast_camera_builder.gd`) are built from code the
same way.

The **props at court level** are scenes placed by hand in
`scenes/environments/us_open/stadium.tscn`, under `Courtside`: the benches (mat, box, chair),
towels, water bottles, tennis bags (pick the brand in the inspector) and the spare rackets, and
the cameras on the TV camera platforms (`PlatformCameras`). Select them in the editor to move,
turn, copy or delete them; rebuilding the stadium does not touch them. Their meshes come from
`scenes/environments/us_open/props/courtside_props_builder.gd` (see the top of the file). The
photographers' and the TV camera operators' places are **prop rows**: one node whose children
(markers) are the places, drawn as a single instanced mesh however many there are, and the crowd
seats a person at each. Move, copy or delete a marker and the photographer follows.

**Racket designs** in the look of current pro racquets (from Babolat, HEAD, Wilson, Yonex,
Tecnifibre, Dunlop and Diadem) are resources in `scenes/player/racket/designs/`: the brand, the
model and a frame and a strings texture (in `assets/models/racket/textures/designs/`). Every
player plays one (see [Updating the players](../code/#updating-the-players)); the player's bench
shows it, with a bag of its brand. The textures are painted by
`pelota-files/racket/make_racket_designs.py` onto the racket model's texture layout: change a
design's colors there, or add one, and run it again.

Keep an eye on **performance**: the stadium is on screen all the time, and the crowd has
thousands of people. Prefer fewer, larger textures, simple materials, and no hidden geometry.

## The umpire's voice

The umpire's calls are spoken by [Kokoro](https://github.com/hexgrad/kokoro), a text to speech
model: the scores, deuce, advantage, game, set and match, the tiebreak scores, let, and the
electronic "Fault" and "Out", plus every player's last name as its own clip. They are made by
`pelota-files/sounds/umpire/make_umpire_calls.py` (see the top of the file for how to run it),
which writes the clips into `assets/sounds/effects/umpire/` and the calls resource
`scenes/match/umpire/umpire_calls.tres`; after adding players, run it and then the roster builder,
which gives each player their name clip. A name said wrong can be respelled there. The voice
sounds like the stadium's speakers through the effects on the **Umpire** audio bus: a
loudspeaker's frequency range and a quiet, open-air reverb.

## Adding a new player to the roster

Every player is a data file in `scenes/player/resources/data/` with their name, country, hand,
height and rank, plus three linked resources: their **stats**, **play style** and **appearance**.
Copy an existing player's files, change them, and the new player shows up in the menus
automatically, sorted by rank.
