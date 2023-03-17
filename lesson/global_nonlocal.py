# global и nonlocal нужны только для изменения значений
# global может создать переменную, nonlocal не может создать переменную
# nonlocal ищет только во внешних скоупах, но не в глобальном
# не используйте global, nonlocal

counter = 100

def increment(value):
    return value + 1


if __name__ == '__main__':
    # counter = increment(counter)
    # print(counter)
    print(increment(counter))



