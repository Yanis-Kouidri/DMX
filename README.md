# DMX

DMX stand for Data Mule eXpress, it's the name of my Ph.D.

The subject is: *Ephemeral communication backbone for data harvesting in wireless sensor networks*

Available here : [DMX](https://Yanis-Kouidri.github.io/DMX/)

## Dev

### Set up

Install [uv](https://docs.astral.sh/uv/), then

```bash
uv sync
```

This command will automatically install python, create the virtual environment and install the dependencies.

### Run

```bash
uv run mkdocs serve --open --livereload
```

## Deploy on GitHub pages

Even if it's deployed automatically thanks to GitHub action, you can publish it manually :

```bash
uv run mkdocs gh-deploy
```

Then it should be available on [DMX GitHub Pages](https://Yanis-Kouidri.github.io/DMX/)
