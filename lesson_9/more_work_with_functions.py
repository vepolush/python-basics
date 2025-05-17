def is_number_more_than_5(number) -> bool:
    return number > 5


def generate_infinity_sequence(func):
    # print("give 1")
    # yield 1
    # print("rest")
    # yield 2
    # print("last")
    current = 1
    while True:
        yield current
        print(func(current))
        current += 1


infinity = generate_infinity_sequence(is_number_more_than_5)

print(next(infinity))
print(56565566)
print(next(infinity))
print(next(infinity))
print(next(infinity))
print(next(infinity))
print(next(infinity))
print(next(infinity))
print(next(infinity))
print(next(infinity))
print(next(infinity))
print(next(infinity))
print(next(infinity))
print(next(infinity))
