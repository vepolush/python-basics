def second_index(text: str, some_str: str) -> int | None:
    """
    Returns the index of the second occurrence of the searched string in the string to search for
    """
    some_str_count = text.count(some_str)

    if some_str_count > 1:
        first_index = text.index(some_str)
        result_index = text.index(some_str, first_index + 1)

        return result_index
    else:
        return None


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
