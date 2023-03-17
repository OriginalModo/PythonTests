from typing import Any, Optional, Union

# Primer 1

# def to_str(integers: list[int]) -> list[str]:
#     return [str(elem) for elem in integers]

# Primer 2
# def to_str(flags: Optional[int]=None) -> list[str]:
#     return [str(elem) for elem in integers]


# Primer 3

# if __name__ == '__main__':
#     text = 'text'
#     text = text.removesuffix('xt')
#     text = text.removeprefix('xt')
#     text = text.rstrip('At')
#     print(text)


if __name__ == '__main__':
    first = {1:1, 2:2}
    second = {3:3, 4:4}
    third = {5:5, 4:100}
    first.update(second)
    # first = first | second
    # first |= second
    # print(first)

    print({**first, **second})
    print(first | second | third)
