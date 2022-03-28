#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать абстрактный базовый класс Number с абстрактными
методами — арифметическими операциями. Создать производные
классы Integer (целое) и Real (действительное).
"""

from abc import ABC, abstractmethod


class Number(ABC):

    def __init__(self, first):
        self.first = first

    @abstractmethod
    def add(self, other):
        pass

    @abstractmethod
    def sub(self, other):
        pass

    @abstractmethod
    def mul(self, other):
        pass

    @abstractmethod
    def div(self, other):
        pass


class Integer(Number):
    def add(self, other):
        if isinstance(other, Integer):
            print(f'Сложение целых чисел: {int(self.first + other.first)}')

    def sub(self, other):
        if isinstance(other, Integer):
            print(f'Вычитание целых чисел: {int(self.first - other.first)}')

    def mul(self, other):
        if isinstance(other, Integer):
            print(f'Умножение целых чисел: {int(self.first * other.first)}')

    def div(self, other):
        if isinstance(other, Integer):
            print(f'Деление целых чисел: {int(self.first / other.first)}')


class Real(Number):
    def add(self, other):
        if isinstance(other, Real):
            print(f'Сложение действительных чисел: {(float(self.first + other.first))}')

    def sub(self, other):
        if isinstance(other, Real):
            print(f'Вычитание действительных чисел: {(self.first - other.first)}')

    def mul(self, other):
        if isinstance(other, Real):
            print(f'Умножение действительных чисел: {(self.first * other.first)}')

    def div(self, other):
        if isinstance(other, Real):
            print(f'Деление действительных чисел: {(self.first / other.first)}')


def main():
    b1 = Integer(10)
    b2 = Integer(2)
    b1.add(b2)
    b1.sub(b2)
    b1.mul(b2)
    b1.div(b2)
    p1 = Real(13.44)
    p2 = Real(2.3)
    p1.add(p2)
    p1.sub(p2)
    p1.mul(p2)
    p1.div(p2)


if __name__ == "__main__":
    main()
