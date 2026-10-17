"""The arithmetic operations, one function each."""

import math


class CalcError(Exception):
    """An operation that has no result, such as division by zero."""


def add(a: float, b: float) -> float:
    return a + b


def sub(a: float, b: float) -> float:
    return a - b


def mul(a: float, b: float) -> float:
    return a * b


def div(a: float, b: float) -> float:
    if b == 0:
        raise CalcError("division by zero")
    return a / b


def pow(a: float, b: float) -> float:
    try:
        return math.pow(a, b)
    except (ValueError, ZeroDivisionError) as e:
        raise CalcError(f"no real result for pow {a} {b}") from e
    except OverflowError as e:
        raise CalcError("result too large") from e


OPERATIONS = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div,
    "pow": pow,
}
