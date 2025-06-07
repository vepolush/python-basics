# iterators
# generators
# coroutine
import asyncio

import time


some_list = [2, 5, 9]


# class McDonalds:
#
#     def __init__(self, orders: list[list]):
#         self.orders = orders
#
#     def __getitem__(self, idx):
#         print(idx, 555)
#         return 22, idx
#
#     def __len__(self):
#         return sum([len(order) for order in self.orders])
#
#
# mac = McDonalds(
#     orders=[
#         ["potato"],
#         ["potato", "cola"],
#         ["potato", "salad", "cola"],
#         ["potato"],
#         ["potato"],
#         ["potato"],
#     ]
# )
# print(len(mac), 555555)
#
# mac = iter(mac)
#
# print(next(mac))
# print(next(mac))
# print(next(mac))
#
# for i in mac:
#     print(22222222222222222)
#     print(i)


async def foo():
    print("go to db")
    await asyncio.sleep(3)
    print("returned")
    return 2222


async def foo2():
    print("go to db --- 2")
    var = await asyncio.sleep(2)
    print(var)
    print("returned ---- 2")
    return 2222


print(asyncio.run(foo2()))
# asyncio.run(foo2())


async def main():
    await asyncio.gather(
        foo(),
        foo2(),
        foo(),
        foo2(),
        foo(),
        foo(),
    )


print(asyncio.run(main()))
# foo()
# foo2()
# foo()
# foo2()
# foo()
# foo()
