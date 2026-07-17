"""Code classification module."""

from string import ascii_lowercase

# Codes 1..25 map to the letters "a".."y" in order; any other code maps to "z".
_FIRST_CODE = 1
_LAST_MAPPED_CODE = 25
_DEFAULT_LETTER = "z"


def classify(code):
    """Map a numeric code to a letter.

    Codes ``1`` through ``25`` map to the letters ``"a"`` through ``"y"`` in
    order. Every other code maps to the default letter ``"z"``.
    """
    is_mapped_code = _FIRST_CODE <= code <= _LAST_MAPPED_CODE
    if is_mapped_code:
        return ascii_lowercase[code - _FIRST_CODE]
    return _DEFAULT_LETTER
