from random import *


def choice_sorting(a):
    for i in range(len(a)):
        mn_ind = i
        for j in range(i + 1, len(a)):
            if a[j] < a[mn_ind]:
                mn_ind = j
        a[i], a[mn_ind] = a[mn_ind], a[i]
    return a


def test_sorting_list():
    list_1 = [uniform(-10 ** 6, 10 ** 6) for _ in range(20)]
    list = list_1
    list.sort()
    assert list == choice_sorting(list_1)
