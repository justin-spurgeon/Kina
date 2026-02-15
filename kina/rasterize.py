"""Rasterize line segments to a 2D grid with hit counts (Bresenham)."""

from typing import List, Tuple


def bresenham(
    x0: int, y0: int, x1: int, y1: int,
) -> List[Tuple[int, int]]:
    """Return list of (col, row) integer cells that the line passes through."""
    cells = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    x, y = x0, y0

    while True:
        cells.append((x, y))
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy

    return cells


def segments_to_grid(
    segments: List[Tuple[float, float, float, float]],
    width: int,
    height: int,
    padding: int = 1,
) -> List[List[int]]:
    """
    Scale and translate segments to fit (width x height), then rasterize with
    Bresenham. Returns 2D grid (row-major: grid[y][x]) of hit counts.
    Coordinate: row 0 = top (max world y), row height-1 = bottom (min world y).
    """
    if not segments:
        return [[0] * width for _ in range(height)]

    # Bounding box in world coords
    all_x = []
    all_y = []
    for (x0, y0, x1, y1) in segments:
        all_x.extend((x0, x1))
        all_y.extend((y0, y1))
    min_x, max_x = min(all_x), max(all_x)
    min_y, max_y = min(all_y), max(all_y)
    span_x = max_x - min_x or 1.0
    span_y = max_y - min_y or 1.0

    # Usable grid area after padding
    w = max(1, width - 2 * padding)
    h = max(1, height - 2 * padding)

    # Scale to fit, preserving aspect
    scale = min(w / span_x, h / span_y)
    ox = padding + (w - span_x * scale) / 2 - min_x * scale
    oy = padding + (h - span_y * scale) / 2 - min_y * scale

    def world_to_cell(wx: float, wy: float) -> Tuple[int, int]:
        cx = int(round(wx * scale + ox))
        cy = int(round(wy * scale + oy))
        # Flip y so row 0 = top (max world y)
        row = height - 1 - cy
        return (cx, row)

    grid: List[List[int]] = [[0] * width for _ in range(height)]

    for (x0, y0, x1, y1) in segments:
        c0 = world_to_cell(x0, y0)
        c1 = world_to_cell(x1, y1)
        for (cx, row) in bresenham(c0[0], c0[1], c1[0], c1[1]):
            if 0 <= row < height and 0 <= cx < width:
                grid[row][cx] += 1

    return grid
