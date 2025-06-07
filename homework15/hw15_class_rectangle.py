from typing import Self


class Rectangle:
    """
    Class for 'Rectangle' description
    """
    def __init__(self, width: int | float, height: int | float):
        self.width = width
        self.height = height

    def get_square(self) -> int | float:
        """
        Returns rectangle's square
        """
        return self.width * self.height

    def __eq__(self, other: Self) -> bool:
        return self.get_square() == other.get_square()

    def __add__(self, other: Self):
        new_rectangle_square = self.get_square() + other.get_square()
        new_rectangle_width = new_rectangle_square / 2
        new_rectangle_height = new_rectangle_square / new_rectangle_width

        new_rectangle = Rectangle(new_rectangle_width, new_rectangle_height)

        return new_rectangle

    def __mul__(self, n: int | float):
        new_rectangle_square = self.get_square() * n
        new_rectangle_width = new_rectangle_square / 2
        new_rectangle_height = new_rectangle_square / new_rectangle_width

        new_rectangle = Rectangle(new_rectangle_width, new_rectangle_height)

        return new_rectangle

    def __str__(self):
        return f"Rectangle with sides {self.width} and {self.height}"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
print("Ok")
