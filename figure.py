# Определить класс Фигура
# В классе фигура должны быть публичный, защищенный и приватный атрибуты
# Для приватных атрибутов реализовать методы получения и изменения

# Определить класс круг,квадрат и треугольник, наследуемый от класса фигура,
# В этих классе , должны быть публичный, защищенный и приватный атрибуты.
# В классах реализовать функции подсчета площади.

# Реализовать геттеры и сеттреы для классов.

import math

class Figure:
    def __init__(self, name, color, border):
        self.name = name  # публичный
        self._color = color  # защищенный
        self.__border = border  # приватный атрибут

    @property
    def border(self):
        return self.__border

    @border.setter
    def border(self, new_border):
        self.__border = new_border

class Circle(Figure):
    def __init__(self, name, color, border, radius):
        super().__init__(name, color, border)
        self.__radius = radius  # приватный атрибут

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, new_radius):
        self.__radius = new_radius

    def area(self):
        return math.pi * self.__radius ** 2

class Square(Figure):
    def __init__(self, name, color, border, side):
        super().__init__(name, color, border)
        self.__side = side  # приватный атрибут

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, new_side):
        self.__side = new_side

    def area(self):
        return self.__side ** 2

class Triangle(Figure):
    def __init__(self, name, color, border, base, height):
        super().__init__(name, color, border)
        self.__base = base  # приватный атрибут
        self.__height = height  # приватный атрибут

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, new_base):
        self.__base = new_base

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        self.__height = new_height

    def area(self):
        return 0.5 * self.__base * self.__height

# Пример использования
circle = Circle("Circle", "Red", 1, 5)
print(circle.area())  # Площадь круга

square = Square("Square", "Blue", 1, 4)
print(square.area())  # Площадь квадрата

triangle = Triangle("Triangle", "Green", 1, 3, 6)
print(triangle.area())  # Площадь треугольника


