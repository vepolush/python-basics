def find_unique_value(some_list:list) -> int | str:
    """
    Returns unique value or message if there are no unique values
    """
    repeating_numbers = []

    for index, number in enumerate(some_list):
        if number not in some_list[index + 1:] and number not in repeating_numbers:
            unique_number = number
            return unique_number
        else:
            repeating_numbers.append(number)

    return "There are no unique values"


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
assert find_unique_value([1, 1, 1, 1]) == "There are no unique values", 'Test4'
print("ОК")
