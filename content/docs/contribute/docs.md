---
title: Documentation
weight: 5
---

These pages are made with [Hugo](https://gohugo.io/) and the
[Hextra](https://imfing.github.io/hextra/) theme. Every page is a Markdown file in the
[pelota-docs](https://github.com/mbkma/pelota-docs) repository. For a small fix, use the **Edit
this page** link at the bottom of any page: it opens the file on GitHub, ready to edit.

## How we write

- **For everyone first.** Start each concept page with a *short version* in plain words, then
  go deeper. Someone who has never seen the code should understand the first paragraph.
- **Explain ideas, not code.** Say what the game does and why, with real numbers ("backpedaling
  is 70% of the forward speed"). Code names belong only in the **In the code** box at the end.
- **Show it.** A plot, a diagram or a screenshot often explains more than a paragraph.
- **Keep it true.** These pages describe the game as it is. When the game changes, the page
  changes with it, in the same pull request if you can.

## Working locally

{{% steps %}}

### Install Hugo

Install Hugo **extended** (0.147 or newer) and Go (Hugo uses Go modules to fetch the theme).

### Run the site

```bash
git clone https://github.com/<your-name>/pelota-docs.git
cd pelota-docs
hugo server
```

Open the address it prints (usually <http://localhost:1313/>). Pages reload as you save.

{{% /steps %}}

## Building blocks

**Diagrams** are drawn with [Graphviz](https://graphviz.org/). Each diagram is a small `.dot`
file in `tools/diagrams/`; render them all with

```bash
sh tools/diagrams/render.sh
```

which writes SVG files into `static/images/diagrams/`. Copy the style lines (colors, font) from an
existing diagram so they all look alike and read well in light and dark mode. Show a diagram on a
page with the `fig` shortcode below.

**Figures** with captions use the `fig` shortcode. Put the image under `static/images/`:

```markdown
{{</* fig src="images/plots/court.svg" caption="The court seen from above." */>}}
```

**Callouts**, **cards**, **steps**, **tabs** and **file trees** come from Hextra; see its
[shortcode guide](https://imfing.github.io/hextra/docs/guide/shortcodes/).

**Math** works with `\( … \)` inline and `$$ … $$` for blocks, when the page has `math: true`.

## Plots

All plots are drawn by one Python script that repeats the game's formulas:

```bash
pip install matplotlib
python3 tools/plots/make_plots.py
```

It writes SVG files into `static/images/plots/`. When a formula or a constant in the game
changes, change it in the script too and run it again. Each plot function names the game file it
mirrors. Keep the colors from the top of the script; they read well on the light and the dark
theme.

## Screenshots

Take screenshots in the game at 1280×720, from the TV camera where possible, without debug
overlays. Save them as JPEG (quality around 85) in `static/images/screenshots/` with a
descriptive name (`training-in-position.jpg`).
