"""Small driver used only to demonstrate pdb for D3 evidence."""

from D3_F3_sinh_gui import calculate_sinh_from_scratch


def run_demo():
    """Calculate a known value while stepping through with pdb."""
    x_value = 1.0
    result, terms_used = calculate_sinh_from_scratch(x_value)
    print("x =", x_value)
    print("sinh(x) =", format(result, ".15g"))
    print("terms used =", terms_used)


if __name__ == "__main__":
    run_demo()
