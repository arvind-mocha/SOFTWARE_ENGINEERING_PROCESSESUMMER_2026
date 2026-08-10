"""Accessible Tkinter calculator for F3: hyperbolic sine ``sinh(x)``.

SOEN 6011 - Delivery 3
Student: Arvind Lakshmanan
Student ID: 40310757

The numerical implementation computes ``sinh(x)`` from scratch with the
Maclaurin series. It does not use ``math.sinh``, ``math.exp``, factorial
helpers, NumPy, SciPy, or another mathematical library for the calculation.
"""

import tkinter as tk
from tkinter import ttk

__version__ = "1.1.0"

LOWER_LIMIT = -20.0
UPPER_LIMIT = 20.0
TOLERANCE = 0.000000000000001
MAX_TERMS = 200
WINDOW_TITLE = f"F3 Hyperbolic Sine Calculator - v{__version__}"


class SinhInputError(Exception):
    """Raised when the entered value is not a supported real number."""


class SinhConvergenceError(Exception):
    """Raised when the series does not reach the required tolerance."""


def absolute_value(value):
    """Return the non-negative magnitude of ``value`` without ``abs()``."""
    if value < 0:
        return -value
    return value


def is_nan(value):
    """Return whether ``value`` is NaN using the self-inequality property."""
    return value != value


def is_infinite_or_too_large(value):
    """Return whether ``value`` is infinite or outside a safe float range."""
    return value > 1.0e308 or value < -1.0e308


def parse_supported_real_number(text):
    """Convert text to one finite supported real number in ``[-20, 20]``."""
    cleaned_text = text.strip()

    if cleaned_text == "":
        raise SinhInputError(
            "Please enter one real number, such as -2, 0.5, or 3e-2."
        )

    try:
        x_value = float(cleaned_text)
    except ValueError as exc:
        raise SinhInputError(
            "The input must be one real number. Do not enter letters, "
            "commas, or multiple values."
        ) from exc

    if is_nan(x_value) or is_infinite_or_too_large(x_value):
        raise SinhInputError(
            "The input must be a finite real number, not NaN or infinity."
        )

    if x_value < LOWER_LIMIT or x_value > UPPER_LIMIT:
        raise SinhInputError(
            "This calculator supports only -20 <= x <= 20. "
            "Please enter a value inside this range."
        )

    return x_value


