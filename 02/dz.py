#  Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# *Пример:*
# - 6782  -> 23
# - 0,56 -> 11

import unittest

number = input('Введите число ')

def get_sum(x):
    sum = 0
    for i in number:
        if i.isdigit():
            sum += int(i)
    return sum

print(get_sum(number))

class TestSum(unittest.TestCase):
    def test_get_sum(self):
        self.assertEqual(get_sum(6782),
                         (23))
