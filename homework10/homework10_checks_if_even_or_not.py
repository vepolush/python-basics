def is_even(digit: int) -> bool:
    """
    Return True is provided number is even, False overwise
    """
    return True if digit % 2 == 0 else False

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')
