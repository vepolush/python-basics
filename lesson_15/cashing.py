import time
from functools import cache, cached_property, lru_cache
from cachetools import cached, TTLCache


# @cache
# @lru_cache(maxsize=1)
@cached(cache=TTLCache(maxsize=5, ttl=3))
def foo(n=55):
    print("I go to database for data", n)
    time.sleep(1)
    print("I got data ")
    return n


# result = foo(n=66)
# result = foo(n=66)
# result = foo()
# time.sleep(1)
# result = foo(n=66)
# time.sleep(1)
# result = foo(n=66)
# print(111111111111111111111)


class Cat:
    def __init__(self, name):
        self.name = name

    @cached_property
    # @property
    def full_call(self):
        print(5555555555555)
        return f"{self.name} white"


cat = Cat("Barsik")
print(cat.full_call)
print(cat.full_call)
cat.name = "ghghg"
print(cat.full_call)
