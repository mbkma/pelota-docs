---
title: Movement
weight: 4
---

**Short version:** players run fastest toward the net, a bit slower sideways and slowest when
backpedaling while still facing the net. For more than a step or two back they turn around and
run, and then they are fast again. They speed up and slow down like athletes: a 5 m sprint takes
about a second.

{{< fig src="images/plots/speed_by_direction.svg" caption="Top speed of an average player by direction. Facing the net, sideways is 80% and backpedaling 70% of the forward speed. Turned around, running back is full speed." width="460px" >}}

## Speed and acceleration

| | Average player |
|---|---|
| Top speed toward the net | 5.6 m/s (20 km/h) |
| Sideways | 80% of it |
| Backpedaling (facing the net) | 70% of it |
| Acceleration | 11 m/s² |

The player's stats scale these values: *top speed* from 85% to 120%, *acceleration* and *agility*
together from about 70% to 140%. Stamina lowers them as the player tires (see
[Stamina and player stats](../stamina-and-stats/)).

**Changing direction** sharply (more than about 30°) costs acceleration for a short moment.
Agile players lose less.

**Arriving** at a target, the player brakes in time to stop there instead of overshooting. The
target speed is never more than the speed from which they can still stop at 8 m/s².

## Backpedaling or turning around

Moving backward faster than **3.5 m/s**, within about 60° of straight back, the player turns
around and runs. Below **2.8 m/s** they face the net again and backpedal. So a step or two back
to meet a ball (which peaks at about 3 m/s) is backpedaled, and a long run back for a lob is a
real turn-and-run.

The body turns, but the player's "front" for the strokes stays toward the net: when a stroke
starts, the body snaps back to face the net, so the swing meets the ball where it should.

## Getting to the ball

When the opponent hits, the controller looks at the ball's predicted flight and picks where to
meet it (see [Hitting the ball](../hitting/#early-or-late-the-contact-window)). From there it
knows where the player must stand, so that the stroke's contact point lands on the ball. For
every possible meeting point it checks whether the player gets there **and is set** 0.25 s
before the ball arrives (0.2 s for a volley). If not, it picks the closest point that works, or
if none does, the one where the player is least late.

A human player then has to do most of the running themselves: once the shot button is pressed,
the automatic movement only jogs at 75% speed.

{{< callout type="info" >}}
**In the code:** `scenes/player/movement_controller.gd` (speed by direction, acceleration,
braking, reach time), `scenes/player/player.gd` (turning to run back),
`scenes/player/controllers/controller.gd` (choosing where to meet the ball).
{{< /callout >}}
