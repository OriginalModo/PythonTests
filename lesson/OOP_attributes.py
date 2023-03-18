# LEGB-rule действует для атрибутов без приставок (self)
# для чего создание классов -  создаеться для разных независимых состояний обектов которые не пересекаются
# для self атрибутов поиск идет сначала в обьекте, потом в классе, затем у предков OCP(object-class-parent)
# если через self пытаться поменять неизменяемый атрибут (строка), то будет создана локальная копия
# если менять через self изменяемый атрибут, то изменится для всех обьектов класса
# cls - это ссылка на класс (не обьект!), питон передает его под капотом
# @classmethod используется для раоты с атрибутом класса и с другими методами класса
# @staticmethod не получает ссылок под капотом, это просто функция связанная с классом
# cls = BlueCat

class BlueCat:
    breed = 'Russian Blue'
    names = []
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.increment_count()
        BlueCat.increment_count()
        # BlueCat.breed = 'Other'
        # self.names.append(name)

    def meow(self):
        print(f"{self.name} of {self.breed} says: Meow!")

    @classmethod
    def increment_count(cls):
        cls.count += 1

    @classmethod
    def make_cat(cls, name):
        # print(cls)
        if name == 'Tom':
            return BlueCat('Tom', 2)
        elif name == 'Angela':
            return cls('Angela', 1)
        return cls('Ginger', 1)

    @staticmethod
    def get_human_age(age):
        return age * 8



if __name__ == '__main__':
    tom = BlueCat.make_cat('Tom')
    # tom = BlueCat('Tom', 2)
    angela = BlueCat.make_cat('Angela')
    # angela = BlueCat('Angela', 1)
    # tom.breed = 'Other'
    tom.meow()
    # tom.names.append('Ginger')
    angela.meow()
    # print(tom.breed)
    # print(tom.names)
    # print(angela.names)
    # print(BlueCat.count)
    # print(BlueCat.get_human_age(angela.age))
    print(angela.get_human_age(angela.age))