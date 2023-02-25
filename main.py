#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------
# Created By  : Fyodorov Dmitry
# Created Date: 16/01/2023
# version = '1.0'
# ----------------------------------------
#
from time import time
# Алгоритмы
from line_search import line_search
from binary_search import binary_search
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from quick_sort import quick_sort
from removing_duplicates_from_list_dictionary import removing_duplicates_from_list_dictionary
from fifo import FiFo
from lifo import LiFo
from parse_excel import excel


if __name__ == '__main__':
    BEGIN = time()

    array, value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 11
    print('Массив: %s, значение: %d' % (array, value))

    index, count = line_search(array, value)
    print('Линейный поиск. Кол-во итераций: %d' % (count))
    print('Найден индекс: %s' % (index))

    index, count = binary_search(array, value)
    print('Бинарный поиск. Кол-во итераций: %d' % (count))
    print('Найден индекс: %s' % (index))

    array = [-3, 65, 77, -5, 6, -2, 33, -10, 47, 32, 51, -6, -5, 23, 91]
    print('Массив    до сортировки: %s' % (array))

    array, count = bubble_sort(array)
    print('Сортировка Пузырьком. Кол-во итераций: %d' % (count))
    print('Массив после сортировки: %s' % (array))

    array, count = selection_sort(array)
    print('Выборочная сортировка. Кол-во итераций: %d' % (count))
    print('Массив после сортировки: %s' % (array))

    array, count = quick_sort(array)
    print('Быстрая сортировка. Кол-во итераций: %d' % (count))
    print('Массив после сортировки: %s' % (array))

    listing = [
        {"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {},
        {"key1": "value1"}, {"key1": "value1"},
        {"key2": "value2"},
    ]
    print('Начальный список: %s' % (listing))
    listing, count = removing_duplicates_from_list_dictionary(0, 0, listing)
    print('Конечный  список: %s\nКоличество операций: %s' % (listing, count))

    print('Очередь FIFO (first in, first out)')
    fifo = FiFo()
    for value in ('A', 'B', 'C', 'D', 'E'):
        fifo.push(value)
    fifo.pop()

    print('Стэк LIFO (last in, first out)')
    lifo = LiFo()
    for value in ('A', 'B', 'C', 'D', 'E'):
        lifo.push(value)
    lifo.pop()

    excel("data.xlsx")

    print('Время выполнения: %s' % (time() - BEGIN))
