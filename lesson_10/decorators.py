# print(55555)
# print
# some_custom_print = print
# some_custom_print(6666666666)
# print(id(print))
# print(print)
# print(id(some_custom_print))
# print(some_custom_print)
# print(print is some_custom_print)
from typing import Callable
from functools import wraps
import datetime

user = {
    "login": "123",
    "password": "123",
}


def base_decorator(callback):
    def wrapper(*args, **kwargs):
        result = callback(*args, **kwargs)
        return result

    return wrapper


def auth_decorator(callback: Callable) -> Callable:

    @wraps(callback)
    def wrapper(*args, **kwargs):
        print("auth_decorator before")
        login = input("login: ")
        password = input("password: ")
        if not (login == user["login"] and password == user["password"]):
            print("Access denied: watch add")

        result = callback(*args, **kwargs)

        # print(result)
        # print(callback.__name__)
        # print(callback.__doc__)
        print("auth_decorator after")
        return result

    # wrapper.__name__ = callback.__name__
    return wrapper


def create_logfile(file="log.csv"):
    def create_logfile_inner(callback: Callable) -> Callable:
        @wraps(callback)
        def wrapper(*args, **kwargs):
            print("create_logfile before")
            result = callback(*args, **kwargs)

            with open(file, mode="a", encoding="utf-8") as f:
                f.write(
                    f"{callback.__name__};{datetime.datetime.now()};{args};{kwargs};{result}\n"
                )
            print("create_logfile after")
            return result

        return wrapper

    return create_logfile_inner


@auth_decorator
@create_logfile("foo.csv")
def foo() -> None:
    print("function itself")
    print(55555555555)


# foo = decorator(foo)


@create_logfile()
def add_two_numbers(num1: int, num2: int) -> int:
    """get sum of two numbers"""
    return num1 + num2


# add_two_numbers = decorator(add_two_numbers)


# def strange_func(callback: Callable, *args, **kwargs):
#     print("some work before")
#     result = callback(*args, **kwargs)
#     if isinstance(result, int):
#         result += 55
#     print("some work after")
#     print(result)
#     return result


# strange_func(foo)
# strange_func(add_two_numbers, num1=5, num2=8)


# lst = [5, 9, 8]
# first, second, *rest = lst
# pass


# decorator = decorator(add_two_numbers)
# print(decorator())
# pass


result = add_two_numbers(5, num2=8)
result = add_two_numbers(10, num2=8)
result = add_two_numbers(num1=55, num2=8)
result = add_two_numbers(5, num2=8)
result = add_two_numbers(5, num2=8)
result2 = foo()
# print(add_two_numbers)


# print(foo)
# print(foo.__dict__)
# print(foo.__name__)
# foo.variable = 555
# print(foo.__dict__)
# foo.__name__ = "bla bla"
# print(foo.__name__)
pass