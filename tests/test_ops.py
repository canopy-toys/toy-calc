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

    def test_pow(self) -> None:
        self.assertEqual(ops.pow(2, 10), 1024)

    def test_pow_no_real_result(self) -> None:
        with self.assertRaises(ops.CalcError):
            ops.pow(-8, 1 / 3)

    def test_pow_zero_to_negative(self) -> None:
        with self.assertRaises(ops.CalcError):
            ops.pow(0, -1)
