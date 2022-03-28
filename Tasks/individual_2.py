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

    def display(self):
        pass

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
            return Integer(int(self.first + other.first))

    def sub(self, other):
        if isinstance(other, Integer):
            return Integer(int(self.first - other.first))

    def mul(self, other):
        if isinstance(other, Integer):
            return Integer(int(self.first * other.first))

    def div(self, other):
        if isinstance(other, Integer):
            return Integer(int(self.first / other.first))

    def display(self):
        print(self.first)


class Real(Number):
    def add(self, other):
        if isinstance(other, Real):
            return Real((float(self.first + other.first)))

    def sub(self, other):
        if isinstance(other, Real):
            return Real((float(self.first - other.first)))

    def mul(self, other):
        if isinstance(other, Real):
            return Real((float(self.first * other.first)))

    def div(self, other):
        if isinstance(other, Real):
            return Real((float(self.first / other.first)))

    def display(self):
        print(self.first)


def main():
    b1 = Integer(10)
    b2 = Integer(2)
    b1.add(b2).display()
    b1.sub(b2).display()
    b1.mul(b2).display()
    b1.div(b2).display()
    p1 = Real(13.44)
    p2 = Real(2.3)
    p1.add(p2).display()
    p1.sub(p2).display()
    p1.mul(p2).display()
    p1.div(p2).display()


if __name__ == "__main__":
    main()
