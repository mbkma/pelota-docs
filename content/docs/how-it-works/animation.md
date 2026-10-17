---
title: Animation
weight: 5
---

**Short version:** the players are moved by recorded motion: running and walking captured from
real people, and tennis strokes. All of them are **retargeted** onto one common skeleton, so they
play on every player's body. While running, several running animations are **blended** by speed
and direction, all kept in step so the feet never slide. A stroke plays **on top** of the
running: it is prepared early, held, and swung so that the racket arrives when the ball does,
and the arm reaches a little for a ball the swing would just miss.

{{< fig src="images/screenshots/run-cycle-side.jpg" caption="One running cycle, seen from the side. The arm swings like in the recorded run, while the racket stays in the hand and points forward." >}}

## The skeleton and retargeting

Every player's body is a humanoid rig, and each body may have its own proportions. On import,
Godot's **retargeting** maps the rig onto the game's **skeleton profile**
(`scenes/player/rig/pelota_skeleton_profile.tres`): the standard humanoid bones (hips, spine,
upper arm, …) plus a few more that matter for tennis: the bone in the right hand that holds the
racket (`RacketGrip`), the twist bones of arms and legs, and helper bones at the shoulders and
hips. Animations keep only the profile's bones, so every animation plays on every body.

Animations from elsewhere (for example the motion-captured locomotion) use other skeletons, with
other bone names and other rest poses; retargeting maps them onto the same profile. The import of
these animations then fixes what retargeting alone cannot:

{{< fig src="images/diagrams/animation_import.svg" caption="The import steps that turn a recorded animation into a game animation." >}}

- **Rest pose:** the recorded skeleton stands in a T-pose (arms straight out), the players in an
  A-pose (arms down at an angle). Copying rotations alone would put the arms through the body,
  so every bone is turned to *point the same way* as in the recording.
- **Root motion:** the recordings walk forward through space. The game removes that travel,
  because the game itself moves the player. The animation only makes the body *look* like it
  runs.
- **The racket hand:** the right hand keeps the grip from the tennis ready pose, with the fingers
  around the handle. Its wrist is turned so the racket points forward and slightly up at the
  middle of the arm swing, and it takes up half of the swing so the racket head stays clear of
  the legs.

## The animation tree

{{< fig src="images/diagrams/animation_tree.svg" caption="The animation tree: the locomotion blends the running; a stroke plays on top." >}}

### Blending the running

The blend space places each running animation at the speed and direction it was recorded at.
The game feeds in the player's actual velocity, and the animations around that point are mixed.
Below walking speed, the standing (idle) animation fades in.

{{< fig src="images/plots/blend_space.svg" caption="The eight locomotion clips, placed by their real speed. Running diagonally forward right mixes the forward run and the sideways run." width="520px" >}}

### Keeping the feet in step

Mixing a walk and a run only works if both are at the same point of the step: left foot down in
one while the right foot is down in the other would look like a stumble. So every clip is cut
to exactly **one step cycle**, stretched to **1 second**, and starts at the moment the **left
foot touches down**. Played together in sync, all clips always agree on which foot is down.

{{< fig src="images/plots/gait_cycle.svg" caption="The walk took 1.03 s and the run 0.70 s per step cycle. Both are stored as 1 s cycles starting at the left foot's touchdown." >}}

How fast the cycle plays (the **cadence**) follows the running speed: between the walk's and the
run's own step rate, and beyond the run a little faster still. Longer strides do the rest, just
like a real runner.

{{< fig src="images/plots/cadence.svg" caption="Step cycles per second by running speed." width="560px" >}}

## Strokes that meet the ball

Each stroke animation has a marker named **hit** at the moment the racket meets the ball, and a
marker named **swing** where the racket is taken back the farthest and the forward swing starts.
Where the racket meets the ball, the **contact point**, comes from the animation itself: the
game poses the player's skeleton at the hit marker and takes the middle of the strings. So it
fits every body and every version of the animation.

{{< fig src="images/screenshots/forehand-sequence.jpg" caption="The forehand: ready, backswing, just before contact, follow-through, finish, recovery." >}}

### Blending by height

There are several versions of a stroke for different heights (for example *forehand down*,
*forehand* and *forehand up*). The game blends the two whose contact points lie around the
ball's height, so the racket meets a ball at any height in between. Both animations play on a
common timeline: their markers are matched, and each plays at its own pace between them.

### Prepare, hold, swing

When the ball is coming, the game predicts when it reaches the contact point. Well before the
swing would have to start, the player **prepares**: turns and takes the racket back to the swing
marker, and **holds** it there while still running into position. When the ball is only as far
away as the forward swing takes, the swing starts and reaches the hit marker with the ball, at
its natural speed. If the ball comes faster, the preparation plays faster (up to 1.5 times) and
starts later in the animation, skipping its quiet start, so the turn and the forward swing are
always seen. Only a ball that leaves less time than the forward swing takes speeds the swing
itself up (up to 1.8 times), and only if even that is not enough does it start part of the way
through.

While the player runs during the preparation, the legs and hips keep running underneath, in
the direction the player runs; the spine takes over the turn of the stroke's hips, so the
shoulders stay turned as in the stroke. From the forward swing on, the stroke's own footwork
takes over. A player who only creeps (slower than 0.4 m/s)
does not step at all.

### The serve

The server holds the ball in the left hand. At the **toss** marker, with the arm almost
stretched, the ball leaves the hand: thrown so high that it falls 35 cm from its highest point
before the racket meets it. The serve waits in the trophy position (its **swing** marker) until
the falling ball is only one forward swing away.

### Reaching for the ball

The player rarely stands exactly where the swing meets the ball. Around contact, the racket arm
**reaches** for the ball: the elbow bends or stretches and the shoulder turns, by up to 45 cm,
so the strings meet the ball the swing alone would miss. How well the player stood still decides
how good the shot is; the reach only shows it. The head follows the ball all the time.

{{< callout type="info" >}}
**In the code:** `scenes/player/player_animator.gd` (blending, cadence, the stroke clock and its
markers), `scenes/player/swing_timer.gd` (preparing, holding and swinging), `scenes/player/model.gd`
(the body, contact points, height blends, reach and head), `scenes/player/rig/` (the skeleton
profile, the import scripts and the reach), `tools/blender/export_player_assets.py` (the export
from Blender). [Animators](../../contribute/animation/) describes how to add new animations.
{{< /callout >}}
