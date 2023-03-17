# Именование! Называем вещи своими именами, коллекции во множественном числе, функции -что делают
# Всегда используем ф-строкиб Никогда не складываем строки
# не делаем тоб что происходит по-умолчанию (str(input())
# исполльзуем листкомпс и генэксп только если есть преобразование И/ИЛИ фильтрация
# предпочитаем листкопмс, генэксп map/filter
# использовать while True для вечных циклов
# если список не нужен, используем генэксп
# не используем range(len(list)), если нужен индекс используем enumerate
# используем if collection чтобы проверить что не пустая
# используем встроенные функции
# ловим конкретное исключениеб пишем информацию в ветке except

integers = [1, 2, 3, -11]
try:
    int('a')
except ValueError as e:
    print(e)
    print(' debil')


# integers = [1, 2, 3, 10]
# print(any(i < 0 for i in integers))

# integers = [1, 2, 3, -1]
# if bool(integers):
#     pass

# integers = [1, 2, 3]
# for index, element in enumerate(integers, 1):
#     print(f"{index}-{element}")


# print(''.join(str(x) for x in range(10) if x % 2 == 0))

# summa = sum(x for x in range(10) if x % 2 == 0)
# print(sum(x ** 2 for x in range(10) if x % 2 == 0))

# while True:
#     break

# integers = list(map(lambda x: x**2, filter(lambda x: x % 2 ==0, range(10))))
# integers1 = (x**2 for x in range(10) if x % 2 == 0)
# print(integers)
# print(integers1)



# integers = list(range(10))
# print(integers)


# a_dict = {1:1, 2:2}
#
# value = a_dict.get(3)
# print(value)



# value = input()
# print(value)
# print(type(value))

# value = 1
# text = 'text'
# integers = [1, 2, 3, 4, 5]
# student = ['Вечный студент', 30]
#
#
# def get_positives(integers: list) -> list:
#     return [i for i in integers if i > 0]



