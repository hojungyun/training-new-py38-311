from typing import Union


# Union keyword prior to Python 3.9
def fn1(num: Union[int, float]) -> Union[int, float]:
    return num + 10


# | operator in Python 3.9
def fn2(num: int | float) -> int | float:
    return num + 10
