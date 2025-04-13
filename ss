# Определить класс Фигура
# В классе фигура должны быть публичный, защищенный и приватный атрибуты
# Для приватных атрибутов реализовать методы получения и изменения

# Определить класс круг,квадрат и треугольник, наследуемый от класса фигура,
# В этих классе , должны быть публичный, защищенный и приватный атрибуты.
# В классах реализовать функции подсчета площади.

# Реализовать геттеры и сеттреы для классов.

class figure:
    def __init__(self, name, color, border):
        self.name = name
        self._color = color
        self.__border = border

    @property

    def get_border(self):
        return self.__border
    
    @border.setter
    def set_border(self, new_border):
        self.__border = new_border
