---
title: Animation
weight: 3
---

Good animation makes the difference between a player who moves and one who *plays tennis*.
Read [how the animation system works](../../how-it-works/animation/) first; this page is the
practical guide.

## What the game needs

| Kind | Examples | Requirements |
|---|---|---|
| **Locomotion** | walk, run, side steps, backpedal, split step | A clean, looping step cycle, recorded in place or moving forward (the import removes the travel) |
| **Strokes** | forehand, backhand, slice, volleys, drop shots, serve | Starts and ends near the ready pose; one clear moment of contact |
| **Others** | celebrations, walking between points, toweling | Start and end in the idle pose |

## Strokes

Strokes are baked on the game rig in Blender (see
[Creating a player model](../art/#creating-a-player-model)) and exported as an **animation set**
with `tools/blender/export_player_assets.py`. The import keeps only the bones of the game's
skeleton profile, so a stroke plays on every player's body. Today there are forehands and
backhands for low, normal and high balls, an open-stance forehand, a slice and the serve;
volleys, drop shots and more variety are very welcome. Each stroke needs:

{{% steps %}}

### An entry in the import list

`scenes/player/animations/base_animations_import.tres` lists the animations of the set the game
uses: the name in the exported file, the name in the game, whether it loops, and its markers.
Exporting again keeps all of this.

### Markers

- `hit`: the moment the racket meets the ball. The game times the swing so that this marker lines
  up with the ball.
- `swing`: the racket taken back the farthest, where the forward swing starts. The game prepares
  the stroke early, holds it here while the player gets in position, and starts the forward swing
  so it reaches `hit` with the ball.
- `toss` (serve only): the ball leaves the hand, with the tossing arm almost stretched. For the
  serve, `swing` is the trophy position, where it waits for the toss to fall.

Strokes that are blended with each other (for example *forehand down*, *forehand* and *forehand
up*) need the same markers.

### A stroke clip

In the player model (`scenes/player/model.tscn`), add a stroke clip to **Stroke Clips**: the
animation and the stroke types it plays. You do not place a contact point: the game works out
where the racket's sweet spot is at the `hit` marker, on each player's body. Clips of the same
stroke type are blended by the height of the ball.

### A slot in the animation tree

Add the animation to both stroke selections (the *LowSelect* and *HighSelect* nodes) in
`scenes/player/animations/player_animation_tree.tres`.

{{% /steps %}}

Tips:

- **Real timing matters.** A pro forehand takes about 0.15 to 0.25 s from the start of the forward
  swing (`swing`) to contact (`hit`). A slower forward swing looks sluggish, and the game has to
  speed it up whenever the player is late.
- **The preparation can be long.** Everything before `swing` can be held and sped up, so a full
  unit turn is welcome.
- **The legs may run.** While the player is moving, the legs of the running animation replace the
  stroke's, so the upper body has to work on a running player as well as on one who stands.

## Motion capture and Mixamo

Locomotion comes from motion-captured animations (the Mixamo locomotion pack), **retargeted**
onto the game's rig. To add or replace one:

{{% steps %}}

### Put the file in the import folder

Copy the `.fbx` (exported *without skin*, 30 fps) into
`assets/models/animations/mixamo/`.

### Set the import options

In Godot's import dock, under **Skeleton → Retarget**, set the bone map to
`scenes/player/resources/mixamo_bone_map.tres` and keep the unmapped bones' tracks. Set the
import script to `scenes/player/rig/mixamo_locomotion_import.gd`, then reimport.

### Name the output

Add the file to the table at the top of the import script, with the name of the game animation
it becomes (and, for walks and runs, of the backward version it makes by playing it in reverse).

### Place it in the blend space

Add the new clip to the locomotion blend space in `player_animation_tree.tres`, at the speed and
direction it was recorded at. The import stores that speed on the clip (`travel_speed`).

{{% /steps %}}

The import script does the rest: it fixes the rest pose, removes the root motion, puts the
racket in the hand and cuts one step cycle starting at the left foot's touchdown, so the new clip
blends in sync with all the others.

## Checking your work

Watch your animation in a match and in training, from the TV camera and up close. Check:

- **Feet:** no sliding when running at different speeds and directions.
- **Racket:** firmly in the hand; never through the body or legs.
- **Contact:** in slow motion, the racket really meets the ball at the hit marker. The arm reaches
  a little for a ball the swing would miss; if it reaches a lot, the stroke's contact height or
  timing is off.

Add a short clip or a strip of screenshots to your pull request.
