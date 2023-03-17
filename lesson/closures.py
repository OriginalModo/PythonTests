# Closure Замыкание
# Замыкание - внутренняя функция которая возвращаеться из внешней функции и при этом использует
# чужие переменные ( из внешнего scope )

# каждое состояние хранит свое состояние, они не пересекаются

# хранит состояние(данные), предоставляет интерфейс для работы с ними, "скрывает" данные, помогает избегать global


# def pow_(base):
#     def inner(value):
#         return value ** base
#     return inner

def pow_(base):
    return lambda value: value ** base


def names():
    all_names = []

    def inner(name: str) -> list:
        all_names.append(name)
        return all_names

    return inner


if __name__ == '__main__':
    boys = names()
    boys('Друг')
    pow__ = pow_(2)
    pow_2 = pow_(3)
    print(pow__(5))
    print(pow__(6))
    print(pow__(7))
    print(pow_2(5))
    print(pow_2(6))
    print(pow_2(7))
    print(boys.__closure__[0].cell_contents)
    p = pow_(2)
    print(p(5))

# Primer 3

# def counter():
#     count = 0
#
#     def inner(value: int) -> int:
#         nonlocal count
#         count += value
#         return count
#     return inner
#
# if __name__ == '__main__':
#     count = counter()
#     print(count(1))
#     print(count(1))
#     print(count(1))
#     print(count(-3))

# Primer 2

# def average():
#     values = []
#     def inner(value: int) -> float:
#         values.append(value)
#         return sum(values) / len(values)
#
#     return inner
#
# if __name__ == '__main__':
#     avg = average()
#     print(avg(10))
#     print(avg(20))
#     print(avg(30))

# Primer 1

# def names():
#     all_names = []
#
#     def inner(name: str) -> list:
#         all_names.append(name)
#         return all_names
#     return inner
#
# if __name__ == '__main__':
#     boys = names()
#     girls = names()
#     print(boys("John"))
#     print(boys("Peter"))
#     print(boys("Jane"))
#     print(girls("Fola"))
#     print(girls("Gola"))
#     print(girls("Dola"))
#     print(boys.__closure__[0].cell_contents)
