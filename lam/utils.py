from functools import reduce
from typing import Callable, TypeVar


def flatten(s: list) -> list:
    if s == []:
        return s
    if isinstance(s[0], list):
        return flatten(s[0]) + flatten(s[1:])
    return s[:1] + flatten(s[1:])


T = TypeVar('T')
def foldr(func: Callable[[T, T], T], acc: T, xs: list) -> T:
    return reduce(lambda x, y: func(y, x), xs[::-1], acc)
