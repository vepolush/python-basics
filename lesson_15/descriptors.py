class Money:
    def __init__(self):
        self.value = 0

    def __get__(self, instance, owner):
        print(instance.__dict__)
        print(owner)
        return self.value

    def __set__(self, instance, value):
        if hasattr(instance, "has_debt"):
            print("has debt attr")
        print(666666666)
        self.value = value

    def __delete__(self, instance):
        print(instance.money, 99999999999666666666666666)
        print(self.value, 99999999999666666666666666)
        if not instance.money:
            del self.value


class BankAccount:

    def __init__(self, user_name: str):
        self.user_name = user_name.title()

    money = Money()

    # @money.getter
    # def money(self):
    #     print(1111111111111)
    #     return self.__money
    #
    # @money.setter
    # def money(self, delta: int):
    #     if delta < 0 and abs(delta) >= self.__money:
    #         raise ValueError("no money")
    #     self.__money += delta
    #
    # @money.deleter
    # def money(self):
    #     del self.user_name
    #     del self.__money
    #     # self.__money = 0


ba = BankAccount("Adams")
setattr(ba, "has_debt", True)
print(ba.has_debt)
print(ba.money)
ba.money = 555
del ba.money
print(ba.money)
ba.money = 0
del ba.money
print(ba.money)
print(ba.__dict__)
