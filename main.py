#!/usr/bin/env python3
"""Resize every image in the in/ folder and write the results to out/."""

import argparse
import sys
from pathlib import Path

from PIL import Image, UnidentifiedImageError

SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff"}
ROOT = Path(__file__).resolve().parent
INPUT_DIR = ROOT / "in"
OUTPUT_DIR = ROOT / "out"


def resize_images(width: int, height: int) -> int:
    if not INPUT_DIR.is_dir():
        print(f"Input folder not found: {INPUT_DIR}", file=sys.stderr)
        print("Create it and put your images inside.", file=sys.stderr)
        return 1

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    images = sorted(
        path
        for path in INPUT_DIR.iterdir()
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS
    )

    if not images:
        print(f"No images found in {INPUT_DIR}")
        print("Supported formats: png, jpg, jpeg, webp, bmp, tiff")
        return 1

    saved = 0
    for path in images:
        destination = OUTPUT_DIR / path.name
        try:
            with Image.open(path) as image:
                resized = image.resize((width, height), Image.Resampling.LANCZOS)
                resized.save(destination)
        except (OSError, UnidentifiedImageError) as error:
            print(f"Skipped '{path.name}': {error}", file=sys.stderr)
            continue

        print(f"Saved {destination.name} ({width}x{height})")
        saved += 1

    if saved == 0:
        print("No images were resized.", file=sys.stderr)
        return 1

    print(f"Done. {saved} image(s) saved to {OUTPUT_DIR}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Resize every image in the in/ folder and save the results to out/."
    )
    parser.add_argument("width", type=int, help="output width in pixels")
    parser.add_argument("height", type=int, help="output height in pixels")
    args = parser.parse_args()

    if args.width < 1 or args.height < 1:
        parser.error("width and height must be positive integers")

    return args


def main() -> int:
    args = parse_args()
    return resize_images(args.width, args.height)


if __name__ == "__main__":
    raise SystemExit(main())
