---
title: Pressure and confidence
weight: 7
---

**Short version:** before every point, each player looks at the score.

- **Pressure** comes mostly from having to **defend a break point** (or a set or match point),
  and from being **behind on the score**. Being *hopelessly* behind releases it again: there is
  nothing left to lose.
- **Confidence** comes mostly from **winning games** lately and from **leading** on the score, and
  a little from **hitting the ball well**.

Pressure makes a player less precise. Confidence helps them recover their breath between points.

## Pressure, step by step

Before each point, the game works out how much pressure the **situation** brings, and the
player's pressure moves 60% of the way toward it. So pressure builds up quickly on big points,
but does not jump all the way at once, and it fades over a few points afterward.

The situation's pressure is the biggest of the point's stakes, plus the pressure of trailing:

{{< fig src="images/plots/pressure_sources.svg" caption="Left: pressure from trailing, by how far behind a player is. It peaks at about two breaks down and fades when the deficit is hopeless. Right: pressure of big points." >}}

**Big points.** Defending a point that would decide something for the opponent weighs the most:
a break point (0.5), a set point (0.65), a match point (0.8). Serving it out yourself on a set or
match point adds a little (0.2 / 0.3), and so does every tiebreak point (0.2).

**Trailing.** How far behind a player is (the **standing**) counts sets and the games of the
current set: a set behind is −0.4, each game behind −0.12. The pressure of trailing rises with
the deficit, is largest at about −0.5 (for example 0–4 in the set), and falls back toward zero
when the situation is hopeless (a set and 0–5 down).

## Confidence, step by step

Confidence moves 30% of the way toward the situation before each point, so it changes more
slowly than pressure. Around a neutral 0.5, it rises or falls with:

- the **standing** (up to ±0.25),
- **momentum** from recent games (up to ±0.2); each game won or lost moves momentum a third of
  the way toward +1 or −1, so the latest games count the most,
- **form** from recent strokes (up to ±0.08): how well the ball was hit. For you, that is your
  shot rating; for the AI, how cleanly it met the ball.

## An example

{{< fig src="images/plots/match_story.svg" caption="Player A holds serve, then defends two break points and is broken. Pressure jumps on the break points and stays raised while A is behind; confidence slowly sinks with the lost games." >}}

## How it affects play

A player's traits **composure** and **clutch** absorb part of the pressure. The rest lowers:

- **shot control** (and with it the landing precision of every shot) by up to 25%,
- **serve accuracy** by up to 20%,
- how well the player **preserves stamina** by up to 10%.

Confidence speeds up stamina **recovery** between points (from 92% to 108%).

You can follow both values live on the small status panel of each player.

{{< callout type="info" >}}
**In the code:** `scenes/player/player_mental_state.gd` (pressure, confidence, momentum, form),
`scenes/match/match_score.gd` (`standing`, `point_importance`),
`scenes/player/player_runtime_stats.gd` (the effects).
{{< /callout >}}
