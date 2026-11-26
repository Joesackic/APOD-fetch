# APOD Fetch

APOD Fetch displays NASA's [Astronomy Picture of the Day](https://apod.nasa.gov/apod/) in your terminal. It shows the image beside its title, date, credit, and explanation when terminal image display is available. Otherwise, it prints the details as text.

The program fetches the APOD for your computer's current local date. It currently has no command-line options for choosing another date.

## Requirements

- Python 3.14 or newer
- An internet connection
- Optional: [Kitty](https://sw.kovidgoyal.net/kitty/) and its `kitten icat` command for image previews

The Python dependencies are installed through the project metadata. Kitty is optional; the program still displays text when image preview is unavailable.

## Install and run

With [uv](https://docs.astral.sh/uv/) installed:

```sh
git clone https://github.com/Joesackic/APOD-fetch.git
cd APOD-fetch
uv sync
uv run apodfetch
```

Run `uv run apodfetch` again whenever you want to see today's APOD. Images are downloaded to a temporary directory and removed when the command finishes.

## Arch Linux package

The repository includes a development package recipe in [`packaging/aur/`](packaging/aur/). To build and install it locally on Arch Linux:

```sh
cd packaging/aur
makepkg -si
apodfetch
```

The package is named `apodfetch-git`. Its `PKGBUILD` clones the published GitHub repository, so commit and push changes before building if you want them included. The recipe files can be copied to a separate AUR repository for publication; their [packaging README](packaging/aur/README.md) has maintenance notes.

## What to expect

- On an image day, APOD Fetch downloads the image and tries to display it with `kitten icat` in a terminal. If that fails, it prints the title, date, credit, explanation, and page link instead.
- On a video or other non-image day, it prints a link to the APOD page.
- If the request or image download fails, it prints an error message. When NASA provides a page link, the download error also includes that link.

The data comes from NASA's [APOD Basic endpoint](https://science.nasa.gov/wp-json/wp/v2/apod-basic). A new day's post may not be available yet when your local calendar date changes; if the request fails then, try again later.

## Development

Application code lives in `src/apodfetch/`. The command-line entry point is `apodfetch.cli:main`, and `pyproject.toml` defines the Python dependencies and build backend. To build a wheel locally, run:

```sh
uv build --wheel
```

## License

APOD Fetch is licensed under the [MIT License](LICENSE). The AUR packaging files have their own [0BSD license](packaging/aur/LICENSE).
