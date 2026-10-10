---
title: How it works
weight: 2
---

This section explains the ideas behind Pelota: what the game computes, and why. Each page starts
with the short version in plain words, then goes into the details with diagrams and plots. At
the end of each page, a small **In the code** box points developers to the files that implement
it.

## The big picture

A match is a handful of parts that talk to each other:

{{< fig src="images/diagrams/overview.svg" caption="The parts of a match and what they tell each other." >}}

- The **match manager** knows the rules. It watches the ball, decides who wins each point, keeps
  the score and tells the players when to serve.
- Each **player** has a **controller** that decides what the player does: where to move and which
  shot to play. A human controller turns your button presses into these decisions; the AI
  controller makes its own. Both drive the player in exactly the same way, so the AI has no
  special powers.
- The **ball** flies by itself, following [its own physics](ball-physics/). The same physics can
  also *predict* the ball's flight, which both controllers use to plan where to meet it.
- The **model** is what you see of a player: the body, the clothes, the racket, and the
  [animation](animation/) that makes it all move.

## Topics

{{< cards >}}
  {{< card link="court" title="The court" icon="map" subtitle="Dimensions and directions everything else refers to." >}}
  {{< card link="ball-physics" title="Ball physics" icon="globe-alt" subtitle="Gravity, spin, air, bounce and net; and how a shot finds its target." >}}
  {{< card link="hitting" title="Hitting the ball" icon="sparkles" subtitle="What makes a shot fast and precise: timing, position, readiness, early or late." >}}
  {{< card link="movement" title="Movement" icon="arrows-expand" subtitle="Speed by direction, backpedaling and turning, getting to the ball." >}}
  {{< card link="animation" title="Animation" icon="film" subtitle="Retargeted motion, synced gait cycles, swings that meet the ball." >}}
  {{< card link="ai" title="The AI opponent" icon="chip" subtitle="How the computer reads your shot, chooses its own and positions itself." >}}
  {{< card link="mental-game" title="Pressure and confidence" icon="heart" subtitle="Nerves on big points, momentum from winning games." >}}
  {{< card link="stamina-and-stats" title="Stamina and player stats" icon="lightning-bolt" subtitle="What makes players different, and how they tire." >}}
  {{< card link="match-flow" title="Match flow" icon="clock" subtitle="Points, faults, breaks between points, and the match clock." >}}
  {{< card link="stadium" title="Stadium and broadcast" icon="video-camera" subtitle="TV cameras, benches and players who sweat." >}}
{{< /cards >}}
