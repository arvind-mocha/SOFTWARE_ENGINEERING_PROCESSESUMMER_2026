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

if __name__ == "__main__":
    main()
