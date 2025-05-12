some_list = [55, 656, 898, 55, 55, "Alex", 2222222222]
some_list2 = [55, 656, 898, 55, 1111111, "Alex", '5']
some_iterable = "b19uh4picm71f"

target_dict = {}

for elem in some_list:
    target_dict[elem] = None

unique_elem = set(some_list)

created_set = {555, 4545, 555}
created_set2 = set()
created_set3 = set(some_iterable)

is_5_in_created_set3 = '5' in created_set3
is_5_in_some_list2 = '5' not in some_list2

# adding
created_set.add("55555555555555555")
# created_set.add([])
created_set.add((3, ))

# remove
created_set.remove(4545)
created_set.discard(4545)

set1 = set(some_list)
set2 = set(some_list2)

# union
union_result1 = set1.union(set2)
union_result2 = set1 | set2

# common
common1 = set1.intersection(set2)
common2 = set1 & set2

# difference
dif1 = set1.difference(set2)
dif2 = set1 - set2

# common difference
common_dif = set1 ^ set2
common_dif2 = set1.symmetric_difference(set2)

for el in set1:
    print(el)

pass
