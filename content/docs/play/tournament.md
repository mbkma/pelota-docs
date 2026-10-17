---
title: US Open
weight: 3
---

In the **US Open** you play the men's singles of a Grand Slam: 128 players, seven rounds, one
champion. Choose **US Open** in the main menu, pick your player and your controller (move it to
the left and confirm), and start.

## The field and the draw

The field is the 128 best players of the ATP ranking (as of October 1, 2026). The 32 best
ranked are **seeded** and kept apart in the draw, like at a real Grand Slam: the first two seeds
can only meet in the final, the first four not before the semifinals, the first eight not
before the quarterfinals, and so on. Everybody else is drawn at random. If you pick a player
outside the field (Rafael Nadal, who retired), you take the place of number 128.

## Your matches and the others

The draw screen shows every round: who plays whom, the seeds in brackets, and the scores of the
matches already played. Your name is in your color, winners are highlighted.

- **Play the round** starts your next match. When it is over, **Back to the Draw** returns to
  the draw, and the other matches of the round are decided.
- **Simulate My Match** decides your next match without playing it, the same way as the other
  matches, over the sets you chose.
- Choose how long your matches are: **best of 3** or **best of 5** sets. The other matches are
  always best of five, as the men play it at Grand Slams.
- Once you are out, **Simulate to the Final** plays the rest of the tournament and shows the
  champion.

The tournament is saved after every round, and your match in it after every point, so you can
stop any time and pick it up again with **Continue US Open** in the main menu: a match you
started continues from the point you were playing. Starting a new US Open replaces the saved
one.

## How the other matches are decided

The other matches are played point by point by the real scoring rules, without being shown. The
server wins a point about as often as on the ATP tour (64% of service points between two equal
players), more if their serve is better than the opponent's return, and more if they play
better from the baseline. Each player also has a good or a bad day. So the favorites usually
win, but not always: about four seeds lose in the first round, and the top seed wins the title
about a third of the time.

{{< callout type="info" >}}
**In the code:** `scenes/tournament/` (`tournament.gd`: the draw and the rounds,
`match_simulator.gd`: the simulated matches, `tournament_screen.gd`: the draw screen) and
`scenes/player/resources/roster/` (the ranking and the builder that makes the players from it).
{{< /callout >}}