def calculate_sinh_from_scratch(x_value):
    """Calculate ``sinh(x)`` using a recurrence form of its Maclaurin series.

    The recurrence is::

        term_0 = x
        term_n = term_(n-1) * x^2 / ((2n)(2n + 1))

    Returns a tuple containing the approximation and the number of terms used.
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
    """Tkinter graphical interface for the F3 hyperbolic-sine calculator."""

    def __init__(self, root):
        """Configure the window, state variables, widgets, and shortcuts."""
        self.root = root
        self.root.title(WINDOW_TITLE)
        self.root.geometry("680x470")
        self.root.minsize(600, 410)

        self.input_value = tk.StringVar()
        self.status_value = tk.StringVar(
            value="Ready. Enter a real number from -20 to 20."
        )

        self.input_entry = None
        self.result_box = None

        self.create_widgets()
        self.bind_keyboard_shortcuts()

    def create_widgets(self):
        """Create the single-window, keyboard-navigable interface."""
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill="both", expand=True)

        self.create_header(main_frame)
        self.create_input_area(main_frame)
        self.create_button_area(main_frame)
        self.create_result_area(main_frame)

    @staticmethod
    def create_header(main_frame):
        """Create the title, version, and concise usage instructions."""
        title_label = ttk.Label(
            main_frame,
            text="F3: Hyperbolic Sine sinh(x)",
            font=("Arial", 18, "bold"),
        )
        title_label.pack(anchor="w")

        version_label = ttk.Label(
            main_frame,
            text=f"Version {__version__} | From-scratch Maclaurin series",
        )
        version_label.pack(anchor="w", pady=(2, 4))

        instruction_label = ttk.Label(
            main_frame,
            text=(
                "Enter one finite real number from -20 to 20. "
                "Press Enter or Alt+C to calculate."
            ),
            wraplength=620,
        )
        instruction_label.pack(anchor="w", pady=(0, 14))

    def create_input_area(self, main_frame):
        """Create a labelled, keyboard-focusable input field."""
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill="x", pady=(0, 10))

        input_label = ttk.Label(
            input_frame,
            text="Enter x (-20 to 20):",
            underline=0,
        )
        input_label.pack(side="left")

        self.input_entry = ttk.Entry(
            input_frame,
            textvariable=self.input_value,
            width=30,
            takefocus=True,
        )
        self.input_entry.pack(side="left", padx=(10, 0), fill="x", expand=True)
        self.input_entry.focus_set()
        self.input_entry.bind("<Return>", self.calculate)

    def create_button_area(self, main_frame):
        """Create the three primary action buttons in a consistent row."""
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill="x", pady=(4, 12))

        calculate_button = ttk.Button(
            button_frame,
            text="Calculate",
            command=self.calculate,
            takefocus=True,
        )
        calculate_button.pack(side="left")

        clear_button = ttk.Button(
            button_frame,
            text="Clear",
            command=self.clear,
            takefocus=True,
        )
        clear_button.pack(side="left", padx=(8, 0))

        exit_button = ttk.Button(
            button_frame,
            text="Exit",
            command=self.root.destroy,
            takefocus=True,
        )
        exit_button.pack(side="left", padx=(8, 0))

    def create_result_area(self, main_frame):
        """Create read-only output and a separate textual status message."""
        result_label = ttk.Label(main_frame, text="Result and explanation:")
        result_label.pack(anchor="w")

        self.result_box = tk.Text(
            main_frame,
            height=9,
            wrap="word",
            takefocus=True,
            font=("Arial", 11),
        )
        self.result_box.pack(fill="both", expand=True, pady=(5, 8))
        self.set_result_text("No calculation yet.")

        status_heading = ttk.Label(main_frame, text="Status:")
        status_heading.pack(anchor="w")

        status_label = ttk.Label(
            main_frame,
            textvariable=self.status_value,
            wraplength=620,
        )
        status_label.pack(anchor="w")

    def bind_keyboard_shortcuts(self):
        """Provide keyboard alternatives for the main GUI actions."""
        self.root.bind("<Alt-c>", self.calculate)
        self.root.bind("<Alt-C>", self.calculate)
        self.root.bind("<Alt-l>", self.clear)
        self.root.bind("<Alt-L>", self.clear)
        self.root.bind("<Escape>", self.close)

    def set_result_text(self, message):
        """Replace the result area text while keeping it read-only."""
        self.result_box.config(state="normal")
        self.result_box.delete("1.0", "end")
        self.result_box.insert("1.0", message)
        self.result_box.config(state="disabled")

    def calculate(self, _event=None):
        """Validate the entry, calculate ``sinh(x)``, and show the result."""
        try:
            x_value = parse_supported_real_number(self.input_value.get())
            result, terms_used = calculate_sinh_from_scratch(x_value)
            message = (
                f"Input x: {x_value:.15g}\n"
                f"sinh(x): {result:.15g}\n"
                "Algorithm: Maclaurin series calculated from scratch\n"
                f"Terms used: {terms_used}\n\n"
                "Series: sinh(x) = x + x^3/3! + x^5/5! + ..."
            )
            self.set_result_text(message)
            self.status_value.set("Calculation completed successfully.")
        except SinhInputError as error:
            self.set_result_text("Input error:\n" + str(error))
            self.status_value.set(
                "Input needs correction. Review the message above and retry."
            )
        except SinhConvergenceError as error:
            self.set_result_text("Calculation error:\n" + str(error))
            self.status_value.set(
                "The series did not reach the required tolerance."
            )

    def clear(self, _event=None):
        """Reset the input, output, status message, and keyboard focus."""
        self.input_value.set("")
        self.set_result_text("No calculation yet.")
        self.status_value.set(
            "Ready. Enter a real number from -20 to 20."
        )
        self.input_entry.focus_set()

    def close(self, _event=None):
        """Close the application; used by the Escape keyboard shortcut."""
        self.root.destroy()


def main():
    """Create and run the Tkinter application."""
    root = tk.Tk()
    SinhCalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
