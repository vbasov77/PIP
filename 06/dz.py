# 22. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


import unittest

count = 5
lst = [2, 7, 8, 6, 1]

def odd_num(lst):
    numbers = []
    for j in range(1, len(lst), 2):
        numbers.append(lst[j])

    return numbers


odd = odd_num(lst)
odd_str = ', '.join(str(x) for x in odd)
sum_lst = sum(odd)

print(f'На нечётных позициях: {odd_str}')
print(f'Сумма {sum_lst}')

class TestTsequence(unittest.TestCase):

    def test_get_lst(self):
        self.assertEqual(odd_num([2, 7, 8, 6, 1]),
                         ([7, 6]))