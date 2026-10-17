"""The arithmetic operations, one function each."""


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


def power(a: float, b: float) -> float:
    try:
        result = a ** b
    except ZeroDivisionError:
        raise CalcError("zero to a negative power")
    except OverflowError:
        raise CalcError("result too large")
    if isinstance(result, complex):
        raise CalcError("result is not a real number")
    return result


OPERATIONS = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div,
    "pow": power,
}
