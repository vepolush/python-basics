some_list = [5, 6, 7, 8, 7, 5, 7, 57, 85, 7, 7, 7, 7, 7, 41, 74, 74]


def is_number_more_than_5(number) -> bool:
    return number > 5


def is_number_more_than_6(number) -> bool:
    return number > 6


callable_validators = {
    5: is_number_more_than_5,
    6: is_number_more_than_6,
    "lambda": lambda arg: lambda: lambda number: number * 5,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
}

n1 = 10
n2 = 20
operation = "-"
res_lambda = callable_validators[operation](n1, n2)

res = callable_validators["lambda"](5)()(5)

# wanted_func = 6
# for item in some_list:
#     func = callable_validators[wanted_func](item)

# filtered_data = filter(is_number_more_than_5, some_list)
filtered_data = filter(lambda number: number > 5, some_list)
mapped_data = list(map(lambda number: number * 2, filtered_data))

# some_list.insert(0, 50000)
#
# print(next(mapped_data))
#
# print(next(filtered_data))
# print(list(filtered_data))
#
# print(next(mapped_data))
pass
