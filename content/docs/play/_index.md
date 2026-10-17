---
title: Play
weight: 1
next: /docs/play/controls
---

Pelota is a singles tennis game: you against the computer, or against a friend on the same
computer. This section gets you started.

## Get the game

{{< tabs >}}
{{< tab name="Download a build" >}}
Download the file for your system from the
[latest release](https://github.com/mbkma/pelota/releases/latest) (the `.zip` for Windows, the
`.tar.gz` for Linux; older versions are on the
[releases page](https://github.com/mbkma/pelota/releases)), unpack it and start `Pelota.exe`
(Windows) or `Pelota.x86_64` (Linux).
{{< /tab >}}
{{< tab name="Run from the source" >}}
Pelota is made with the [Godot engine](https://godotengine.org/), version **4.8**.

1. Install Godot 4.8 (the standard build, not the .NET one).
2. Get the project: `git clone https://github.com/mbkma/pelota.git`
3. Start Godot, choose **Import**, and open the `project.godot` file in the `pelota` folder.
4. Press **F5** (or the ▶ button) to play.

The first start takes a while because Godot imports all models and textures.
{{< /tab >}}
{{< /tabs >}}

## Game modes

**Match**
: Pick your player and your opponent, then play a full match on the stadium court. Each side
  can be played by the computer, the keyboard or a gamepad. So you can watch two computer
  players, play against the computer, or play against a friend. The match is saved after
  every point: quit any time and pick it up again with **Continue Match** in the main menu,
  from the point you were playing. Starting a new match replaces the saved one.

**US Open**
: Play the men's singles of the US Open as one of the 128 best ranked ATP players: seven
  rounds from the first round to the final, against the players the draw brings. The other
  matches are simulated, so the favorites usually go far, but upsets happen. See
  [US Open](tournament/).

**Training**
: You alone on court with a ball machine on the far baseline. Move around freely and ask for a
  ball whenever you are ready (<kbd>E</kbd> or the right trigger). After each of your shots the
  screen shows whether it landed **IN** or **OUT** (or went into the **NET**) and how fast it was.
  This is the best place to learn the timing.

{{< fig src="images/screenshots/training-in-position.jpg" caption="Training: the ball machine is on the far baseline. The green ring and line at your feet show where you can meet the incoming ball; the big ring on the far side shows where your shot will land." >}}

## The rules in short

Pelota plays real tennis rules: points go 15, 30, 40 and game; at 40–40 (deuce) you need two
points in a row. Six games win a set, but you need two games more than your opponent; at 6–6 a
tiebreak to 7 points decides. A match is best of three sets (in the US Open you can choose
best of five, as the men play it).

A serve must land in the service box diagonally across; if it misses you get a second serve,
and if that misses too it is a double fault and the point goes to your opponent.

{{< cards >}}
  {{< card link="controls" title="Controls" icon="cursor-click" >}}
  {{< card link="hitting-well" title="Hitting well" icon="sparkles" >}}
  {{< card link="tournament" title="US Open" icon="trophy" >}}
{{< /cards >}}
