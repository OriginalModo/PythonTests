# Магические методы = dunder методы, методы которые начинаются и заканчиваются __
# __init__ по умолчанию не ждет агрументов
# __repr__ для программистов, возвращает строку, которой видно (и можно воссоздать) состояние обьекта
# __str__ для людей, возвращает строку
# если не реализован репр и стр, то будет возвращен адрес в памяти
# по умолчанию сравнивает адрес в памятиб в реализации лучше сразу проверить тип
# если методы сравнения не реализованы падает ошибка
# __contains__ для реализации проверки IN
# bool для самодельных обьектов всегда вернет True, для изменения поведения нужно написать  __bool__
# len вернет ошибку если не переопределить метод __len__
# чтобы обьет стал вызываемым (callable) нужно реализовать __call__, иначе ошибка
# __iter__ возвращает обьект итератор, тот кто реализует итер = Итерабл
# __next__ должен вернуть следующий обьект из контейнера, кто его реализует = Итератор for работает до StopIteration
# __getitem__ нужен для функционала [] (аналог списка и словаря), __setitem__ для присвоение через [], если не реализовать = ошибка
# если в обьекте не реализован __iter__ то для цикла будет использован __getitem__ там ожидается падание IndexError

class Banknote:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'Banknote({self.value})'

    def __str__(self):
        return f'Банкнота номиналов в {self.value} рублей'

    def __eq__(self, other):
        if other is None or not (other, Banknote):
            return False
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value

class Iterator:
    def __init__(self, container):
        self.container = container
        self.index = 0

    def __next__(self):
        if 0 <= self.index < len(self.container):
            value = self.container[self.index]
            self.index += 1
            return value
        raise StopIteration

class Wallet:

    def __init__(self, *banknotes: Banknote):
        self.container = []
        self.container.extend(banknotes)
        self.index = 0

    def __repr__(self):
        return f'Wallet({self.container})'

    def __contains__(self, item):
        return item in self.container

    def __bool__(self):
        return len(self.container) > 0  # bool(self.container)  len - очень быстрая не бояться его использовать

    def __len__(self):
        return len(self.container)

    def __call__(self, *args, **kwargs):
        return f'{sum(i.value for i in self.container)} рублей'

    # def __iter__(self):
    #     return Iterator(self.container)

    def __getitem__(self, item: int):
        if item < 0 or item > len(self.container):
            raise IndexError
        return self.container[item]

    def __setitem__(self, key, value: Banknote):
        if key < 0 or key > len(self.container):
            raise IndexError
        self.container[key] = value



    # def __iter__(self):
    #     return self

    def __next__(self):
        while 0 <= self.index < len(self.container):
            value = self.container[self.index]
            self.index += 1
            return value
        raise StopIteration

        # if 0 <= self.index < len(self.container):
        #     value = self.container[self.index]
        #     self.index += 1
        #     return value
        # else:
        #     raise StopIteration


if __name__ == '__main__':
    banknote = Banknote(50)
    fifty = Banknote(50)
    hundred = Banknote(100)
    wallet = Wallet(fifty, hundred, hundred)
    wallet[0] = Banknote(500)
    for money in wallet:
        print(money)


    # print(wallet[1])

    # for money in wallet:
    #     print(money)
    # for money in wallet:
    #     print(money)


    # print(len(wallet)) # __len__
    # print(wallet()) # __call__



    # print(Banknote(50) in wallet)

    # if wallet:
    #     print('!')

    # print(fifty >= hundred)
    # other = eval(repr(banknote)) # не балуйтесь с eval

    # print(f'{banknote!r}') # вывод __repr__
