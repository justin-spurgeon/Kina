"""CLI entrypoint: generate dragon curve Unicode art."""

import argparse
import sys
from pathlib import Path

from .art import grid_to_unicode
from .lsystem import expand_dragon
from .rasterize import segments_to_grid
from .turtle import interpret

DEFAULT_ITERATIONS = 10
MAX_ITERATIONS = 20
DEFAULT_WIDTH = 80
DEFAULT_HEIGHT = 24


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate dragon curve Unicode art (L-system)."
    )
    parser.add_argument(
        "--iterations",
        "-n",
        type=int,
        default=DEFAULT_ITERATIONS,
        help=f"L-system expansion iterations (default {DEFAULT_ITERATIONS}, max {MAX_ITERATIONS})",
    )
    parser.add_argument(
        "--width",
        "-w",
        type=int,
        default=DEFAULT_WIDTH,
        help=f"Grid width in characters (default {DEFAULT_WIDTH})",
    )
    parser.add_argument(
        "--height",
        "-H",
        type=int,
        default=DEFAULT_HEIGHT,
        help=f"Grid height in characters (default {DEFAULT_HEIGHT})",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=None,
        help="Also write output to this file (stdout is always printed)",
    )
    args = parser.parse_args()

    iterations = max(0, min(args.iterations, MAX_ITERATIONS))
    width = max(1, args.width)
    height = max(1, args.height)

    s = expand_dragon(iterations, max_iterations=MAX_ITERATIONS)
    segments = interpret(s, step_length=1.0)
    grid = segments_to_grid(segments, width, height)
    text = grid_to_unicode(grid)

    # Always print to stdout (UTF-8)
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")
    print(text)

    if args.output is not None:
        args.output.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
