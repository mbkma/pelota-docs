---
title: The court
weight: 1
---

**Short version:** the net is at the center of the world, the court runs along the **z** axis,
sideways is **x**, and up is **y**. One player plays on the positive z half, the other on the
negative half.

{{< fig src="images/plots/court.svg" caption="The court seen from above, with the game's axes and line positions." width="480px" >}}

## Directions

| Axis | Direction | Notes |
|---|---|---|
| **x** | sideways | 0 is the middle of the court |
| **y** | up | 0 is the court surface |
| **z** | along the court | 0 is the net; one player is on z > 0, the other on z < 0 |

Because everything is measured from the net, many rules become simple: a ball is "on my side"
when its z has the same sign as my position, and "how deep" a ball is means simply how far its z
is from 0.

## Dimensions

| Line | Distance |
|---|---|
| Net height | 0.914 m in the middle, 1.065 m at the posts |
| Service line | 6.40 m from the net |
| Baseline | 13.0 m from the net |
| Singles sideline | 4.115 m from the middle |

{{< callout type="warning" >}}
A real court's baseline is 11.89 m from the net; the game currently uses 13.0 m. Many tuning
values (where players stand, how deep shots go) are built around the game's value.
{{< /callout >}}

## Facing and "left/right"

Players always face the net. A ball on the player's right (as they look at the net) is played
with a forehand, a ball on their left with a backhand. For the player on the positive z half,
their right is the positive x side.

Your controls follow the screen instead: pushing "up" moves you up the screen. The game turns
your input by the camera's direction, so the controls feel the same at both ends of the court.

{{< callout type="info" >}}
**In the code:** `scripts/core/game_constants.gd` (court dimensions), `scenes/court/court.gd`
(court regions used for in/out decisions).
{{< /callout >}}
