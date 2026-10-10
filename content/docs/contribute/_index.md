---
title: Contribute
weight: 3
---

Pelota is free and open source, and it grows with the people who help. You do not need to be a
programmer: a tennis game needs players and stadiums modeled, motion animated, menus translated,
these docs written, and above all people who play it and say what feels wrong.

{{< cards >}}
  {{< card link="code" title="Programming" icon="code" subtitle="Gameplay, AI, physics, tools. GDScript in Godot." >}}
  {{< card link="art" title="Art and models" icon="color-swatch" subtitle="Players, clothes, rackets, the stadium, textures." >}}
  {{< card link="animation" title="Animation" icon="film" subtitle="Strokes and footwork: from Blender or motion capture into the game." >}}
  {{< card link="translation" title="Translation" icon="translate" subtitle="Bring Pelota to your language." >}}
  {{< card link="docs" title="Documentation" icon="document-text" subtitle="Improve these pages, add diagrams and plots." >}}
  {{< card link="testing" title="Playing and testing" icon="chat-alt-2" subtitle="Report bugs, give feedback on how it feels." >}}
{{< /cards >}}

## Where things live

| Repository | What is in it |
|---|---|
| [pelota](https://github.com/mbkma/pelota) | The game: the Godot project |
| [pelota-files](https://github.com/mbkma/pelota-files) | Source files of the art: Blender files of players, rackets, the court, the stadium, … |
| [pelota-docs](https://github.com/mbkma/pelota-docs) | This documentation |

## How a contribution works

{{% steps %}}

### Say hello

Open an [issue](https://github.com/mbkma/pelota/issues) describing what you would like to do,
or comment on an existing one. For small fixes you can skip this and go straight to a pull
request. For anything bigger it saves you work, because someone may already be on it, or there
may be a plan you should know about.

### Make the change

Fork the repository on GitHub, make your change on a branch, and try it in the game. The guides
for your kind of contribution (see the cards above) explain the tools and conventions.

### Open a pull request

Describe what you changed and why; screenshots or short clips help a lot for anything visual.
Someone will review it, maybe ask for changes, and merge it.

{{% /steps %}}

## Licenses

The game's code is released under the [GNU GPL v3](https://github.com/mbkma/pelota/blob/main/LICENSE).
Art you contribute must be your own work or under a license that allows it to be shared and
changed. Add its author, source and license to `ATTRIBUTION.md` when it is not your own.
