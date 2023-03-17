# позиционные аргументы всегда идут в начале
# / все что слева = только позиционные аргументы
# *, - все, что справа - только keyward аргументы
# *args собирает все позиционные аргументы в кортеж
# **kwargs собирает все keyward аргументы в словарь



a, *b = 'abcd'


# def example(a, b, /, c, *, d):
#     print(a)
#     print(b)
#     print(c)

def example(a, b, *, c,  d):
    print(a)
    print(b)
    print(c)
    print(d)

def m_print(*args, **kwargs):
    print(f'Got keywards: {kwargs}')
    for arg in args:
        print(str(arg))

if __name__ == '__main__':
    # print(*[1,2,3])
    # example(a=1,c=2,b=3)
    # example(1, 2, d=True, c=False)
    m_print(1, 2, 3, 4, 5, sep=':', end='-', number=100)
    # print(1, 2, **{'sep': ':', 'end': '-'})
    # print(1, 2, sep=':', end='-')