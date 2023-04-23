# DRY - don't repeat yourself - не повторяйся
# YAGNI - You aren't gonna need it - это не понадобится
# KISS - Keep it simple, stupid - будь проще             # простое лучше чем сложное
# POLA - Principle of Least Astonishment - не удивляй пользователя
# EAFP - Easier to Ask Forgiveness than Permission - проще извиниться, чем просить разрешение (сначала действуй)
# EAFP - Оптимистичное програмирование
# LBYL - Look Before You Leap - смотри, прежде чем прыгнуть (сначала спроси)
# LBYL - Защитное програмирование
from Tools.scripts.win_add2path import PATH


# DRY


# def func():
#     # some code
#     with open('test.txt') as file:
#         result = file.readlines()
#     return result
#
#
# def two():
#     # some code
#     with open('test2.txt') as file:
#         result = file.readlines()
#     return result


def func():
    # some code
    try:
        return read_from_file('test.txt')
    except FileNotFoundError as error:
        print(f'{error}')


def two():
    # some code
    return read_from_file('test2.txt')



def read_from_file(name):
    with open(f'folder/{name}') as file:
        result = file.readlines()
    return result

# END DRY

# YAGNI


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f'{self.name} says: Meow!')


    def scratch(self):
        #code
        pass

# END YAGNI

# EAFP # Python way

def func():
    # some code
    try:
        return read_from_file_eafp('test.txt')
    except:
        # простите
        pass



def two():
    # some code
    return read_from_file('test2.txt')



def read_from_file_eafp(name):
    try:
        with open(f'folder/{name}') as file:
            result = file.readlines()
        return result
    except:
        # sorry
        pass

# END EAFP


# LBYL

    def read_from_file_lbyl(name):
        if PATH(f'folder/{name}').exists():
            with open(f'folder/{name}') as file:
                result = file.readlines()
            return result
        else:
            # code
            pass

