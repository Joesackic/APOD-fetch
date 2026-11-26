from pathlib import Path
from tempfile import TemporaryDirectory

import requests

from apodfetch.api import fetch_apod, download_image
from apodfetch.renderer import render_apod


def main() -> int:
    try:
        data = fetch_apod()
    except (requests.RequestException, ValueError) as error:
        print(f"Could not fetch today's APOD: {error}")
        return 1

    if not isinstance(data, dict):
        print("Could not read today's APOD response.")
        return 1

    if not data.get("media_type"):
        print("Today's APOD response is missing its media type.")
        return 1

    if data.get("media_type") != "image":
        print("Today's APOD is not an image.")
        if data.get("url"):
            print(data["url"])
        return 0

    image_url = data.get("hdurl")
    if not image_url:
        print("Today's APOD image is unavailable.")
        if data.get("url"):
            print(f"View it online: {data['url']}")
        return 1

    with TemporaryDirectory() as directory:
        path = Path(directory) / "apod.jpg"

        try:
            download_image(image_url, path)
        except (requests.RequestException, OSError) as error:
            print(f"Could not download today's APOD image: {error}")
            if data.get("url"):
                print(f"View it online: {data['url']}")
            return 1

        render_apod(path, data)

    return 0
