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

A player is one shared skeleton with **modular parts**: a body, a shirt, shorts, shoes, hair and a
racket. Each player has an **appearance** that picks the meshes, textures and colors for these
parts. Anything a player's appearance leaves empty is taken from the **base appearance**, so a
new player only needs what makes them different, often just a few colors and textures.

| Part | Mesh | Texture | Color |
|---|---|---|---|
| Body (skin and face) | ✓ | skin texture | skin tint |
| Shirt, shorts, shoes | ✓ | ✓ | tint (multiplies the texture; a plain color without one) |
| Hair | ✓ (hair cards) | strand shape (alpha) | hair color |
| Racket | shared | frame texture, strings texture | — |

The appearances are in `scenes/player/resources/appearances/`; open one in Godot's inspector to
see all fields.

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

In **Apply Assets**, choose clothes and hair. Keep the clothes as separate meshes. The game swaps
shirts, shorts and shoes independently.

### Share it

Open a pull request on [pelota-files](https://github.com/mbkma/pelota-files) with your `.blend`
file and a few renders, and describe the player. See the
[MPFB documentation](https://static.makehumancommunity.org/mpfb.html) for more.

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
