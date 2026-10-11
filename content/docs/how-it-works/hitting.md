---
title: Hitting the ball
weight: 3
---

**Short version:** every shot has a normal **rally speed** and an extra **attacking pace** on
top. Whether the attacking pace really comes through, and how precisely the ball lands, depends
on four things: **timing** (for a human player), **position** (was the ball in the racket's
sweet spot?), **readiness** (was the player set, and did the ball give them time?) and **how
early** the ball is taken.

{{< fig src="images/diagrams/hitting.svg" caption="What goes into a shot: two speeds, and what decides how much of them comes through." width="680px" >}}

## Shot speed

| Stroke | Rally speed | Extra attacking pace |
|---|---|---|
| Forehand | 33–38 m/s (119–137 km/h) | 10–14 m/s |
| Backhand | 31.5–36 m/s | 8–12 m/s |
| Slice | 22–26 m/s | 4 m/s |
| Drop shot | 9–13 m/s | none |
| Volley | 14–18 m/s plus 55% of the incoming ball's speed | 6 m/s on a high ball |

The ranges go from the weakest to the best player at that stroke. For example, a perfect
forehand of the best player reaches about 52 m/s (187 km/h). The rally speeds come from
Hawk-Eye tracking of the Australian Open: a pro's rally ball leaves the racket at about
125–130 km/h, crosses the net about 0.55 m above the cord and peaks at about 1.7 m.

## Timing (human player)

Releasing the shot button is the moment of truth. The **timing quality** is 1 inside the
perfect window just before contact and falls to 0 when the button is released 0.8 s or more too
early. The perfect window is 0.12 s for an average player. The player's *timing* stat widens or
narrows it (from 75% to 135%), and taking the ball early or late changes it too (see below).

{{< fig src="images/plots/timing.svg" caption="Left: timing quality by how long before contact the button was released. Right: what a shot gets at each quality. Perfect timing is a clear step up, not just a bit better." >}}

Perfect timing is its own tier. Compare a release just outside the window with a perfect one:

| | Worst timing | Just outside perfect | **Perfect** |
|---|---|---|---|
| Rally speed | 80% | 92% | **100%** |
| Attacking pace | 0% | 50% | **100%** |
| Spin | 85% | 105% | **130%** |
| Landing area radius | 2.5 m | 0.9 m | **0.25 m** |

The landing area is then scaled by the player's precision: shot control, mixed with the return
skill for a return of serve and the net game for a volley. Pressure reduces shot control (see
[Pressure and confidence](../mental-game/)).

Still holding the button when the racket meets the ball means the player just blocks the ball
back: a weak shot through the middle that lands about 6 m behind the net at 70–90 km/h.

The **AI** has no button to time. Its precision comes from its stats and play style instead.

## Position: the sweet spot

Every stroke animation has a **contact point**: where the racket meets the ball in that swing.
The closer the real ball passes to it, the cleaner the hit.

{{< fig src="images/plots/positioning.svg" caption="Within 15 cm of the contact point the hit is perfect; beyond 1 m the ball is missed." width="560px" >}}

A ball met off the sweet spot loses **control**. Less control means less of the attacking pace,
a shorter and flatter ball (down to 55% of the planned depth and 35% of the spin), and a bigger
random miss (up to 3 m).

## Readiness

The full attacking pace needs a **ready** player:

- **Set early:** the player was standing (moving slower than 1 m/s) for at least 0.5 s before
  contact.
- **Time from the ball:** a ball that reaches the player within 0.75 s of being hit (a hard
  drive or serve) leaves no time to attack; from 1.35 s on, there is plenty.

The worse of the two counts. So a hard ball can be returned, but not attacked.

## Deep balls

A ball bouncing near the baseline pushes the player back and rushes the shot. From 8 m behind
the net to the baseline the pressure rises from nothing to full. A fully deep ball takes away
35–60% of the control (less for players with good shot control) and all of the attacking pace.
For a serve, the same happens over the last 2.5 m before the service line.

## Fast balls

A fast ball is hard to control. A rally ball arrives at about 10–14 m/s; from 13 m/s on, the
pace takes away control, at 20 m/s (a hard first serve) 35–70% of it (less for precise players,
and on a return for good returners). So a big serve usually gets a weak return back: shorter,
slower and more scattered.

## Early or late: the contact window

After the bounce, the ball can be met anywhere in a **contact window**:

- the **early** end, on the rise at 0.8 m;
- the **standard** contact, as the ball drops through 1.1 m after the top of its bounce (or at
  the top, for a low bounce);
- the **late** end, as it drops to 0.5 m.

A player only moves back about a meter for a normal groundstroke, so the window ends where they
would have to move back further. A deep, high ball is then taken earlier and higher.

{{< fig src="images/plots/contact_window.svg" caption="Left: the player stands well behind the baseline and can take the ball early, standard or late. Right: the player stands near the baseline and a deep, high ball comes; the window ends 1 m behind them, so the ball is taken on the rise." >}}

The **earliness** of a contact is 1 at the early end, 0.5 at the standard contact and 0 at the
late end. It changes the shot:

| | Early | Late |
|---|---|---|
| Pace | borrows up to 15% of the incoming ball's speed | keeps only half of the attacking pace |
| Risk | up to 30% less control (half for the best timing) | none |
| Timing window (human) | down to 60% | up to 125% |

A human player chooses by where they stand: once the shot button is pressed, the player meets
the ball at the point of the window closest to them. The AI chooses by its play style (see
[The AI opponent](../ai/)).

## Serves

A serve's speed depends on serve power (47–58 m/s, 169–209 km/h, for a flat first serve). A
slice serve has 87.5% and a kick serve 76% of that speed, traded for spin. Second serves are
slower. For a human player, the serve's timing works like a shot's, with a perfect window of
0.08 s: an untimed serve keeps 72% of its speed, a perfect one all of it.

{{< callout type="info" >}}
**In the code:** `scenes/player/player.gd` (contact: position, readiness, deep and fast balls, earliness),
`scenes/player/controllers/human_controller.gd` (timing, aiming, charging),
`scenes/player/contact_window.gd` (the contact window),
`scenes/player/controllers/controller.gd` (choosing the contact point),
`scenes/player/ai/shot_executor.gd` (the AI's shots).
{{< /callout >}}
