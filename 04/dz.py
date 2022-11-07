# 16. Задать список из n чисел последовательности (1+1/n)^n
# и вывести на экран их сумму

# n = int(input('Введите число'))
# result = [round((1 + 1 / i) ** i, 3) for i in range(1, n + 1)]
# print (result)
# print (round(sum(result), 3))

# Второе решение

import unittest

while True:
    num = input('Введите целое положительное число:  ')
    try:
        num = int(num)
        if num > 0:
            break
        else: print('Число отрицательное')
    except ValueError:
        print('Число должно быть положительным')

def get_lst(num):
    lst = []
    for i in range(1, num + 1):
        elem = round(((1 + 1/i)**i), 2)
        lst.append(elem)
    return lst

def get_sum(lst):
    sum_lst = sum(lst)
    return sum_lst

lst = get_lst(num)
print(lst)
print (get_sum(lst))

class Tsequence(unittest.TestCase):

    def test_get_lst(self):
        self.assertEqual(get_lst(3),
                         ([2.0, 2.25, 2.37]))

    def test_get_sum(self):
        self.assertEqual(get_sum([2.0, 2.25, 2.37]),
                         (6.62))
