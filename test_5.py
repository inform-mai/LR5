# Проверка, является ли число палиндромом
from random import *

def palindrom(n):
    pal_n = int(str(n)[::-1])
    return pal_n

def test_palindrom_1():
    number = randint(10, 10 ** 6)
    assert number == palindrom(number)

