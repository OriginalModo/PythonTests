from functools import wraps


# def typed_int(function):
#     @wraps(function)
#     def wrapper(*args):
#
#         for i in args:
#             if not isinstance(i, int):
#                 raise ValueError('Тип должен быть целым числом(int)')
#
#         return function(*args)
#
#     # wrapper.__name__ = function.__name__
#     # wrapper.__doc__ = function.__doc__
#     return wrapper
#
# def typed_str(function):
#     @wraps(function)
#     def wrapper(*args):
#
#         for i in args:
#             if not isinstance(i, str):
#                 raise ValueError('Тип должен быть строкой(str)')
#
#         return function(*args)
#
#     # wrapper.__name__ = function.__name__
#     # wrapper.__doc__ = function.__doc__
#     return wrapper

def typed(type_):
    def real_decorator(function):
        @wraps(function)
        def wrapper(*args):

            for i in args:
                if not isinstance(i, type_):
                    raise ValueError(f'Тип должен быть {type_}')

            return function(*args)

        # wrapper.__name__ = function.__name__
        # wrapper.__doc__ = function.__doc__
        return wrapper
    return real_decorator


@typed(int)
def calculate(a, b, c):
    # Logic
    return a + b + c

@typed(str)
def convert(a, b):
    return a + b


if __name__ == '__main__':
    # calculate = typed_int(calculate)
    # print(calculate.__name__)
    # calculate = typed(int)(calculate)

    print(calculate(1, 2, 3))
    print(convert('a', 'b'))
