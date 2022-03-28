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

    def display(self):
        print(f'Большая пара чисел {self.first} {self.second}')

    def comparison(self, other):
        if isinstance(other, Pair):
            if self.first > other.first:
                return Pair(self.first, self.second)
            elif self.first == other.first and self.second > other.second:
                return Pair(self.first, self.second)
            elif self.first < other.first:
                return Pair(other.first, other.second)
            elif self.first == other.first and self.second < other.second:
                return Pair(other.first, other.second)
            elif self.first == other.first and self.second == other.second:
                return Fraction(self.first, self.second)


class Fraction(Pair):

    def comparison(self, other):
        if isinstance(other, Fraction):
            if self.first > other.first:
                return Fraction(self.first, self.second)
            elif self.first == other.first and self.second > other.second:
                return Fraction(self.first, self.second)
            elif self.first < other.first:
                return Fraction(other.first, other.second)
            elif self.first == other.first and self.second < other.second:
                return Fraction(other.first, other.second)
            elif self.first == other.first and self.second == other.second:
                return Fraction(self.first, self.second)


if __name__ == '__main__':
    num1 = Pair(44, 68)
    num2 = Pair(44, 99)
    num1.comparison(num2).display()
    fraction1 = Fraction(6, 78)
    fraction2 = Fraction(4, 58)
    fraction1.comparison(fraction2).display()
