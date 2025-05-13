def add_one(some_list: list) -> list | str:
    """
    Returns a list from digits that make up the value of the number added to 1
    """
    some_list_string = ''
    result_list_numbers = []

    for number in some_list:
        some_list_string += str(number)

    some_list_number_add_1 = int(some_list_string) + 1

    for digit in str(some_list_number_add_1):
        result_list_numbers.append(int(digit))

    return result_list_numbers


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
