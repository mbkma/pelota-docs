---
title: Stadium and broadcast
weight: 10
---

**Short version:** the match is filmed like a TV broadcast. The main camera behaves like the one
at a real tournament, the stadium shows a serve clock, serve speeds and the match time, the crowd
cheers exciting points, and the players get visibly sweaty as the match goes on.

## The TV camera

The main camera stands high behind one baseline, like the main camera of a real tennis broadcast
(its framing was measured from US Open 2025 footage):

- The match **opens** with a wider shot tilted up toward the crowd, then zooms in to the
  standard shot.
- **Before a serve**, if the returner is on the camera's end (standing far back), the camera
  widens a little to keep them in the picture, and settles back shortly after the serve.
- During rallies it **holds still**. Between points it now and then reframes slightly, as a
  camera operator would.

Press <kbd>1</kbd> during a match to cycle through the other cameras.

## Courtside cameras

Three broadcast cameras stand on the court's side: one next to the umpire, and two that turn to
follow the player on their end. They are modeled after real studio cameras on pedestals, with a
white box lens, a lens hood and red tally lights. Their front lens glass is a small shader that
reflects the stadium tinted by a lens coating, whose color shifts from green to purple as you
look at it from the side.

{{< fig src="images/screenshots/broadcast-camera-lens.jpg" caption="A courtside camera: the coated front lens reflects the sky and the stadium." width="560px" >}}

## Benches

Each player's bench has their spare rackets, in the same design as the racket they play with.

{{< fig src="images/screenshots/bench-rackets.jpg" caption="Two benches, two players, two racket designs." >}}

## Players who sweat

The longer the match, the more the players sweat, following the [match clock](../match-flow/#the-match-clock):
from a warmed-up 10% at the start to fully soaked after 90 minutes of match time.

{{< fig src="images/plots/sweat.svg" caption="Sweat by match time." width="520px" >}}

- **Skin** gets shinier: a thin wet film (clearcoat) and a smoother surface.
- **The shirt** soaks through in patches: down the spine, on the chest, under the arms and in a
  band around the collar. The patches grow with the sweat and have uneven edges.
- **Drops** fly off the head when the player runs; more the faster they run and the sweatier
  they are.

{{< fig src="images/screenshots/sweat-dry-and-soaked.jpg" caption="Dry (start of the match) and soaked (after 90 minutes), front and back." >}}

## The crowd

The stands are full of individual spectators in blocks. Only a share of them is animated (the
rest hold a still pose, which keeps large crowds cheap to draw), and everybody cheers after a
point: louder for long rallies and big points.

{{< callout type="info" >}}
**In the code:** `scenes/environments/us_open/` (stadium, cameras: `cameras/tv_camera.gd`,
`cameras/broadcast_camera.tscn`, `cameras/lens_glass.gdshader`), `scenes/player/model.gd` and
`scenes/player/sweat_patches.gdshader` (sweat), `scenes/environments/crowd/` (crowd).
{{< /callout >}}
