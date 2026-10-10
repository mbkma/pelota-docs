---
title: Animation
weight: 5
---

**Short version:** the players are moved by recorded motion: running and walking captured from
real people, and tennis strokes. These animations were made for other skeletons, so the game
**retargets** them onto its players. While running, several running animations are **blended**
by speed and direction, all kept in step so the feet never slide. A stroke plays **on top** of
the running and is started at exactly the right moment, so that the racket arrives when the
ball does.

{{< fig src="images/screenshots/run-cycle-side.jpg" caption="One running cycle, seen from the side. The arm swings like in the recorded run, while the racket stays in the hand and points forward." >}}

## The skeleton and retargeting

Every player has the same skeleton: a humanoid rig with about 150 bones, including fingers and a
special bone in the right hand that holds the racket.

Animations from elsewhere (for example the motion-captured locomotion) use other skeletons, with
other bone names and other rest poses. Godot's **retargeting** maps both onto a common humanoid
profile (hips, spine, upper arm, …), so an animation made for one humanoid can play on another.
The import of these animations then fixes what retargeting alone cannot:

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

Each stroke animation has a marker named **hit** at the moment the racket meets the ball. For
example, the forehand below hits at 0.567 s. Each stroke also has a **contact point**: where,
relative to the player, the racket meets the ball in that animation. There are several versions
for high and low balls (for example *forehand up* and *forehand down*), and the game picks the
one closest to the height of the ball.

{{< fig src="images/screenshots/forehand-sequence.jpg" caption="The forehand: ready, backswing, just before contact (0.55 s), follow-through, finish, recovery." >}}

When the ball is coming, the game predicts when it reaches the contact point. The swing starts
exactly so long before that as the hit marker is into the animation. If the player is late, the
swing is played faster (up to 1.8 times), and if even that is not enough, it starts part of the
way through, with a shortened backswing.

{{< fig src="images/plots/swing_timing.svg" caption="Three swings ending at the same contact: on time, late (sped up), and very late (backswing cut short)." >}}

While the stroke plays on top, the legs keep running underneath.

{{< callout type="info" >}}
**In the code:** `scenes/player/player_animator.gd` (blending, cadence, strokes and markers),
`scenes/player/player.gd` (when to start a swing), `scenes/player/model.gd` and its stroke
contact points, `assets/models/player/mixamo_locomotion/mixamo_locomotion_import.gd` (the import
steps above). [Animators](../../contribute/animation/) describes how to add new animations.
{{< /callout >}}
