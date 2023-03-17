
def calculator(expression):
    allowed = '+-/*'
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'Хотя бы 1 знак {allowed}')
    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)
                return {
                    '+': lambda a,b: a+b,
                    '-': lambda a,b: a-b,
                    '*': lambda a,b: a*b,
                    '/': lambda a,b: a/b,
                }[sign](left, right)
            except (ValueError, TypeError):
                raise ValueError(f'Ошибка: 2 целых числа')

def plus(a: int, b: int) -> int:
    """Function PLUS (+)"""
    return a + b

if __name__ == '__main__':
    print(plus(10, 10))


