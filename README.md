# Pelota documentation

The documentation site of [Pelota](https://github.com/mbkma/pelota), a free and open source 3D
tennis game. It is built with [Hugo](https://gohugo.io/) and the
[Hextra](https://imfing.github.io/hextra/) theme.

## Run it locally

Install Hugo **extended** (0.147 or newer) and Go, then:

```bash
hugo server
```

## Structure

- `content/docs/play/`: how to play
- `content/docs/how-it-works/`: the concepts behind the game, in plain words
- `content/docs/contribute/`: guides for contributors
- `tools/plots/make_plots.py`: draws the plots (`python3 tools/plots/make_plots.py`, needs matplotlib)
- `tools/diagrams/*.dot`: the diagrams (`sh tools/diagrams/render.sh`, needs Graphviz)
- `static/images/`: plots, diagrams and screenshots

See [Contribute → Documentation](content/docs/contribute/docs.md) for how we write.
