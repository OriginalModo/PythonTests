import pprint
from time import sleep

# List comprehenstion = Listcomps
# Generator expressions = genexp
# [ВЫРАЖЕНИЕ/ПРЕОБРАЗОВАНИЕ for element in ИСТОЧНИК if УСЛОВИЕ]
# переменные в листкомпс недоступны извне
# читается слева направо
# для словаря обязательно указать КЛЮЧ:ЗНАЧЕНИЕ
# генератор вернет обьект, а не коллекцию
# генератор ленивый, не выполняет действий и не занимает память
# генератор проверяет источник при создании!!!
# генератор одноразовый, если исчерпан то бросает StopIteration
# цикл перехватывает StopIteration
# используйте генексп вместо компс, кроме случаев когда нужна длина len или индексы

squares = [e*e for e in range(10) if e % 2 == 0]
text = 'hello world'
words = [word.capitalize() for word in text.split()]

ints = [-1, -2, 0, 3, -4]
positive = [i for i in ints if i > 0]

squares2 = []
for i in range(10):
    if i % 2==0:
        squares2.append(i*i)


letters = [letter for word in text.split() for letter in word if letter < 'l']

matrix = [list(range(x, x+3)) for x in range(3)]

unique_letters = {letter for word in text.split() for letter in word if letter < 'o'}

alphabet = {index: letter for index, letter in enumerate('abcasdasddffgghhh', 1)}

# positive_gen = (i for i in range(10_000_000_000) if i > 0)
positive_gen = (i for i in ints if i > 0)

def some_source():
    # open db
    # read file
    # calculate
    return 1,2,3

def some_filter(x):
    sleep(1)
    return True

def some_mapping(x):
    sleep(1)
    return x


if __name__ == '__main__':
    # pprint.pprint(matrix, indent=1, width=15)
    # print({v: k for k, v in alphabet.items()})
    # print(positive_gen)
    # print(next(positive_gen))
    # print(positive_gen)
    # print(next(positive_gen))
    # print(next(positive_gen))
    # gen = (i for i in some_source())
    # print(next(positive_gen))
    it = (some_mapping(i) for i in some_source() if some_filter(i))
    print(next(it))




