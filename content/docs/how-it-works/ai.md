---
title: The AI opponent
weight: 6
---

**Short version:** when your ball comes, the AI predicts its flight and decides where to meet
it. It decides how bold to be (safe, neutral or attacking) and in which direction to play,
looking at where you stand. It looks at you once more just before it swings. After hitting, it
recovers to the spot that best covers your possible replies, or, after a good attack from a
short ball, follows it to the net. It plays by the same rules as you: the same physics, the same
movement, the same shot model.

{{< fig src="images/diagrams/ai_flow.svg" caption="What the AI does from your shot to its own." width="420px" >}}

## Where to meet the ball

For a groundstroke, the AI picks a point in the [contact window](../hitting/#early-or-late-the-contact-window):

- By **play style**: an aggressive player takes the ball earlier (earliness 0.3 for the least,
  0.75 for the most aggressive), with some random variation from ball to ball.
- A **short ball** is taken early, inside the court, so the AI can attack it.

## How bold: safe, neutral or attack

| The AI plays **safe** when… | It **attacks** more often when… |
|---|---|
| it barely gets to the ball (needs more than 85% of the available time) | the ball is a **chance**: short (bounces nearer than 9 m from the net) and weak (slower than 27 m/s) |
| your ball is very fast (over 126 km/h) | you are **out of position** |
| it is exhausted (below 32% stamina) | its play style is aggressive (20% to 60% base chance) |
| your ball is deep (likely, the deeper the more) | |

On a full chance (a short, weak ball), it attacks about 90% of the time.

## Where to: watching you

The AI works out where you *should* stand to cover its shot: a little toward the side it hits
from, the middle of the angles it can play. The farther you are from that spot, the more **out
of position** you are, and the more it plays into the **open court**, away from you.

With a short ball and you in position, it often plays a **short angle**: cross court, wide and
short with extra topspin, to pull you out of the court. Then the next ball goes into the open
court on the other side.

{{< fig src="images/plots/open_court.svg" caption="The one-two: a short angle pulls you wide, the next ball goes into the open court." width="560px" >}}

Otherwise it picks between **cross court**, **center** and **down the line**: cross court
(over the low middle of the net, into the longest diagonal) is the safe default, down the line
the aggressive one. Its play style shifts these odds, and some players have a favorite pattern
(always cross, or inside-out forehands).

**Committing late:** the AI decides on a target when your ball comes, but **0.35 s before
contact it looks at you again** and re-aims. Running to one side too early can be punished.

## Volleys and the net

The AI volleys when it plays at the net, or when your ball comes into the **net zone** (within
6 m of the net) out of the air and it can step in and be set in time. It does not volley balls
higher than 2.3 m; those it lets bounce.

It **follows its own shot to the net** only when all of these hold:

- it attacked from **at least 1.5 m inside the baseline** (after a short ball),
- the ball was met cleanly and lands deep or wide, and is fast or leaves you stretched,
- it can reach the **service line before you hit your reply**, so it can volley from there
  instead of being passed in the middle of the court,
- and it decides to (15% to 55% of the time, by its *net play* skill).

If it then has to play a groundstroke anyway (say, you lob it), it gives up the net.

## Recovering

After hitting, the AI recovers onto the **bisector** of the angle you can play into: from your
hitting position, halfway between the two corners of its service line. How deep depends on its
play style (from 1.5 m inside to 2.3 m behind its usual spot behind the baseline). After a weak
shot of its own it stays 1.2 m deeper; after a good attack it steps 0.9 m in.

{{< fig src="images/plots/recovery.svg" caption="The recovery spot lies on the bisector of the angle you can play into." width="420px" >}}

## What makes AI players different

Each player has a **play style**:

| Style value | Effect |
|---|---|
| *Aggression* | How often it attacks, how early it takes the ball, how often down the line |
| *Shot power* | Pace of its rally shots |
| *Topspin* | How much topspin it uses (more margin over the net) |
| *Court position* | How deep it stays: inside, on, or well behind the baseline |
| *Consistency* | How tightly its shots group around the target |
| *Preferred pattern* | A favorite tactic, which makes players recognizable |

…and the same **stats** as any player (see [Stamina and player stats](../stamina-and-stats/)).
Its shots miss their target by a random amount from about 0.15 m (the most precise) to 1.8 m (the
least); its serves aim at the T, the body or wide.

{{< callout type="info" >}}
**In the code:** `scenes/player/controllers/ai_controller.gd` (phases, where to meet the ball,
commit, net approach, recovery), `scenes/player/ai/ai_point_context.gd` (chance, out of
position), `scenes/player/ai/shot_planner.gd` (intent and direction),
`scenes/player/ai/shot_executor.gd` (building the stroke),
`scenes/player/resources/ai_play_style.gd` (play styles).
{{< /callout >}}
