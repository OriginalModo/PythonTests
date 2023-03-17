from collections import OrderedDict, ChainMap, Counter, defaultdict, deque, namedtuple
import csv

# !!!  hashable за время жизни обьект не меняется str, int, tuple если они состоят из не изменяемых обьектов


# OrderedDict нужен для действия со словарем где находим порядок элементов, например сравнение с учетом порядка,
# перестановки элементов с сохранением порядка. Платим памятью!

# ChainMap нужен для логического обьединения словарей для поиска информации, но при изменениях меняется первый словарь

# Counter нужен для подсчета элементов в последовательности, работает только с hashable

# defaultdict нужен для создания словаря со значениями по умолчанию. Значение подставляется при обращении к
# несуществующему ключу

# deque потокабезопасна, быстро оперирует с обеими сторонами

# namedtuple ужен для создания структуры данных, нечто среднее между стандартными типами и самописным классом,
# неизменяемый, позволяет обращаться по имени артибута, позволяет использовать индексы.

# namedtuple

Point = namedtuple('Point', 'x y')
with open('points.csv') as file:
    for line in csv.reader(file):
        point = Point._make(line)
        print(point)


# tom = ('Tom', 4, 'yellow')

# Cat = namedtuple('Car', 'name age color')
# tom = Cat('Tom', 4, 'yellow')
# print(tom)
# print(tom.age)




# deque

# with open('points.csv') as file:
#     a_deque = deque(file, maxlen=2)
#
# for line in a_deque:
#     print(line.rstrip())

# a_deque = deque([1, 2, 3], maxlen=3)
# print(a_deque)
# a_deque.append(4)
# print(a_deque)

# a_deque = deque()
# a_deque.append(1)
# print(a_deque)
# a_deque.appendleft(2)
# print(a_deque)
# print(a_deque.pop())
# print(a_deque)


# defaultdict

# a_dict = defaultdict(list)
# for char in 'hello':
#     a_dict[char].append(char)
#
# print(a_dict)

# a_dict = defaultdict(int)
# print('1' in a_dict)

# print(a_dict['aaadsdd'])

# a_dict = defaultdict(int)
# for char in 'hello':
#     a_dict[char] += 1
# print(sorted(a_dict.items(), key=lambda x: x[1], reverse=True))

# a_dict = defaultdict(int)
# print(int())


# Counter
# counter = Counter('hello')
# print(counter)
# print(counter.most_common(3))

# counter = Counter('hello')
# print(counter)
# counter.update('world')
# print(counter)


# ChainMap

# first = {1:1, 2:2, 3:3}
# second = {4:4, 5: 5}
#
# chain = ChainMap(first, second)
# print(chain)
# first[1]=100
# print(chain)
# chain[5]=200
# print(chain)

# print(5 in chain)


#OrderedDict

# first = {1: 1, 2: 2, 3:3}
# second = {2: 2, 1: 0}
#
# order1 = OrderedDict(first)
# order2 = OrderedDict(second)
# # print(order1==order2)
# order1.move_to_end(3,last=False)
# print(order1)
