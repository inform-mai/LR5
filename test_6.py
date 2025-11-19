# Сравнение количества простых чисел 1 и другого списка
from random import *


def count_prime_numbers(my_list):
    cnt_prime = 0
    for i in my_list:
        cnt_del = 0
        for j in range(2, i // 2 + 1):
            if abs(i) % j == 0:
                cnt_del += 1
        if cnt_del == 0:
            cnt_prime += 1
    return cnt_prime


def test_compare_lists():
    list_1 = [randint(-10 ** 6, 10 ** 6) for _ in range(20)]
    list_2 = [randint(-10 ** 6, 10 ** 6) for _ in range(20)]
    assert count_prime_numbers(list_1) > count_prime_numbers(list_2)
