"""CLI entrypoint: generate dragon curve Unicode art."""

import argparse
import sys
from pathlib import Path
import random

DEFAULT_ITERATIONS = 10
MAX_ITERATIONS = 20
MAX_WIDTH = 100

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

    parser.add_argument(
        "--width",
        "-w",
        type=int,
        default=MAX_WIDTH,
        help=f"Maximum width of the output (default {MAX_WIDTH})",
    )

    args = parser.parse_args()

    iterations = max(0, min(args.iterations, MAX_ITERATIONS))

    axiom = "haabkj"
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
        "d": "⢭\n",
        "e": "⢈",
        "f": "⢀",
        "g": "⡎",
        "h": "⡁\n",
        "i": "▍ ",
        "j": ".",
        "k": "⣀ :\t",
    }

    output = ""
    width = 0

    for i in range(iterations):
        axiom = "".join(productions.get(c, c) for c in axiom)
        for c in axiom:
            symbol = symbols.get(c, c)
            width += len(symbol)
            if width > args.width:
                output += "\n\t"
                width = 0
            output += symbol

    print(output)

if __name__ == "__main__":
    main()
