#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------
# Created By  : Fyodorov Dmitry
# Created Date: 16/01/2023
# version = '1.0'
# ----------------------------------------
#
from time import time

from line_search import line_search
from binary_search import binary_search
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from quick_sort import quick_sort


if __name__ == '__main__':
    BEGIN = time()

    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    value = 11
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

    print('Время выполнения: %s' % (time() - BEGIN))
