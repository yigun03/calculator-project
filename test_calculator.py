# test_calculator.py | 4칙연산 계산기 테스트 | 작성자: Alice
import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    # ── 덧셈 테스트 ──────────────────────────
    def test_add_positive(self):
        self.assertEqual(add(3, 5), 8)

    def test_add_negative(self):
        self.assertEqual(add(-3, -5), -8)

    def test_add_mixed(self):
        self.assertEqual(add(10, -3), 7)

    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)

    # ── 뺄셈 테스트 ──────────────────────────
    def test_subtract_positive(self):
        self.assertEqual(subtract(10, 3), 7)

    def test_subtract_negative(self):
        self.assertEqual(subtract(-5, -3), -2)

    # ── 곱셈 테스트 ──────────────────────────
    def test_multiply_positive(self):
        self.assertEqual(multiply(4, 5), 20)

    def test_multiply_negative(self):
        self.assertEqual(multiply(-4, 5), -20)

    def test_multiply_zero(self):
        self.assertEqual(multiply(100, 0), 0)

    def test_multiply_float(self):
        """소수점 곱셈"""
        self.assertAlmostEqual(multiply(0.1, 0.2), 0.02, places=5)

    # ── 나눗셈 테스트 ────────────────────────
    def test_divide_positive(self):
        self.assertEqual(divide(10, 2), 5.0)

    def test_divide_float(self):
        self.assertAlmostEqual(divide(1, 3), 0.333, places=3)

    def test_divide_large(self):
        self.assertEqual(divide(1000000, 1000), 1000.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_divide_by_zero_msg(self):
        with self.assertRaises(ValueError) as ctx:
            divide(5, 0)
        self.assertIn("Cannot divide by zero", str(ctx.exception))

    def test_divide_negative(self):
        """음수 나눗셈"""
        self.assertEqual(divide(-10, 2), -5.0)

if __name__ == '__main__':
    unittest.main()