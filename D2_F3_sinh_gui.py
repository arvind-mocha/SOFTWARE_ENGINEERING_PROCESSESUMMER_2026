"""
SOEN 6011 Delivery 2 - F3: Hyperbolic Sine sinh(x)
Student: Arvind Lakshmanan
Student ID: 40310757

This implementation calculates sinh(x) from scratch using the Maclaurin series:
    sinh(x) = x + x^3/3! + x^5/5! + ...

The mathematical implementation does not use math.sinh, math.exp, or any other
Python mathematical library function. Tkinter is used only for the graphical
user interface, as required for D2.
"""

import tkinter as tk
from tkinter import ttk

LOWER_LIMIT = -20.0
UPPER_LIMIT = 20.0
TOLERANCE = 0.000000000000001
MAX_TERMS = 200


class SinhInputError(Exception):
    """Raised when the user input cannot be used as a supported real number."""


class SinhConvergenceError(Exception):
    """Raised when the series does not reach the required tolerance."""


def absolute_value(value):
    """Return the non-negative size of a number without using abs()."""
    if value < 0:
        return -value
    return value
def is_nan(value):
    """Return True when value is NaN. NaN is the only float unequal to itself."""
    return value != value


def is_infinite_or_too_large(value):
    """Return True for positive or negative infinity and unsafe huge values."""
    return value > 1.0e308 or value < -1.0e308

def parse_supported_real_number(text):
    """Convert the user entry to a supported finite real number."""
    cleaned_text = text.strip()

    if cleaned_text == "":
        raise SinhInputError("Please enter one real number, such as -2, 0.5, or 3e-2.")

    try:
        x_value = float(cleaned_text)
    except ValueError as exc:
        raise SinhInputError(
            "The input must be one real number. Do not enter letters, commas, or multiple values."
        ) from exc

    if is_nan(x_value) or is_infinite_or_too_large(x_value):
        raise SinhInputError("The input must be a finite real number, not NaN or infinity.")

    if x_value < LOWER_LIMIT or x_value > UPPER_LIMIT:
        raise SinhInputError(
            "This D2 from-scratch implementation supports only -20 <= x <= 20. "
            "Please enter a value inside this range."
        )

    return x_value

if __name__ == "__main__":
    main()
