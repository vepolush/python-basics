def common_elements() -> set:
    """
    Generates two lists using range for 100 elements. Returns set with intersected elements
    """
    multiples_of_3 = []
    multiples_of_5 = []

    for i in range(100):
        if i % 3 == 0:
            multiples_of_3.append(i)

        if i % 5 == 0:
            multiples_of_5.append(i)

    lists_intersection = set(multiples_of_3) & set(multiples_of_5)

    return lists_intersection


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")
