"""The arithmetic operations, one function each."""


class CalcError(Exception):
    """An operation that has no result, such as division by zero."""


class DivisionByZero(CalcError):
    """Division by zero: exits 2, so scripts can tell it apart from other errors."""


def add(a: float, b: float) -> float:
    return a + b


def sub(a: float, b: float) -> float:
    return a - b


def mul(a: float, b: float) -> float:
    return a * b


def div(a: float, b: float) -> float:
    if b == 0:
        raise DivisionByZero("division by zero")
    return a / b


OPERATIONS = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div,
}
