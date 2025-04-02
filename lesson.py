# Определить класс Работник
# В классе работник должны быть публичный, защищенный и приватный атрибуты
# Для приватных атрибутов реализовать методы получения и изменения
#
# Определить класс Программист, наследуемый от класса Работник,
# В классе Программист, должны быть публичный, защищенный и приватный атрибуты
# Для приватных атрибутов реализовать методы получения и изменения

class Worker: # Работник
    def __init__(self, name, salary, identifier, password): # <--- Исправлено
        self.name = name # Публичный атрибут (имя)
        self._salary = salary # Защищенный атрибут (зарплата)
        self.__identifier = identifier # Приватный атрибут (идентификатор)
        self.__password = password # Приватный атрибут (пароль)


    def get_identifier(self):
        return self.__identifier

    def set_identifier(self, new_identifier):
        self.__identifier = new_identifier


    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password

class Programmer(Worker): # Программист
    def __init__(self, name, salary, identifier, password, language, project, id_project):
        super().__init__(name, salary, identifier, password) # Вызов конструктора родительского класса (Работник)

        self.language = language
        self._project = project
        self.__id_project = id_project


    def get_id_project(self):
        return self.__id_project

    def set_id_project(self, new_id):
        self.__id_project = new_id

worker = Worker("Dima", 70000, "123", "f54")
print(f"Работника имя: {worker.name}")
print(f"Работника зарплата: {worker._salary}")
print(f"Работника идентификатор: {worker.get_identifier()}")
worker.set_password("new_password")
print(f"Работника пароль: {worker.get_password()}")


# Добавлен пример использования класса Programmer для полноты:
programmer = Programmer("Anna", 90000, "456", "initial_pass",
                        "Python", "WebDev", 1)
print(f"Имя программиста: {programmer.name}")
print(f"ID проекта: {programmer.get_id_project()}")
programmer.set_id_project(2)
print(f"Новый ID проекта: {programmer.get_id_project()}")
