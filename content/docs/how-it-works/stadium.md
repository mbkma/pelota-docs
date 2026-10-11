---
title: Stadium and broadcast
weight: 10
---

**Short version:** the match is filmed like a TV broadcast. The main camera behaves like the one
at a real tournament, the stadium shows a serve clock, serve speeds and the match time, the crowd
cheers exciting points, and the players get visibly sweaty as the match goes on.

## The TV camera

The main camera stands on a platform in the stands behind one baseline, exactly where the main
camera of the US Open 2025 final stood: its position, angle and zoom were calibrated from the
broadcast by matching the court's lines in a frame of the final. The court level around it was
measured from the same frame, so the TV picture lines up with the real one:

- The match **opens** with a wider shot tilted up toward the crowd, then zooms in to the
  standard shot.
- **Before a serve**, if the returner is on the camera's end (standing far back), the camera
  widens a little to keep them in the picture, and settles back shortly after the serve.
- During rallies it **holds still**. Between points it now and then reframes slightly, as a
  camera operator would.

Press <kbd>1</kbd> during a match to cycle through the other cameras.

## The score panel

The score panel in the bottom left is the one of the US Open 2025 broadcast: a row per player
with their seed, name and country, the yellow swoosh at the server, the games of every set
(yellow for the set's winner) and the points in a white box. Points change at once, as on TV;
when a new set begins the panel widens. Between points it sometimes shows more:

- a **caption** on a yellow tab that slides up from behind the panel: "BREAK POINT", "SET
  POINT", "CHAMPIONSHIP POINT" or "DEUCE", numbered when it happens again in the game ("BREAK
  POINT #2"; championship points are counted over the match). At the start it names the
  stadium.
- now and then, when nothing is at stake, an **IBM statistic**: the scores wipe away, the panel
  widens, and the two players' values fade in under a title like "BREAK POINTS WON", "1ST SERVE
  IN", "ACES" or "LAST 10 POINTS". After six seconds it all reverses.

## Courtside cameras

Three TV cameras stand at court level next to the net, in the pit behind the ad boards on the
right of the main camera: one looks across the court, and two turn to follow the player on their
end. Like the real ones at the US Open, they are low on tripods and wrapped in boxy blue rain
covers, with only the lens hood, the viewfinder and the pan bars showing. Their front lens glass
is a small shader that reflects the stadium tinted by a lens coating, whose color shifts from
green to purple as you look at it from the side.

{{< fig src="images/screenshots/broadcast-camera-lens.jpg" caption="A courtside camera: the coated front lens reflects the sky and the stadium." width="560px" >}}

## Benches and the umpire chair

Each player's bench is a white chair and a navy box on a mat, next to the umpire chair; the
spare rackets on it are in the same design as the racket the player plays with. The umpire sits
high on a navy chair with Polo and Chubb panels, a small desk with a microphone and a sunshade.

{{< fig src="images/screenshots/bench-rackets.jpg" caption="Two benches, two players, two racket designs." >}}

## Players who sweat

The longer the match, the more the players sweat, following the [match clock](../match-flow/#the-match-clock):
from a warmed-up 10% at the start to fully soaked after 90 minutes of match time.

{{< fig src="images/plots/sweat.svg" caption="Sweat by match time." width="520px" >}}

- **Skin** gets shinier: a thin wet film (clearcoat) and a smoother surface.
- **The shirt** soaks through in patches: down the spine, on the chest, under the arms and in a
  band around the collar. The patches grow with the sweat and have uneven edges, and they stay
  on the cloth however the player moves.
- **Drops**, faint and see-through, now and then fly off the head in a short burst, but only
  when the player is tired (stamina below 35%) and running; more often the more tired, the
  sweatier and the faster.

{{< fig src="images/screenshots/sweat-dry-and-soaked.jpg" caption="Dry (start of the match) and soaked (after 90 minutes), front and back." >}}

## Arthur Ashe Stadium

The match is played in a model of Arthur Ashe Stadium, the US Open's center court, with almost
23,000 seats. Like the real one, it rises in rings around the court:

- the **court**, as at the US Open: blue inside the lines and green around them, with the net
  a singles net between posts inside the doubles alleys (no singles sticks), Cadillac crests
  near its ends, and "The world's healthiest sport" painted beside the court;
- the **court level**: a tall blue wall behind each baseline, from stand to stand, with the
  sponsors' logos, the IBM serve speed panel, the Rolex clock showing the match time and the
  serve clocks in its top corners; and straight, low ad boards along the sides, ending short of
  the walls so people can walk through at the corners. On the left of the main camera the
  courtside seats begin right behind the board; on the right a pit runs at court level, where
  the photographers sit with their long lenses along the whole court and the TV cameras stand
  next to the net;
- the **lower bowl**: a first tier, a cross aisle, and a second tier behind a terracotta wall,
  with the TV camera platforms behind both baselines;
- two rings of **suites** with glass fronts and small balconies under blue fascias with the
  sponsors' logos and a glowing LED ribbon;
- the steep **upper bowl** up to the rim, and the brick facade outside;
- the **roof**: a fixed ring around the open middle, carried by trusses with lights, speakers,
  video boards and the flag hanging from them, and the two retractable roof panels, parked
  open over the long sides on four huge trusses.

Everything follows one shape: the court's rectangle with rounded corners, each corner made of
four straight facets. Rows, aisles, fascias and the roof are all placed by how far out they are
from the field wall, so they follow the bowl as it widens.

## The crowd

Every seat can hold a spectator: the crowd fills the stadium's seats, about nine in ten of them,
with spectators of six different people in many clothes colors. Each section of seats is one
block, drawn with one draw call per person model, and far blocks automatically use simpler
models. Everybody cheers after a point: louder for long rallies and big points.

{{< callout type="info" >}}
**In the code:** `scenes/environments/us_open/` (stadium, `arthur_ashe/arthur_ashe_builder.gd`
builds the stadium, cameras: `cameras/tv_camera.gd`,
`cameras/broadcast_camera.tscn`, `cameras/lens_glass.gdshader`), `scenes/player/model.gd` and
`scenes/player/sweat_patches.gdshader` (sweat), `scenes/environments/crowd/` (crowd).
{{< /callout >}}
