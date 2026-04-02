# DMX

My Ph.D.

Available here : [DMX](https://Yanis-Kouidri.github.io/DMX/)

## Dev

### Set up

Create python virtual environment

```bash
python3 -m venv .venv
```

Load virtual environment

```bash
source .venv/bin/activate
```

Install mkdocs

```bash
pip install -r requirements.txt
```

### Run

```bash
mkdocs serve --open --livereload
```

## Deploy on GitHub pages

To publish it manually

```bash
mkdocs gh-deploy
```

Then it should be available on [DMX GitHub Pages](https://Yanis-Kouidri.github.io/DMX/)
