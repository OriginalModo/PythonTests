# yield показывает что функция генератор, возвращает обьект генератор
# генератор ленивый (lazy) одноразовый, кидает StopIteration при исчерпании
# после выполнения yield встает на паузу,
# любая функция после return забывает(сборщик мусора)


squares = (i ** 2 for i in range(0, 11, 2))


def squares2():
    print("Generator working...")
    for i in range(0, 11, 2):
        yield i ** 2



def pause():
    print("Generator working...")
    while True:
        print(a)
        yield a

a = 10
gen = pause()
print(next(gen))
a = 20
print(next(gen))
a = 100500
print(next(gen))