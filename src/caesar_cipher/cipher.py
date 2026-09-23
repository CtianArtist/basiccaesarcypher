"""Pure Caesar cipher operations.

The functions in this module do not depend on Tkinter, which makes them easy
to reuse from another program and straightforward to test.
"""

from __future__ import annotations

import string

MIN_SHIFT = 1
MAX_SHIFT = 25
LOWERCASE_ALPHABET = string.ascii_lowercase
UPPERCASE_ALPHABET = string.ascii_uppercase


def _validate_shift(shift: int) -> None:
    """Raise ValueError when *shift* is outside the supported range."""
    if type(shift) is not int:
        raise ValueError("Shift must be an integer value.")

    if not MIN_SHIFT <= shift <= MAX_SHIFT:
        raise ValueError(
            f"Shift must be an integer between {MIN_SHIFT} and {MAX_SHIFT}."
        )


def caesar(text: str, shift: int, *, encrypting: bool = True) -> str:
    """Apply a Caesar shift to *text*.

    Only ASCII letters are shifted. All other characters are returned
    unchanged. ``shift`` must be an integer from 1 through 25.
    """
    if not isinstance(text, str):
        raise TypeError("Text must be a string.")

    _validate_shift(shift)
    effective_shift = shift if encrypting else -shift

    translation = str.maketrans(
        LOWERCASE_ALPHABET + UPPERCASE_ALPHABET,
        _rotate(LOWERCASE_ALPHABET, effective_shift)
        + _rotate(UPPERCASE_ALPHABET, effective_shift),
    )
    return text.translate(translation)


def encrypt(text: str, shift: int) -> str:
    """Encrypt *text* using a positive Caesar shift."""
    return caesar(text, shift)


def decrypt(text: str, shift: int) -> str:
    """Decrypt *text* using a positive Caesar shift."""
    return caesar(text, shift, encrypting=False)


def _rotate(alphabet: str, shift: int) -> str:
    """Return *alphabet* rotated by *shift*, including negative shifts."""
    offset = shift % len(alphabet)
    return alphabet[offset:] + alphabet[:offset]