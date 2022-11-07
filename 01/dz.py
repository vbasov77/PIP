# Рассчитаем скорость авто пройденного за 45 мин. Расстояние 100 км V=S/t
# V=S/t

import unittest

s = 100
t = 45


def speed_detection(s, t):
    hour = t / 60  # Перевели минуты в часы
    v = s / hour
    return (round(v))

# print(speed_detection(s, t))


class TestSpeed(unittest.TestCase):
    def test_speed_detection(self):
        self.assertEqual(speed_detection(100, 45),
                         (133))
