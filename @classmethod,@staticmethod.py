# Создайте класc `Book` с методом `@classmethod`, который создает объект из
# строки "Название,Автор,Год".
#
# Добавьте в класс `Book` `@staticmethod` для проверки, является ли год выпуска
# допустимым(например, не отрицательным)

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

# self - это экземпляр класса Python для доступа к объекту, cls
# обозначает сам класс для модификации, влияющей на все экземпляры.

# my_string = "яблоко,банан,апельсин"
# result = my_string.split(",")
# print(result)   # Вывод: ['яблоко', 'банан', 'апельсин']

# @classmethod и @ staticmethod - это декораторы

    @classmethod
    def from_string(cls, book_string):
        title, author, year_str = book_string.split(",")
        year = int(year_str)
        return cls(title, author, year)

    @staticmethod
    def is_valid_year(year):
        return year >= 0

# Пример использования
book_str = "Война и мир,Лев Толстой,1869" # Инфа
book = Book.from_string(book_str) # ↑ (book_str) - Инфа

print(book.title) # Война и мир
print(book.author) # Лев Толстой
print(book.year) # 1869

print(Book.is_valid_year(book.year)) # True (совпадение)

