# Vendored from https://github.com/kvoss/lsystem (BSD-2-Clause)
# Minimal L-system string expansion only.

from itertools import islice


class LSystemI:
    def __init__(self, word="", productions=None):
        self.word = word
        self.productions = dict() if productions is None else productions

    def __iter__(self):
        return self

    def __next__(self):
        old = self.word
        self.word = "".join(self.productions.get(c, c) for c in self.word)
        return old


class LSystem:
    """Container for an L-System. Use indexing to get nth generation: LSystem(...)[n]."""

    def __init__(self, variables=None, axiom="", consts=None, productions=None):
        self.variables = list() if variables is None else variables
        self.axiom = axiom
        self.consts = list() if consts is None else consts
        self.productions = dict() if productions is None else productions

    def __getitem__(self, n):
        """Return the nth generation string, or the axiom if n is 0."""
        iterable = LSystemI(self.axiom, self.productions)
        return next(islice(iterable, n, None), self.axiom)


# Dragon curve: axiom FX, X -> X+YF+, Y -> -FX-Y
DRAGON_AXIOM = "FX"
DRAGON_PRODUCTIONS = {
    "X": "X+YF+",
    "Y": "-FX-Y--",
}


def expand_dragon(iterations: int, max_iterations: int = 20) -> str:
    """Expand the dragon curve L-system for the given number of iterations."""
    n = max(0, min(iterations, max_iterations))
    system = LSystem(axiom=DRAGON_AXIOM, productions=DRAGON_PRODUCTIONS)
    return system[n]
