"""CLI entrypoint: generate dragon curve Unicode art."""

import argparse
import sys
from pathlib import Path

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

    axiom = "aa"
    productions = {
        "a": "bdc",
        "b": "cfjaf",
        "c": "cbadej",
        "d": "dabe",
        "e": "efhcd",
        "f": "fg",
        "g": "gaef",
        "h": "hij",
        "i": "i",
        "j": "jkbcg",
        "k": "defcab",
    }

    output = ""
    outcount = 0
    acount = 0
    limit = 40

    for i in range(iterations):
        axiom = "".join(productions.get(c, c) for c in axiom)
        for c in axiom:
            if outcount % limit == 0:
                output += "\n 𐋣"
                limit -= 1
                limit = max(limit, 1)
                if limit == 1:
                    limit = 40
                outcount = 0
            outcount += 1
            if c == "a":
                acount += 1
                if acount % 30 == 0:
                    output += "\n"
                output += "⡕"
            elif c == "b":
                if acount > 80:
                    output += "_"
                else:
                    output += "⢶"
            elif c == "c":
                output += "⟣"
            elif c == "d": 	
                output += "╰╌ ╮"
            elif c == "e":
                output += "="
            elif c == "f":
                output += "-"
            elif c == "g":
                output += " ╰╌"
            elif c == "h":
                output += " +"
            elif c == "i":
                output += ": "
            elif c == "j":
                output += "╮┦"
            elif c == "k":
                output += "j"
            else:
                output += " "
    print(output)

if __name__ == "__main__":
    main()
