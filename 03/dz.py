# 15). Напишите программу, которая принимает на вход число N и выдает
# набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


import unittest

number = int(input('Введите число: '))

def product_numbers(x):
    lst = []
    m = 1
    for i in range(1, number + 1):
        m *= i
        lst.append(m)
    return lst

print(product_numbers(number), end=' ')

class TestSum(unittest.TestCase):
    def test_get_sum(self):
        self.assertEqual(product_numbers(4),
                         ([1, 2, 6, 24]))