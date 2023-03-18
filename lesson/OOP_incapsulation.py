# Инкапсуляция заключается в сборе (класс) данных и методов для работы с ними
# И Предоставление пользователю публичного интерфейса (API)
# _ - (protected) знак того что этот атрибут не предназначен для прямого использования. Работа обьекта не гарантируется,
# при использовании таких атрибутов
# __ - (private) (псевдно приватность)(сокрытия данных нет) под капотом преобразуется в object._Class__attribute (только для случаев когда начинается с __ ) Name Mangling
# Явное лучше чем не явное, простое лучше чем сложное создатель pip, venv против __
# Публичный АПИ(интерфейс) - это контракт, все методы будут работать, внутреняя же реализация не гарантируется.
# Совет - делать одно _ для внутренних атрибутов и реализаций, не перебарщивать с __ и сеттерами/геттерами

class Person_two:
    def __init__(self, age):
        self._age = age

    def get_age(self):
        return self._age

    # def set_age(self, age):
    #     self.__age = age
    #
    # def get_age(self):
    #     return self.__age

class Person:
    def __init__(self, first_name, last_name, age):
        self.list = [first_name, last_name, age]
        # self._first_name = first_name
        # self._last_name = last_name
        # self.__age = age
        # self.__one__ = 1

    def set_age(self, age):
        if age < 1 or age > 120:
            raise ValueError(f'Age must be in range 1-120')
        self.list[2] = age

    def describe(self):
        print(f'I am {self.list[0]} {self.list[1]}, Im {self.list[2]} years old!')


if __name__ == '__main__':
    ivan = Person('Ivan', 'Petrov', 20)
    # ivan._Person__age = 100
    # ivan.set_age(1200)
    ivan.describe()
    # print(ivan.__dir__())
    # print(ivan._Person__age)
    ivan2 = Person_two(30)
    # ivan2._age = 50
    print(ivan2._age)

