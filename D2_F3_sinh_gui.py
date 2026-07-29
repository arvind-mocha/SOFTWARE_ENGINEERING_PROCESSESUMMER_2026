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

def calculate_sinh_from_scratch(x_value):
    """
    Calculate sinh(x) using the Maclaurin series.

    Recurrence used:
        term_0 = x
        term_n = term_(n-1) * x^2 / ((2n)(2n + 1))

    This avoids factorial and exponentiation library functions.
    """
    if x_value == 0.0:
        return 0.0, 1

    total = x_value
    term = x_value
    x_squared = x_value * x_value
    iteration = 1

    while iteration <= MAX_TERMS:
        denominator = (2 * iteration) * (2 * iteration + 1)
        term = term * x_squared / denominator
        total = total + term

        relative_stop = TOLERANCE * (1.0 + absolute_value(total))
        if absolute_value(term) <= relative_stop:
            return total, iteration + 1

        iteration = iteration + 1

    raise SinhConvergenceError(
        "The calculation did not converge within the iteration limit. "
        "Try an input closer to zero."
    )

class SinhCalculatorApp:
    """Tkinter graphical uttk.Labelface for thtextvariablelculator."""

    def __init__(self, root):
        self.root = root
        self.root.title("F3 Hyperbolic Sine Calculator - D2")
        self.root.geometry("640x420")
        self.root.minsize(560, 360)

        self.input_value = tk.StringVar()
        self.status_value = tk.StringVar(value="Enter a real number and click Calculate.")

        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill="both", expand=True)

        title_label = ttk.Label(
            main_frame,
            text="F3: Hyperbolic Sine sinh(x)",
            font=("Arial", 18, "bold"),
        )
        title_label.pack(anchor="w")

        subtitle_label = ttk.Label(
            main_frame,
            text="From-scratch Maclaurin series implementation using Tkinter GUI",
        )
        subtitle_label.pack(anchor="w", pady=(2, 14))

        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill="x", pady=(0, 10))

        input_label = ttk.Label(input_frame, text="Enter x (-20 to 20):")
        input_label.pack(side="left")

        input_entry = ttk.Entry(input_frame, textvariable=self.input_value, width=28)
        input_entry.pack(side="left", padx=(10, 0))
        input_entry.focus()
        input_entry.bind("<Return>", self.calculate)

        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill="x", pady=(4, 12))

        calculate_button = ttk.Button(button_frame, text="Calculate", command=self.calculate)
        calculate_button.pack(side="left")

        clear_button = ttk.Button(button_frame, text="Clear", command=self.clear)
        clear_button.pack(side="left", padx=(8, 0))

        exit_button = ttk.Button(button_frame, text="Exit", command=self.root.destroy)
        exit_button.pack(side="left", padx=(8, 0))

        result_label = ttk.Label(main_frame, text="Result and explanation:")
        result_label.pack(anchor="w")

        self.result_box = tk.Text(main_frame, height=9, wrap="word")
        self.result_box.pack(fill="both", expand=True, pady=(5, 8))
        self.result_box.insert("1.0", "No calculation yet.")
        self.result_box.config(state="disabled")

        status_label = ttk.Label(main_frame, textvariable=self.status_value)
        status_label.pack(anchor="w")


if __name__ == "__main__":
    main()
