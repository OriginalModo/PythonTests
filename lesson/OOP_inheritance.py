# Inheritance - Наследование, это механизм получения доступа к данным и поведению своего предка.
# И расширению (изменения поведения) классов не меняя код
# IS-A является (наследование)
# HAS-A содержит (композиция)
# __ (два подчеркивания, private) сделаны для того чтобы НЕ ПЕРЕОПРЕДЕЛИТЬ АТРИБУТ ВАШЕГО ПРЕДКА

class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def calculate_total_bonus(self):
        return self.salary // 100 * self.bonus

    def __str__(self):
        return f"{self.__class__.__name__} {self.name}, salary={self.salary}, bonus={self.bonus}%," \
               f" total bonus={self.calculate_total_bonus()} rub"


class Cleaner(Employee):
    def __init__(self, name):
        super().__init__(name, 15000, 1)



class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, 45000, 15)


class CEO(Employee):
    def __init__(self, name):
        super().__init__(name, 105000, 100)

    def calculate_total_bonus(self):
        return 200_000


def calc_bonuses(employees: list[Employee]):
    for employee in employees:
        print(f'Calc bonus {employee.name}, it is = {employee.calculate_total_bonus()}')



if __name__ == '__main__':
    masha = Cleaner('Maria Ivanovna')
    print(masha)
    grisha = Manager('Grigoriy Petrovich')
    print(grisha)
    ivan_palych = CEO('Ivan Pavlovych')
    print(ivan_palych)
    a_list = [masha, grisha, ivan_palych]
    calc_bonuses(a_list)
    # print(calc_bonuses([masha, grisha, ivan_palych]))





# Primer Start
#
# class Cleaner:
#     def __init__(self, name):
#         self.name = name
#         self.salary = 15000
#         self.bonus = 1
#
#     def calculate_total_bonus(self):
#         return self.salary // 100 * self.bonus
#
# def __str__(self):
#     return f"Cleaner {self.name}, salary={self.salary}, bonus={self.bonus}%," \
#            f" total bonus={self.calculate_total_bonus()} rub"

#
# class Manager:
#     def __init__(self, name):
#         self.name = name
#         self.salary = 45000
#         self.bonus = 15
#
#     def calculate_total_bonus(self):
#         return self.salary // 100 * self.bonus
#
#     def __str__(self):
#         return f"Manager {self.name}, salary={self.salary}, bonus={self.bonus}%, total bonus={self.calculate_total_bonus()} rub"
#
#
# class CEO:
#     def __init__(self, name):
#         self.name = name
#         self.salary = 105000
#         self.bonus = 100
#
#     def calculate_total_bonus(self):
#         return self.salary // 100 * self.bonus
#
#     def __str__(self):
#         return f"CEO {self.name}, salary={self.salary}, bonus={self.bonus}%, total bonus={self.calculate_total_bonus()} rub"
#
#
# if __name__ == '__main__':
#     masha = Cleaner('Maria Ivanovna')
#     print(masha)
#     grisha = Manager('Grigoriy Petrovich')
#     print(grisha)
#     ivan_palych = CEO('Ivan Pavlovych')
#     print(ivan_palych)
