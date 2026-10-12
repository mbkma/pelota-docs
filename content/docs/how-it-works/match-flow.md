---
title: Match flow
weight: 9
---

**Short version:** the match manager runs the rules. It asks the server to serve, watches every
bounce of the ball to decide whether it is in, out or a second bounce, awards the point, updates
the score and gets everybody ready for the next point.

## A point from start to end

{{< fig src="images/diagrams/point_flow.svg" caption="A point from the serve to the end." >}}

**Who wins the point:** the last player to hit the ball wins it if their ball bounced in and
the opponent did not get it back before the second bounce. They lose it if the ball went out
or into the net.

**In or out:** each half of the court is a region. A bounce counts only in the half the ball
must land in, and that half switches with every valid bounce. A serve must land in the service
box diagonally opposite the server.

## Timing between points

| Moment | Wait |
|---|---|
| After a first serve fault or a let | The ball flies on for **2 s**, then the server serves again |
| After a point | **3 s** before the players are placed for the next point |
| AI server | waits **2 s** before tossing the ball |
| Serve clock | **25 s** shown on the stadium clocks |

## The score

Standard tennis: 15, 30, 40, game, with deuce and advantage; six games and a two-game lead win a
set, with a tiebreak to 7 at 6–6; best of three sets. Players change ends after every odd game
(and every 6 points in a tiebreak).

The score also tells each player **what the next point means**: a game point, a break point, a
set point or a match point, for either side. This feeds the players'
[pressure](../mental-game/).

## The match clock

The stadium shows a match time that runs like a real match: every point adds 25 seconds (walking
back, toweling, preparing the serve) plus 1.5 seconds per shot of the rally, counted at the end
of each game (at most 10 minutes per game).

## Statistics

During the match the game records for each player: first serves in, aces, double faults, first-
and second-serve points won, winners, errors, break points (played, won, saved), net points,
serve speeds and the longest rally.

{{< callout type="info" >}}
**In the code:** `scenes/match/match_manager.gd` (the rules and the flow),
`scenes/match/match_score.gd` (scoring), `scenes/match/match_data.gd` (match clock),
`scenes/match/match_statistics.gd` (statistics).
{{< /callout >}}
