import requests

from pathlib import Path
from datetime import date

API_URL = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"


import requests
from pathlib import Path
from datetime import date

API_URL = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"


def fetch_apod():
    date_code = date.today().strftime("%y%m%d")

    response = requests.get(
        f"{API_URL}/{date_code}",
        timeout=15
    )

    response.raise_for_status()

    return response.json()


def download_image(url: str, path: Path) -> Path:
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    path.write_bytes(response.content)

    return path

