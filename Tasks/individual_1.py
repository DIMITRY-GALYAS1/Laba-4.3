#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать класс Pair (пара чисел); определить методы изменения полей
и сравнения пар: пара p1 больше пары р2, если (first.p1 > first.р2)
или (first.p1 = first.р2) и (second.p1 > second.р2). Определить
класс-наследник Fraction с полями: целая часть числа и дробная часть
числа. Определить полный набор методов сравнения.
"""


class Pair:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def comparison(self, other):
        if isinstance(other, Pair):
            if self.first > other.first:
                return True
            elif self.first == other.first and self.second > other.second:
                return True
            else:
                return False


class Fraction(Pair):
    pass


if __name__ == '__main__':
    num1 = Pair(45, 68)
    num2 = Pair(44, 99)
    print(num1.comparison(num2))
    fraction1 = Fraction(6, 78)
    fraction2 = Fraction(4, 58)
    print(fraction1.comparison(fraction2))
