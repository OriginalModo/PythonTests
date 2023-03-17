# аналог def!!!
# можно писать всеб что допустимо после return u def
# не выполняются до вызова ()!!!
# можно писать без лямбд

from operator import attrgetter, itemgetter #они быстрее работают


fact = lambda number: number * fact(number - 1) if number > 1 else number
print(fact(5))
fact = lambda number: number * fact(number - 1) if number > 1 else (1 if number == 0 else number)

def square(x):
    return x ** 2


any_ = lambda: abracadabra
any_2 = lambda: square(use(it))

# square2 = lambda x: x ** 2
# eve_odd = lambda x: 'EVEN' if x % 2 == 0 else 'ODD'
def is_even(x):
    return x%2==0

def second(x):
    return x[1]

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Cat {self.name}, age is {self.age}"





if __name__ == '__main__':
    ints = list(range(10))
    # print(list(map(lambda y: y ** 2, filter(lambda x: x % 2 == 0, ints))))
    print([i**2 for i in ints if i%2==0])
    a_dict = {'a': 3, 'b': 2, 'd': 1, 'c': 4}# ('a'" 3)
    print(sorted(a_dict.items(), key=lambda x: x[1]))
    print(sorted(a_dict.items(), key=itemgetter(1)))
    print(sorted(a_dict.items(), key=second))
    cats = [Cat('Tom', 33), Cat('Angela', 48)]

    print(sorted(cats, key=lambda cat: cat.age))
    print(sorted(cats, key=attrgetter('age')))