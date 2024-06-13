import doctest
import unittest


def parse_input(expression: str) -> tuple:
    """
    This function takes a string expression and returns a tuple of two integers and an operator.

    >>> parse_input("1 + 1")
    (1, '+', 1)
    >>> parse_input("5 * 5")
    (5, '*', 5)
    """

    parts = expression.split()
    if len(parts) != 3:
        raise ValueError("Invalid input. Try things like 1 + 1 or 5 * 5.")
    try:
        operand1, operator, operand2 = int(parts[0]), parts[1], int(parts[2])
    except ValueError:
        raise ValueError("Invalid input. Try things like 1 + 1 or 5 * 5.")
    return operand1, operator, operand2


def calculate(operand1: int, operator: str, operand2: int) -> float:
    """
    This function takes two integers and an operator, and calculates the result.

    >>> calculate(1, '+', 1)
    2
    >>> calculate(5, '*', 5)
    25
    """

    match operator:
        case "+":
            return operand1 + operand2
        case "-":
            return operand1 - operand2
        case "*":
            return operand1 * operand2
        case "/":
            if operand2 == 0:
                raise ValueError("Division by zero is problematic.")
            return operand1 / operand2
        case _:
            return None


class TestParseInput(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(parse_input("1 + 1"), (1, "+", 1))
        self.assertEqual(parse_input("5 * 5"), (5, "*", 5))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            parse_input("1 +")


class TestCalculate(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(1, "+", 3), 4)

    def test_subtraction(self):
        self.assertEqual(calculate(23, "-", 11), 12)

    def test_multiplication(self):
        self.assertEqual(calculate(2, "*", 3), 6)

    def test_division(self):
        self.assertEqual(calculate(20, "/", 4), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            calculate(20, "/", 0)

    def test_division_result_not_int(self):
        self.assertAlmostEqual(calculate(10, "/", 3), 3.3333333, places=7)

    def test_negative_addition(self):
        self.assertEqual(calculate(-1, "+", -3), -4)

    def test_negative_subtraction(self):
        self.assertEqual(calculate(-3, "-", -1), -2)

    def test_negative_multiplication(self):
        self.assertEqual(calculate(-2, "*", -3), 6)

    def test_negative_division(self):
        self.assertEqual(calculate(-20, "/", -4), 5)

    def test_unknown_operator(self):
        self.assertIsNone(calculate(1, "%", 1))


if __name__ == "__main__":
    unittest.main(exit=False)
    doctest.testmod()
