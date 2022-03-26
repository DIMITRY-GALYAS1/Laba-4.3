#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать абстрактный базовый класс Number с абстрактными
методами — арифметическими операциями. Создать производные
классы Integer (целое) и Real (действительное).
"""

from abc import ABC, abstractmethod


class Number(ABC):

    @abstractmethod
    def add(self, a, b):
        pass

    @abstractmethod
    def sub(self, a, b):
        pass

    @abstractmethod
    def mul(self, a, b):
        pass

    @abstractmethod
    def div(self, a, b):
        pass


class Integer(Number):
    def add(self, a, b):
        print(f'Сложение целых чисел: {int(a + b)}')

    def sub(self, a, b):
        print(f'Вычитание целых чисел: {int(a - b)}')

    def mul(self, a, b):
        print(f'Умножение целых чисел: {int(a * b)}')

    def div(self, a, b):
        print(f'Деление целых чисел: {int(a / b)}')


class Real(Number):
    def add(self, a, b):
        print(f'Сложение действительных чисел: {(float(a + b))}')

    def sub(self, a, b):
        print(f'Вычитание действительных чисел: {(float(a - b))}')

    def mul(self, a, b):
        print(f'Умножение действительных чисел: {(float(a * b))}')

    def div(self, a, b):
        print(f'Деление действительных чисел: {(float(a / b))}')


def main():
    b1 = Integer()
    b1.add(10, 2)
    b1.sub(10, 2)
    b1.mul(10, 2)
    b1.div(10, 2)
    p1 = Real()
    p1.add(13.44, 2.3)
    p1.sub(13.44, 2.3)
    p1.mul(13.44, 2.3)
    p1.div(13.44, 2.3)


if __name__ == "__main__":
    main()
