import unittest

from calc import ops


class OpsTest(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(ops.add(2, 3), 5)

    def test_sub(self) -> None:
        self.assertEqual(ops.sub(2, 3), -1)

    def test_mul(self) -> None:
        self.assertEqual(ops.mul(2, 3), 6)

    def test_div(self) -> None:
        self.assertEqual(ops.div(3, 2), 1.5)

    def test_div_by_zero(self) -> None:
        with self.assertRaises(ops.CalcError):
            ops.div(1, 0)

    def test_power(self) -> None:
        self.assertEqual(ops.power(2, 10), 1024)

    def test_power_fraction(self) -> None:
        self.assertEqual(ops.power(4, 0.5), 2)

    def test_power_zero_to_negative(self) -> None:
        with self.assertRaises(ops.CalcError):
            ops.power(0, -1)

    def test_power_complex_result(self) -> None:
        with self.assertRaises(ops.CalcError):
            ops.power(-8, 0.5)

    def test_power_overflow(self) -> None:
        with self.assertRaises(ops.CalcError):
            ops.power(10.0, 400.0)
