---
title: Translation
weight: 4
---

Pelota should be playable in your language. Translation work comes in two parts: making the
game's texts translatable, and translating them.

{{< callout type="warning" >}}
**Current state:** only the menus that come from the game template are translated (English and
French). The game's own texts, such as menu labels, shot ratings ("PERFECT!", "OUT OF POSITION"),
the HUD, the umpire's calls and the statistics, are not translatable yet. This is a great first
task, for a programmer and a translator together.
{{< /callout >}}

## How translation works in Godot

Godot translates texts by **keys**. A text shown in the game is written as a key, for example
`RATING_PERFECT`, and Godot looks the key up in a translation table for the player's language:

| keys | en | de | fr |
|---|---|---|---|
| RATING_PERFECT | PERFECT! | PERFEKT! | PARFAIT ! |
| RATING_OUT_OF_POSITION | OUT OF POSITION | FALSCH POSITIONIERT | MAL PLACÉ |

Labels in scenes are translated automatically when their text is a key. In code, texts go
through `tr("RATING_PERFECT")`.

## Translating

{{% steps %}}

### Find the table

The game's translation table will live in the project (a `.csv` file like the one above, or
`.po` files if more languages join). Check the
[issues](https://github.com/mbkma/pelota/issues) for the current state and say which language
you want to take on.

### Add your language

Add a column with your language's code (`de`, `es`, `pt_BR`, …) and translate each row. Keep
the texts short; buttons and the shot ratings have little room.

### Know the tennis words

Use the words your language's TV commentators use: *break point*, *ace*, *let*, *double
fault*, *deuce*, *advantage*. Many languages use the English word for some of them. When unsure,
say so in your pull request.

### Check it in the game

Godot imports the table and the language shows up in the options menu. Look at every screen for
texts that do not fit or read oddly.

{{% /steps %}}

## Making texts translatable (programmers)

- Use keys instead of literal texts for everything the player reads, and wrap texts built in code
  in `tr()`.
- Do not glue sentences together from pieces; word order differs between languages. Use one key
  with placeholders: `tr("SERVE_SPEED").format({"speed": 182})`.
- Do not edit the template's translations in `addons/`; the game gets its own table.
