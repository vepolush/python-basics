from inspect import isgenerator
from typing import Callable


def pow(x):
    return x ** 2


def some_gen(begin: int, end: int, func: Callable):
    """
    Returns one term of a numerical sequence whose law is specified using function

     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """
    for i in range(end):
        yield begin
        begin = func(begin)


gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
