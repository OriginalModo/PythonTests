# Обьект - сущность обьединяющая данные и методы для работы с ними (состояние и поведение)
# Чертеж-класс, обьект это дом.
# класс - этот новый тип данных, обьект -его конкретный представитель
# у любого обьекта есть id, значение и тип
# первая потребность для классов - когда не хватает встроеных типов, вторая - разное состояние
# метод - это функция которая принадлежит классу
# dunder дандер, магический метод    double under __dunder__


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def meow(self):
        print(f'{self.name} says: Meow!')

    def __add__(self, other): # +
        if isinstance(other, Cat):
            return Cat('Ginger', 0)



if __name__ == '__main__':
    tom = Cat('Tom', 2)
    angela = Cat('Angela', 1)
    print(tom)
    print(angela)
    tom.meow()
    angela.meow()
    print(tom.name)
    print(tom.age)
    ginger = tom + angela
    ginger.meow()
    # Cat.meow(tom) !!!

