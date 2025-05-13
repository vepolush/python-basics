def process_summa(number_1: int, number_2: int) -> int:
    result = number_1 + number_2
    return result


def process_division(divident: int, *, divisor: int) -> float:
    if not divisor:
        raise ValueError("zero as divisor was provided")
        # return 0.0
    quotient = divident / divisor
    return quotient


def process_substraction(*, subtrahend: int, minuend: int) -> int:
    difference = subtrahend - minuend
    return difference


def process_mut(number_1: int, number_2: int) -> int:
    result = number_1 * number_2
    return result
