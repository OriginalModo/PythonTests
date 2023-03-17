# Функция - полноправный обьект (ОБЬЕКТ ПРВОГО КЛАССА или гражданин первого класса)
# внутренняя ункция может захватывать переменные из внешней
from functools import wraps


def logger(func):
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} started')
        result = 2 *func(*args, **kwargs)
        print(f'{func.__name__} finished')
        return result
    return wrapper

@logger
def summ(a, b): # в этот момент summ=wrapper
    return a+b

# def example(a):
#     def inner(b):
#         print(a+b)
#     inner(3)

if __name__ == '__main__':
    # function = logger(summ)
    # print(function(2, 3))
    # print(logger(summ)(2, 3))
    # summ = logger(summ)
    # print(summ(2, 5))
    print(summ(2, 3))


