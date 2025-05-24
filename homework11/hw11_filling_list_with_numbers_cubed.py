from inspect import isgenerator
from typing import Generator


def generate_cube_numbers(end: int) -> Generator:
    """
    Returns numbers cubed from two to 'end'
    """
    number_count = 2
    number_cubed = number_count ** 3

    while number_cubed <= end:
        number_count += 1
        yield number_cubed
        number_cubed = number_count ** 3


gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
print("Ok")
