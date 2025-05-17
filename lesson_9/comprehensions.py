import sys

source_list = [2, 6, "kjhjhj", True, "data", [], 5.5, 5.5, 2]

# list comprehension


res = []
for elem in source_list:
    if type(elem) in (int, float):
        res.append(elem * 2)


# result_only_numbers_list = [item for item in source_list if type(item) in [int, float]]
result_numbers_x_2 = [
    item * 2 for item in source_list if isinstance(item, (int, float))
]
result_numbers_x_2_tuple = tuple(result_numbers_x_2)
results_with_true_false = True + False + True + 55


# set comprehension
set_result_1 = set(result_numbers_x_2)
set_result_2 = {
    candidate for candidate in source_list if isinstance(candidate, (int, float))
}

# dict comprehension
dict_result_1 = {number: number for number in result_numbers_x_2 if number >= 4}


# generator comprehension
result_generator = (item * 2 for item in source_list if isinstance(item, (int, float)))

print(sys.getsizeof(result_numbers_x_2))
print(sys.getsizeof(result_numbers_x_2_tuple))
print(sys.getsizeof(result_generator))

print(next(result_generator))
print(next(result_generator))
print(next(result_generator))
print(next(result_generator))
print(next(result_generator))
print(next(result_generator))

source_list.append(100)
source_list.append(100)

print(next(result_generator))
print(next(result_generator))


# list_from_generator = list(result_generator)
# for item in result_generator:
#     print(item)


pass
