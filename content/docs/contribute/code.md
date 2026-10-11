---
title: Programming
weight: 1
---

Pelota is written in **GDScript** in the **Godot 4.8** engine. No other language or build step is
needed.

## Set up

{{% steps %}}

### Godot

Install Godot **4.8** (the standard build, not .NET). The project uses features of 4.8, so older
versions will not open it correctly.

### The project

```bash
git clone https://github.com/<your-name>/pelota.git   # your fork
```

Open `pelota/project.godot` in Godot and press **F5** to play. The first start imports all assets
and takes a while.

### The linter

The code is checked with [gdtoolkit](https://github.com/Scony/godot-gdscript-toolkit) (the
version is in `requirements.txt`):

```bash
pip install -r requirements.txt
gdformat scenes scripts      # formats the code
gdlint scenes scripts        # checks naming, order, line length (100)
```

Run both before you open a pull request. The rules are in `gdlintrc`.

{{% /steps %}}

## Find your way around

{{< filetree/container >}}
  {{< filetree/folder name="pelota" >}}
    {{< filetree/folder name="scenes" >}}
      {{< filetree/folder name="ball" >}}{{< filetree/file name="ball.gd — flight, bounce, net, prediction, aiming" >}}{{< /filetree/folder >}}
      {{< filetree/folder name="player" >}}
        {{< filetree/file name="player.gd — movement, strokes, contact, stamina" >}}
        {{< filetree/file name="model.gd — looks, sweat, stroke contact points" >}}
        {{< filetree/file name="player_animator.gd — animation blending, strokes" >}}
        {{< filetree/folder name="controllers — human and AI" state="closed" >}}{{< /filetree/folder >}}
        {{< filetree/folder name="ai — shot planning" state="closed" >}}{{< /filetree/folder >}}
        {{< filetree/folder name="resources — roster, appearances, play styles" state="closed" >}}{{< /filetree/folder >}}
      {{< /filetree/folder >}}
      {{< filetree/folder name="match — rules, score, statistics" state="closed" >}}{{< /filetree/folder >}}
      {{< filetree/folder name="training — training mode" state="closed" >}}{{< /filetree/folder >}}
      {{< filetree/folder name="environments — stadium, cameras, crowd" state="closed" >}}{{< /filetree/folder >}}
      {{< filetree/folder name="menus, ui — menus and HUD" state="closed" >}}{{< /filetree/folder >}}
    {{< /filetree/folder >}}
    {{< filetree/folder name="scripts/core — constants, global game data" state="closed" >}}{{< /filetree/folder >}}
    {{< filetree/folder name="assets — models, textures, sounds" state="closed" >}}{{< /filetree/folder >}}
    {{< filetree/folder name="addons — third-party plugins (do not edit)" state="closed" >}}{{< /filetree/folder >}}
  {{< /filetree/folder >}}
{{< /filetree/container >}}

The [How it works](../../how-it-works/) pages explain each system and end with an **In the code**
box naming the files to read.

## How we write code

These rules keep the code base small and readable. Please follow them; reviews will point to them.

- **Fix the root problem, no fallbacks.** If something can be null or wrong, find out why and fix
  that, instead of adding a check that hides it.
- **No code kept for compatibility.** When you change how something works, update all its users
  and remove the old way, unless keeping it was explicitly asked for.
- **Clean up as you go.** During a bigger change, refactor so the result is clean code, not a
  patch on top.
- **Named classes over paths.** Use `class_name` and typed references instead of loading scripts
  or scenes by path (`preload("res://…")`) where a class will do.
- **Never edit `addons/`.** Those are third-party plugins; work around them in the game's own code.
- **Static types everywhere.** Type every variable, parameter and return value.
- **Comments explain *what* and *why*, in plain sentences.** Every class, constant and function
  gets a `##` doc comment that says what it means (with units: m, s, m/s), so the next reader can
  understand it without reading the code below.
- **Name values, do not hide them.** Tuning values are named constants with a comment saying what
  they mean and in which unit, usually with a real-world reference ("ATP average forehand
  ~115 km/h").

## Making gameplay changes

Tennis feel is easy to break. Some habits that help:

- **Measure, do not guess.** Many systems have real-world references (shot speeds, sprint times,
  serve percentages). Check your change against them, for example by watching an AI-against-AI
  match (pick two computer players in the match menu) and looking at the debug HUD.
- **Look at it.** For anything visual (animation, cameras, effects) record a short clip or take
  screenshots before and after, and add them to the pull request.
- **Update the docs.** If your change alters how something works, update the matching page here.
  It is part of the change.

## Updating the players

The players are made from the ATP ranking in
`scenes/player/resources/roster/atp_top_128.csv`: rank, name, country, age, height, hand,
backhand and playing style (`big_server`, `aggressive`, `baseliner`, `counterpuncher` or
`all_court`). When the ranking changes, update the file and run the builder:

```bash
godot --headless --path . -s res://scenes/player/resources/roster/roster_builder.gd
```

It writes one player resource per row into `scenes/player/resources/data/`. A player whose
resource is made by hand (stats, play style and look tuned by hand, like Sinner or Alcaraz)
keeps it: the builder only updates the facts and moves the stats to the level of the rank. Every
other player is generated from the rank and the playing style. A hand-made player who drops out
of the ranking stays playable without a rank.
