import subprocess
import shutil
import textwrap

from pathlib import Path
from rich.text import Text
from rich.console import Console
from bs4 import BeautifulSoup

console = Console()

def clean_html(html: str) -> str:
    return BeautifulSoup(html, "html.parser").get_text()

def render_text_apod(data: dict) -> None:
    console.print("Image preview unavailable. Today's APOD:")
    console.print(f"Title: {data.get('title') or 'Unknown'}")
    console.print(f"Date: {data.get('date') or 'Unknown'}")
    console.print(f"Credit: {clean_html(data.get('credit') or 'Unknown')}")
    if data.get("explanation"):
        console.print(clean_html(data["explanation"]))
    if data.get("url"):
        console.print(f"View it online: {data['url']}")

def short_explanation(html: str, max_chars: int = 220) -> str:
    text = clean_html(html)
    text = " ".join(text.split())
    return textwrap.shorten(text, width=max_chars, placeholder="...")

def render_apod(path: Path, data: dict):
    if not console.is_terminal or shutil.which("kitten") is None:
        render_text_apod(data)
        return

    console.clear()

    terminal_width, terminal_height = shutil.get_terminal_size()

    image_width = min(40, terminal_width // 3)
    image_height = max(1, min(20, terminal_height - 4))

    text_offset = image_width + 3
    text_width = max(1, terminal_width - text_offset - 1)

    try:
        subprocess.run(
            [
                "kitten",
                "icat",
                "--align", "left",
                "--place", f"{image_width}x{image_height}@0x0",
                str(path)
            ],
            check=True,
            stderr=subprocess.DEVNULL,
        )
    except (OSError, subprocess.CalledProcessError):
        render_text_apod(data)
        return

    print(f"\033[1;{text_offset + 1}H", end="")
    console.print("APOD FETCH", style="bold cyan")

    # summary = short_explanation(data["explanation"])

    summary = clean_html(data.get("explanation") or "")
    
    lines = [
        f"Title: {data.get('title') or 'Unknown'}",
        f"Date: {data.get('date') or 'Unknown'}",
        f"Credit: {clean_html(data.get('credit') or 'Unknown')}",
        "",
        "",
        summary,
    ]

    row = 3

    for line in lines:
        wrapped_lines = textwrap.wrap(line, width=text_width) or [""]

        for wrapped_line in wrapped_lines:
            print(f"\033[{row};{text_offset + 1}H", end="")
            console.print(Text(wrapped_line))
            row += 1

    end_row = max(image_height + 2, row + 1)
    print(f"\033[{end_row};1H", end="", flush=True)
