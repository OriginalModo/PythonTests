# Использует сет/гет а также проперти ТОЛЬКО при наличии логики в получении или установке атрибута

# Возможность установки/получения атрибутов с логикой
# Запретить менять атрибуты или добавить новые атрибуты
# __dict__ это атрибут обьектов в питоне, который хранит состояние  (Состояние - все атрибуты, всё что знает обьект)
# __setattr__ вызывается при попытке установить атрибут
# если добавить только @property без то @setter атрибуты менять нельзя
# __slots__ - создан для уменьшения панмяти, занимаемой обьектами ЗАМЕНЯТ СЛОВАРЬ __dict__ на Кортеж (tuple)

from pympler import asizeof


class Cat:
    # FIELDS = ('name', 'age')
    __slots__ = ('_name', '_age')

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def __repr__(self):
        return f"Cat(name={self.name}, age={self.age})"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise AttributeError("Name cant be empty")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 1 or value > 15:
            raise AttributeError('Age should be in range [1,15]')
        self._age = value





    # def __setattr__(self, key, value):
    #     if key not in self.FIELDS:
    #         raise AttributeError(f"Only allowed {self.FIELDS}")
    #     if key == 'name' and not value:
    #         raise AttributeError(f"Attribute '{key}' can't be set")
    #     if key == 'age' and (value < 1 or value > 15):
    #         raise AttributeError('Age should be in range [1,15]')
    #     self.__dict__[key] = value

# class Empty:
#     pass




if __name__ == '__main__':
    # empty = Empty()
    # empty.abra = 'cadabra'
    # print(empty.__dict__)
    tom = Cat('Tom', 11)

    # tom.age = 100
    # print(tom.__dict__.__sizeof__())
    print(tom.__sizeof__())
    print(asizeof.asizeof(tom))
    # tom.name10 = 10
    # print(asizeof.asizeof(tom))





