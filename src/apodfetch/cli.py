from pathlib import Path
from tempfile import TemporaryDirectory

from apodfetch.api import fetch_apod, download_image
from apodfetch.renderer import render_apod


def main():
    data = fetch_apod()

    if data["media_type"] != "image":
        print("Today's APOD is not an image.")
        print(data["url"])
        return

    with TemporaryDirectory() as directory:
        path = Path(directory) / "apod.jpg"

        download_image(data["hdurl"], path)
        render_apod(path, data)
