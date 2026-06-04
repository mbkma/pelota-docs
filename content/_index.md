---
title: Pelota Game Documentation
layout: hextra-home
---

<div class="hx:mt-3 hx:mb-6">
{{< hextra/hero-headline >}}
  Pelota <br class="sm:hx:block hx:hidden" /> Docs
{{< /hextra/hero-headline >}}
</div>

<div class="hx:mb-6">
{{< hextra/hero-subtitle >}}
  Pelota is a 3D tennis simulation built with Godot, focused on realistic ball physics, tactical AI, and clear gameplay systems. This documentation explains the high-level concepts and the math behind the game.
{{< /hextra/hero-subtitle >}}
</div>

<div class="content hx:w-full">

![Gameplay](/images/pelota_gameplay01.png)

{{< cards >}}
  {{< card link="docs/" title="Docs" icon="book-open" >}}
{{< /cards >}}

## News

{{< latest-posts 5 >}}

{{< cards >}}
  {{< card link="/blog" title="All posts" icon="newspaper" >}}
{{< /cards >}}

## Features

<br>

{{< hextra/feature-grid >}}
  {{< hextra/feature-card
    title="Physics-Based Ball Model"
    subtitle="Gravity, Magnus effect, drag, and bounce damping are simulated step-by-step for both runtime gameplay and trajectory prediction."
    class="hx:aspect-auto md:hx:aspect-[1.1/1]"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(56,132,255,0.16),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Real Tennis Match Flow"
    subtitle="Points, games, sets, serves, faults, and rally states follow a clear state machine that mirrors real tennis structure."
    class="hx:aspect-auto md:hx:aspect-[1.1/1]"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(72,199,142,0.16),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="3D Coordinate-Centered Design"
    subtitle="All systems use explicit X/Y/Z court coordinates, from player movement and targeting to AI decision metrics and shot execution."
    class="hx:aspect-auto md:hx:aspect-[1.1/1]"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(255,176,56,0.18),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Adaptive AI Strategy"
    subtitle="AI builds contextual shot decisions from ball trajectory, stamina, risk, and intent profiles such as neutral, attack, and defend."
  >}}
  {{< hextra/feature-card
    title="Mathematical Documentation"
    subtitle="LaTeX formulas explain velocity integration, drag, spin forces, and bounce decomposition in implementation-level detail."
  >}}
  {{< hextra/feature-card
    title="Godot 4 Architecture"
    subtitle="Scene-driven systems connect Ball, Player, Controller, and MatchManager components with reusable data contexts and signals."
  >}}
{{< /hextra/feature-grid >}}

</div>