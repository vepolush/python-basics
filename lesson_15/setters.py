class BankAccount:

    def __init__(self, user_name: str, money: int):
        self.user_name = user_name.title()
        self.__money = money

    money = property()

    @money.getter
    def money(self):
        print(1111111111111)
        return self.__money

    @money.setter
    def money(self, delta: int):
        if delta < 0 and abs(delta) >= self.__money:
            raise ValueError("no money")
        self.__money += delta

    @money.deleter
    def money(self):
        del self.user_name
        del self.__money
        # self.__money = 0


ba = BankAccount("Adams", 1000)
ba.money = -110
del ba.money
# ba.__money = 5000
# print(ba.money)
print(ba.__dict__)
