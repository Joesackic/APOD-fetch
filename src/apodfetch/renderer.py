import subprocess
from pathlib import Path


def render_image(path: Path):
    subprocess.run(
        ["kitten", "icat", str(path)],
        check=True
    )
