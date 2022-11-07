# 17). Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях. Позиции (случайные) хранятся в файле file.txt (создаётся во время выполнения кода и зависит от количества элементов в списке) в одной строке одно число.
# Пример:
# Файл:
# 4
# 5
# 2
# N = 3 => [-3, -2, -1, 0, 1, 2, 3]
# Результат: 1*2*(-1) = -2

from random import randint
import unittest

path = 'file.txt'

with open(path, 'w') as data:
    data.write('4\n')
    data.write('5\n')
    data.write('2\n')

def get_lst(n):
    lst = []
    for i in range(-n, n + 1):
        lst.append(i)
    return lst

def get_data_from_file(path):
    data = open(path, 'r')
    dlst = [int(line.strip()) for line in data]
    data.close()
    return dlst

def get_mult(numbers, datalst):
    mult = 1
    for i in datalst:
        mult *= numbers[i]
    return mult

n = 3
datalst = get_data_from_file(path)
lst = get_lst(n)

# print(lst)
# print(datalst)
# print(get_mult(lst, datalst))

class TestСomposition(unittest.TestCase):
