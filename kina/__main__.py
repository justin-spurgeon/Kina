"""CLI entrypoint: generate dragon curve Unicode art."""

import argparse
import sys
from pathlib import Path
import random

DEFAULT_ITERATIONS = 10
MAX_ITERATIONS = 20
DEFAULT_WIDTH = 80
DEFAULT_HEIGHT = 24


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate Unicode art (L-system)."
    )
    parser.add_argument(
        "--iterations",
        "-n",
        type=int,
        default=DEFAULT_ITERATIONS,
        help=f"L-system expansion iterations (default {DEFAULT_ITERATIONS}, max {MAX_ITERATIONS})",
    )

    args = parser.parse_args()

    iterations = max(0, min(args.iterations, MAX_ITERATIONS))

    axiom = "haab"
    productions = {
        "a": "aaab",
        "b": "cfjaf",
        "c": "c",
        "d": "dabe",
        "e": "e",
        "f": "f",
        "g": "gaef",
        "h": "hij",
        "i": "i",
        "j": "j",
        "k": "dk",
    }

    symbols = {
        "a": "⢚",
        "b": "⣲",
        "c": "⢖",
        "d": "⢭",
        "e": "⢈",
        "f": "⢀",
        "g": "⡎",
        "h": "⡁",
        "i": "▍ ",
        "j": "▔\n",
        "k": "⣀ ",
    }

    output = ""

    for i in range(iterations):
        axiom = "".join(productions.get(c, c) for c in axiom)
        for c in axiom:
            output += symbols.get(c, c)

    print(output)

if __name__ == "__main__":
    main()
