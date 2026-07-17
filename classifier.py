"""Code classification module."""

import math


def classify(code):
    """Map a numeric code to a letter.

    Codes 1 through 25 map to the letters "a" through "y" in order; any
    other value maps to "z".
    """
    is_finite_number = isinstance(code, (int, float)) and math.isfinite(code)
    is_whole_number = is_finite_number and code == int(code)
    is_mapped_code = is_whole_number and 1 <= code <= 25
    if is_mapped_code:
        return chr(ord("a") + int(code) - 1)
    return "z"
