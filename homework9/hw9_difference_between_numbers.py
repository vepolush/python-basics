def difference(*numbers: int | float) -> int | float:
    """
    Returns difference between the largest and the smallest numbers provided
    """
    if len(numbers) >= 2:
        max_number = max(numbers)
        min_number = min(numbers)

        difference_between_max_and_min = round(max_number - min_number, 1)

        return difference_between_max_and_min
    elif len(numbers) == 1:
        return numbers[0]
    return 0

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
