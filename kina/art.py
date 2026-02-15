"""Map a hit-count grid to density Unicode characters (░ ▒ ▓ █)."""

from typing import List

# Light to heavy block elements
DENSITY_CHARS = (" ", "▱", "ʰ◁", "○", "ʹ ▪ ..", "ᣖ         ", "ˉnoᣂsis")


def grid_to_unicode(
    grid: List[List[int]],
    max_hits_for_full: int = 6,
) -> str:
    """
    Convert 2D grid of hit counts to a string using density characters.
    Buckets: 0 -> ' ', 1 -> '░', 2 -> '▒', 3 -> '▓', 4+ -> '█' (or scale by max_hits_for_full).
    """
    if not grid:
        return ""

    # Normalize by max so we use full range of shades
    flat = [c for row in grid for c in row]
    max_count = max(flat) if flat else 0
    if max_count <= 0:
        return "\n".join("".join(DENSITY_CHARS[0] for _ in row) for row in grid)

    n = len(DENSITY_CHARS) - 1  # 0..n map to 1..n+1 chars (0 = space)
    lines = []
    for row in grid:
        line = []
        for count in row:
            if count <= 0:
                line.append(DENSITY_CHARS[0])
            else:
                # Map count to 1..n (1 = light, n = full block)
                idx = min(n, max(1, round((count / max_count) * n)))
                line.append(DENSITY_CHARS[idx])
        lines.append("".join(line))
    return "\n".join(lines)
