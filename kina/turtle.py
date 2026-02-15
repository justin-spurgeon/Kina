"""Turtle interpreter for L-system strings. Emits line segments (x0, y0, x1, y1)."""

import math
from typing import List, Tuple

# 90° in radians; + = turn right (subtract), - = turn left (add)
TURN_ANGLE = math.pi / 10.4


def interpret(
    s: str,
    step_length: float = 1.0,
    initial_angle: float = math.pi / 2,
) -> List[Tuple[float, float, float, float]]:
    """
    Interpret the expanded L-system string as turtle commands.
    F = move forward and draw (emit segment); + = turn right 90°; - = turn left 90°.
    Returns list of segments (x0, y0, x1, y1) in world coordinates (y up).
    """
    segments: List[Tuple[float, float, float, float]] = []
    x, y = 0.0, 0.0
    angle = initial_angle

    for c in s:
        if c == "F":
            nx = x + step_length * math.cos(angle)
            ny = y + step_length * math.sin(angle)
            segments.append((x, y, nx, ny))
            x, y = nx, ny
        elif c == "+":
            angle -= TURN_ANGLE
        elif c == "-":
            angle += TURN_ANGLE
        # X, Y and any other char: no-op

    return segments
