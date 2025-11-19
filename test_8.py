# Проверка, есть ли у кубического уравнения положительные корни.
from random import *


def solve_equation(a, b, c, d):
    list_solves = []
    list_x = [x // 10.0 for x in range(1, 10 ** 6)]
    for x in list_x:
        if a * x ** 3 + b * x ** 2 + c * x + d == 0:
            list_solves.append(x)
        else:
            continue
    return list_solves


def test_solves():
    a = 1
    b = -3
    c = -13
    d = 150
    my_list = solve_equation(a, b, c, d)
    assert len(my_list) > 0
