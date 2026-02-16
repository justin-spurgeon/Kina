"""HTML output for Unicode art with configurable font size."""

from typing import List, Tuple


def art_to_html(art: str, font_size: int) -> str:
    """
    Return a complete HTML document that displays the art in a <pre> with
    monospace font and the given font size (px). Clamps font_size to at least 1.
    """
    size = max(1, font_size)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Dragon curve</title>
  <style>
    body {{ margin: 1rem; }}
    pre {{
      font-family: monospace;
      font-size: {size}px;
      white-space: pre;
      overflow: auto;
    }}
  </style>
</head>
<body>
<pre>{art}</pre>
</body>
</html>
"""


def art_to_html_multi_stage(stage_pairs: List[Tuple[str, int]]) -> str:
    """
    Return a complete HTML document that displays multiple art stages, each in its
    own <pre> with monospace font and a per-stage font size (px).
    stage_pairs: list of (art_string, font_size); font_size is clamped to at least 1.
    """
    if not stage_pairs:
        return art_to_html("", 16)

    pre_blocks = []
    for art, size in stage_pairs:
        px = max(1, size)
        pre_blocks.append(f'<pre style="font-size: {px}px;">{art}</pre>')

    body_content = "\n".join(pre_blocks)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Dragon curve (stages)</title>
  <style>
    body {{ margin: 1rem; }}
    pre {{
      font-family: monospace;
      white-space: pre;
      overflow: auto;
      margin: 1rem 0;
    }}
  </style>
</head>
<body>
{body_content}
</body>
</html>
"""
