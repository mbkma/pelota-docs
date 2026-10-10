---
title: Stamina and player stats
weight: 8
---

**Short version:** every player has about twenty **ratings** from 1 to 100, like in a sports
manager game. They decide how fast the player runs, how hard and precise they hit, and how well
they keep their nerve. Running and hitting use up **stamina**; a tired player runs slower and hits
less precisely, and recovers while standing between points.

## The ratings

| Group | Ratings | What they change |
|---|---|---|
| Physical | *acceleration*, *top speed*, *agility*, *stamina* | Running speed, how fast they get going, how much a sharp turn costs, the size of the stamina pool |
| Strokes | *forehand*, *backhand*, *serve power*, *serve accuracy*, *return*, *volley*, *slice*, *topspin* | Shot speed and attacking pace per stroke, serve speed and precision, spin |
| Precision | *accuracy*, *consistency*, *timing* | **Shot control**: how tightly shots land around the aim; *timing* also widens the perfect timing window |
| Mental | *composure*, *focus*, *clutch* | How much [pressure](../mental-game/) gets through; *focus* also slows tiring and speeds recovery |
| Tactical | *net play* | How willing the player is to come to the net and how good they are there |

Some values combine several ratings. **Shot control**, for example, is 35% accuracy + 35%
consistency + 20% timing + 10% composure, and every shot's landing precision builds on it.

## Stamina

**The pool:** a player's stamina rating sets the size of their energy pool (from 72 to 165 units).

**Using it up:**

- **Running** drains stamina in proportion to the speed: about 4 to 7.5 units per second at
  full speed. Good *focus* and *composure* put a player at the low end.
- **Every stroke** costs about 5 to 11 units, more for fast and heavily spun shots.

**Recovering:** standing still recovers 3.5 to 9 units per second (by the stamina rating, more
with good *focus*), a bit faster when the player is still quite fresh, and faster with confidence.

**When tired:**

| | Fresh | Exhausted |
|---|---|---|
| Top speed and acceleration | 100% | about 40% (rating effect × general tiredness) |
| Shot control | 100% | 72% |
| Spin control | 100% | 75% |
| Serve accuracy | 100% | 78% |
| Timing | 100% | 85% |

The AI also plays more safely when it is low on stamina (below 32%).

## Where players are defined

Each player in the roster is a small data file with their name, country, hand and rank, and
three parts:

- **stats**: the ratings above,
- **play style**: how the [AI](../ai/#what-makes-ai-players-different) plays them,
- **appearance**: their body, clothes, hair and racket (see
  [Art and models](../../contribute/art/)).

{{< callout type="info" >}}
**In the code:** `scenes/player/player_stats_profile.gd` (ratings and how they combine),
`scenes/player/player_runtime_stats.gd` (stats during the match, with pressure and confidence),
`scenes/player/player.gd` (stamina use and recovery), the roster in
`scenes/player/resources/data/`.
{{< /callout >}}
