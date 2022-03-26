#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный
номер объекта, и свойство, в котором хранится принадлежность команде. У солдат есть
метод "иду за героем", который в качестве аргумента принимает объект типа "герой". У
героев есть метод увеличения собственного уровня.
В основной ветке программы создается по одному герою для каждой команды. В цикле
генерируются объекты-солдаты. Их принадлежность команде определяется случайно.
Солдаты разных команд добавляются в разные списки.
Измеряется длина списков солдат противоборствующих команд и выводится на экран. У
героя, принадлежащего команде с более длинным списком, увеличивается уровень.
Отправьте одного из солдат первого героя следовать за ним. Выведите на экран
идентификационные номера этих двух юнитов.
"""

import random


class Soldiers:
    id = 1

    def __init__(self):
        self.id = Soldiers.id
        Soldiers.id += 1

    def go_hero(self, hero):
        print(f'солдат с id {self.id} следует за героем {hero.id}')

    def __str__(self):
        return f'{self.id}'


class Heroes(Soldiers):

    def __init__(self, team):
        Soldiers.__init__(self)
        self.team = team
        self.level = 1

    def level_up(self):
        self.level += 1
        print(f'герой с id {self.id} достиг {self.level} уровня')


def main():
    hero_1 = Heroes('black')
    hero_2 = Heroes('white')
    list_heroes = []
    list_heroes_2 = []
    for k in range(15):
        if random.choice(['black', 'white']) == 'black':
            list_heroes.append(Soldiers())
        else:
            list_heroes_2.append(Soldiers())

    len_heroes = len(list_heroes)
    len_heroes_2 = len(list_heroes_2)
    print(f'солдат у героя hero_1 - {len_heroes}')
    print(f'солдат у героя hero_2 - {len_heroes_2}')
    if len_heroes > len_heroes_2:
        hero_1.level_up()
    else:
        hero_2.level_up()

    random.choice(list_heroes).go_hero(hero_1)


if __name__ == "__main__":
    main()
