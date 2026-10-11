---
title: Ball physics
weight: 2
math: true
---

**Short version:** the ball is pulled down by gravity, slowed by the air and pushed up or down
by its spin. When it lands, it bounces back up with less speed; topspin makes it kick forward
and higher, backspin keeps it low. It can clip the net cord and dribble over, or run into the
net. The game computes all of this itself, step by step, so it can also **predict** where a
ball will go.

{{< fig src="images/plots/ball_trajectories.svg" caption="Three shots from the same spot, all landing 2.5 m inside the far baseline. The heavy topspin shot clears the net highest and still comes down in; after the bounce it kicks up highest. The slice flies slower and stays lower after the bounce." >}}

## Forces in flight

Every physics step (about 60 times per second, and 240 times per second when the game works out
how to aim a shot), the ball's velocity changes by:

- **Gravity**: 9.81 m/s² downward.
- **Spin**, which acts more on a fast ball than on a slow one:
  - **topspin** pushes the ball *down*, up to 15 m/s² at full spin, so it dips into the court;
  - **backspin** pushes it *up*, but at most 5 m/s², because a slice spins slower than a topspin
    drive;
  - **sidespin** curves the ball sideways, up to 8 m/s².
- **Air drag**, which slows the ball the more the faster it is.

In formulas, with spin \(s\) between −1 and 1 and the speed factor \(f = \min(|v| / 40, 1)\):

$$
a_y = -g - s_y \, a_{\text{spin}} \, f
\qquad
v \leftarrow \frac{v}{1 + c_d \, |v| \, \Delta t}
$$

where \(a_{\text{spin}}\) is 15 m/s² for topspin and 5 m/s² for backspin, and \(c_d = 0.02\).

## The bounce

When the ball reaches the ground:

- It keeps **60–78%** of its downward speed, going back up. A gentle impact keeps more than a
  hard one, like a real ball.
- It keeps **88%** of its forward speed (friction with the court).
- **Topspin** kicks it forward and a little higher; **backspin** holds it back and keeps it low;
  **sidespin** kicks it sideways.
- The ball keeps 60% of its spin.

A ball that lands very softly (slower than 0.6 m/s downward) does not bounce anymore. It rolls
and slows down.

## The net

The net cord hangs from 1.07 m at the posts of the singles net, inside the doubles alleys, to 0.914 m in the middle. When the ball crosses
the net:

- **Above the cord**: nothing happens.
- **Just touching the cord**: it pops up a little, loses about half its speed and dribbles over.
  On a serve that lands in, this is a *let* and the serve is replayed.
- **Into the net**: it drops back on the hitter's side.

## Predicting the flight

Because the game runs the same steps for the real ball and for a prediction, the predicted
flight matches the real one to within a few centimeters. The prediction is a list of points, each with a position, a time and how many
times the ball has bounced since it was hit. Everything that needs to know the future uses it:

- the players, to find where and when to meet the ball;
- the swing, to start the animation so the racket arrives at the right moment;
- the AI, to judge how deep and how high a ball comes.

## Aiming: how a shot finds its target

A player decides *where* the ball should land and *how fast* it should go forward. The game then
finds the rest:

1. Guess a sideways and an upward speed.
2. Simulate the flight and see where the ball lands.
3. Correct the sideways speed by the sideways miss, and the upward speed by the depth miss.
4. Repeat until the ball lands within 3 cm of the target (at most 12 times).

Then it checks the **net**: if the ball would pass lower than the wanted clearance over the cord
(15 cm for groundstrokes, 3 cm for serves), the shot is hit 10% slower, which means a higher and
safer arc, and solved again. A real player does the same thing when a ball is too low to drive
flat.

{{< callout type="info" >}}
**In the code:** `scenes/ball/ball.gd`: flight (`_advance_velocity`), bounce (`_touch_ground`),
net (`_collide_with_net`), prediction (`predict_trajectory`) and aiming (`calculate_velocity`).
The plot above is drawn by `tools/plots/make_plots.py` in this documentation, which repeats the
same formulas.
{{< /callout >}}
