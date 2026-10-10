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

Strokes are animations on the game's player rig, stored in `scenes/player/animations/`. Today
there are forehands and backhands for low, normal and high balls, an open-stance forehand, a
slice and the serve; volleys, drop shots and more variety are very welcome. Each stroke needs:

{{% steps %}}

### A hit marker

Add an animation **marker** named `hit` at the frame where the racket meets the ball. The game
starts the swing so that this marker lines up with the ball (and speeds up the swing when the
player is late). A serve also needs a `toss` marker, where the ball leaves the hand.

### A contact point

In the player model (`scenes/player/model.tscn`), under **Points**, each stroke has a marker
(a *stroke clip*) placed where the racket meets the ball in that animation, relative to the
player. Play the animation to the hit marker and put the point at the racket's sweet spot. For
high and low balls, add separate versions (like *forehand up* and *forehand down*). The game
picks the one closest to the ball's height.

### A slot in the animation tree

Add the clip to the stroke selection (the *StrokeSelect* node) in
`scenes/player/animations/player_animation_tree.tres`, so the game can play it as a stroke on
top of the running.

{{% /steps %}}

Tips:

- **Real timing matters.** A pro forehand takes about 0.5 s from the start of the forward swing to
  contact. A slower swing looks sluggish, and the game has to speed it up more often (whenever the
  player is a little late).
- **Keep the feet honest.** The stroke plays on top of the running, so a stroke that steps
  forward should do so in the direction the player moves.

## Motion capture and Mixamo

Locomotion comes from motion-captured animations (the Mixamo locomotion pack), **retargeted**
onto the game's rig. To add or replace one:

{{% steps %}}

### Put the file in the import folder

Copy the `.fbx` (exported *without skin*, 30 fps) into
`assets/models/player/mixamo_locomotion/`.

### Set the import options

In Godot's import dock, under **Skeleton → Retarget**, set the bone map to
`mixamo_bone_map.tres` and keep the unmapped bones' tracks. Set the import script to
`mixamo_locomotion_import.gd`, then reimport.

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
- **Contact:** in slow motion, the racket really meets the ball at the hit marker.

Add a short clip or a strip of screenshots to your pull request.
