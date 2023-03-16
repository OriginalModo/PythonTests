# True False

falsy = [None, False, 0, 0.0, '', set(), tuple(), dict(), list(), range(0), ]

def check(x) -> bool:
    print(f"{x}>0 is {bool(x > 0)}")
    return x > 0



if check(-1) or check(-5) or check(-2) or check(-3):
    print('YES')

def is_even(x) -> bool:
    return x % 2 == 0


print(is_even(1))