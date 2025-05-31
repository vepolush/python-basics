class MuteAnimalError(Exception):
    pass


def foo():
    raise ValueError()


def foo1():
    raise AttributeError()


def foo2():
    foo()
    foo1()


class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_noise(self):
        raise MuteAnimalError()


class Dog(Animal):
    def make_noise(self):
        print("bark-bark")

    # def __getattribute__(self, item):
    #     print(f"__getattribute__ called for {item}")
    #     return super().__getattribute__(item)
    #
    # def __getattr__(self, item):
    #     print(5555555555555)
    #     print(f"__getattr__ called for missing attribute: {item}")
    #     return f"Default value for {item}"


class Worm(Animal):
    pass


dog = Dog("pie")
worm = Worm("casper")
dog.make_noise()
dog.age = 5
# print(dog.weight, 666666666666666)


def make_feed(animal: Animal):
    print(f"Feed {animal}")


# value = 3
# try:
#     # foo2()
#     # 1 / 0
#     warm.make_noise()
#     value = 10
# except MuteAnimalError:
#     print("not implemented")
#     raise
# except ZeroDivisionError:
#     print("not implemented zero")
#     raise
# else:
#     print("555555555555555555555555555")
# finally:
#     print("9999999999999999999999999")
#     value = 20
#
# print(value)
# make_feed(dog)

try:
    total_spends = dog.age * 20000
except AttributeError:
    print("Age attribute not set")
    total_spends = 0

print(total_spends)


if age := getattr(worm, "age", 0):
    total_spends_warm = age * 2
else:
    total_spends_warm = 0


# if hasattr(warm, "age"):
#     total_spends_warm = warm.age * 2
# else:
#     total_spends_warm = 0
#
# print(total_spends_warm)
####################################
# age = getattr(warm, "age", 0)
# total_spends_warm = age * 2
# print(total_spends_warm)


# total_spends_warm = worm.age * 2 if hasattr(worm, 'age') else 0
# print(total_spends_warm)


class NotPositiveError(Exception):
    pass


def get_rectangle_perimeter(width: int, height: int) -> int:
    if any([width < 0, height < 0]):
        raise NotPositiveError()
    result = width * height
    return result


res = get_rectangle_perimeter(4, 2)
print(res)
