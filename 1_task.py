# На языке Python написать алгоритм (функцию) определения четности целого числа, который будет
# аналогичен нижеприведенному по функциональности, но отличен по своей сути.
# Объяснить плюсы и минусы обеих реализаций.
#
# Пример:
#
# def isEven(value):
#
#       return value % 2 == 0
"""Изначальный вариант
Минусы
1. Деление более долгий процесс чем усножение
2. возможны проблемы с плавающей точкой
Плюсы
1. Прост и понятен

Мой вариант
Плюс
1. Не зависит от плавающей точки
Минусы
2. из-за преобразовний будет дольше"""
def isEven2(value):
      """в двоичном коде в конце четного числа всегда 0"""
      return f'{value * 0.5:.1f}'[-1]=='0'
      return '{:b}'.format(value)[-1]=='0'

print(isEven2(6))

