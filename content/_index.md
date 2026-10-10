---
title: Pelota
layout: hextra-home
---

<div class="hx:mt-6 hx:mb-6">
{{< hextra/hero-headline >}}
  Tennis, simulated —&nbsp;<br class="sm:hx:block hx:hidden" />and explained
{{< /hextra/hero-headline >}}
</div>

<div class="hx:mb-8">
{{< hextra/hero-subtitle >}}
  Pelota is a free and open source 3D tennis game made with Godot.&nbsp;<br class="sm:hx:block hx:hidden" />
  Here you learn how to play it, how it works inside, and how you can help build it.
{{< /hextra/hero-subtitle >}}
</div>

<div class="hx:mb-12">
{{< hextra/hero-button text="Start playing" link="docs/play" >}}
{{< hextra/hero-button text="How it works" link="docs/how-it-works" style="background: transparent; border: 1px solid currentColor; color: inherit;" >}}
</div>

<div class="hx:mb-12">
{{< fig src="images/screenshots/match-tv-camera.jpg" caption="A match in Pelota, seen through the TV camera." >}}
</div>

{{< hextra/feature-grid >}}
  {{< hextra/feature-card
    title="A ball that behaves like a ball"
    subtitle="Topspin dips and kicks up, slice floats and skids, a ball clips the net cord and dribbles over. The same simulation predicts where every ball will go."
    link="docs/how-it-works/ball-physics"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(31,158,137,0.18),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Timing and footwork decide"
    subtitle="Release the button at the right moment, stand in the right place, and choose to take the ball early or late. A perfect hit is clearly better than a good one."
    link="docs/how-it-works/hitting"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(242,165,65,0.18),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="An opponent that watches you"
    subtitle="The AI punishes short balls, pulls you wide and then plays into the open court, and only comes to the net when it can get there."
    link="docs/how-it-works/ai"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(59,130,246,0.16),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Nerves and momentum"
    subtitle="Defending break points builds pressure, winning games builds confidence, and both change how well a player hits."
    link="docs/how-it-works/mental-game"
  >}}
  {{< hextra/feature-card
    title="Motion from real movement"
    subtitle="Motion-captured running and stroke animations, retargeted onto the players and blended so the feet never slide."
    link="docs/how-it-works/animation"
  >}}
  {{< hextra/feature-card
    title="Built in the open"
    subtitle="Programmers, 3D artists, animators, translators, writers and testers are all welcome. Start here to find your way in."
    link="docs/contribute"
  >}}
{{< /hextra/feature-grid >}}

<div class="content hx:w-full hx:mt-12">

## News

{{< latest-posts 3 >}}

</div>
