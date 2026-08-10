"""PyUnit tests for the SOEN 6011 D3 F3 sinh calculator."""

import unittest

from D3_F3_sinh_gui import (
    LOWER_LIMIT,
    UPPER_LIMIT,
    SinhInputError,
    absolute_value,
    calculate_sinh_from_scratch,
    is_infinite_or_too_large,
    is_nan,
    parse_supported_real_number,
)


class TestHelperFunctions(unittest.TestCase):
    """Verify subordinate functions used by the scratch implementation."""

    def test_absolute_value_positive(self):
        """Positive values remain unchanged."""
        self.assertEqual(absolute_value(4.5), 4.5)

    def test_absolute_value_negative(self):
        """Negative values become positive."""
        self.assertEqual(absolute_value(-4.5), 4.5)

    def test_nan_detection(self):
        """NaN is detected through self-inequality."""
        nan_value = float("nan")
        self.assertTrue(is_nan(nan_value))
        self.assertFalse(is_nan(1.0))

    def test_infinity_detection(self):
        """Positive and negative infinity are rejected."""
        self.assertTrue(is_infinite_or_too_large(float("inf")))
        self.assertTrue(is_infinite_or_too_large(float("-inf")))
        self.assertFalse(is_infinite_or_too_large(20.0))


class TestInputParsing(unittest.TestCase):
    """Verify valid and invalid user-input handling."""

    def test_accepts_integer_text(self):
        """Integer text is converted to a float."""
        self.assertEqual(parse_supported_real_number("3"), 3.0)

    def test_accepts_decimal_and_scientific_notation(self):
        """Supported decimal and scientific notation are accepted."""
        self.assertEqual(parse_supported_real_number(" -2.5 "), -2.5)
        self.assertEqual(parse_supported_real_number("3e-2"), 0.03)

    def test_accepts_boundaries(self):
        """The documented lower and upper boundaries are valid."""
        self.assertEqual(
            parse_supported_real_number(str(LOWER_LIMIT)), LOWER_LIMIT
        )
        self.assertEqual(
            parse_supported_real_number(str(UPPER_LIMIT)), UPPER_LIMIT
        )

    def test_rejects_blank_input(self):
        """Blank input raises the custom input error."""
        with self.assertRaises(SinhInputError):
            parse_supported_real_number("   ")

    def test_rejects_non_numeric_input(self):
        """Letters and malformed numeric input are rejected."""
        with self.assertRaises(SinhInputError):
            parse_supported_real_number("abc")
        with self.assertRaises(SinhInputError):
            parse_supported_real_number("1,2")

    def test_rejects_nan_and_infinity(self):
        """Non-finite float values are rejected."""
        with self.assertRaises(SinhInputError):
            parse_supported_real_number("nan")
        with self.assertRaises(SinhInputError):
            parse_supported_real_number("inf")
        with self.assertRaises(SinhInputError):
            parse_supported_real_number("-inf")

    def test_rejects_out_of_range_values(self):
        """Values just outside the documented range are rejected."""
        with self.assertRaises(SinhInputError):
            parse_supported_real_number("20.0001")
        with self.assertRaises(SinhInputError):
            parse_supported_real_number("-20.0001")


class TestSinhCalculation(unittest.TestCase):
    """Verify numerical behavior of the Maclaurin recurrence."""

    def assert_sinh_close(self, x_value, expected, places=12):
        """Check the approximation and ensure at least one term was used."""
        actual, terms_used = calculate_sinh_from_scratch(x_value)
        self.assertAlmostEqual(actual, expected, places=places)
        self.assertGreaterEqual(terms_used, 1)

    def test_zero(self):
        """sinh(0) is exactly zero."""
        result, terms_used = calculate_sinh_from_scratch(0.0)
        self.assertEqual(result, 0.0)
        self.assertEqual(terms_used, 1)

    def test_common_positive_values(self):
        """Known positive values are approximated accurately."""
        self.assert_sinh_close(0.5, 0.5210953054937474)
        self.assert_sinh_close(1.0, 1.1752011936438014)
        self.assert_sinh_close(3.0, 10.017874927409903)

    def test_common_negative_values(self):
        """Known negative values preserve the odd-function sign."""
        self.assert_sinh_close(-0.5, -0.5210953054937474)
        self.assert_sinh_close(-1.0, -1.1752011936438014)
        self.assert_sinh_close(-3.0, -10.017874927409903)

    def test_supported_boundaries(self):
        """The algorithm remains accurate at the supported boundaries."""
        self.assert_sinh_close(20.0, 242582597.70489514, places=6)
        self.assert_sinh_close(-20.0, -242582597.70489514, places=6)

    def test_odd_function_property(self):
        """The implementation preserves sinh(-x) = -sinh(x)."""
        positive, _ = calculate_sinh_from_scratch(7.25)
        negative, _ = calculate_sinh_from_scratch(-7.25)
        self.assertAlmostEqual(negative, -positive, places=12)


if __name__ == "__main__":
    unittest.main(verbosity=2)
