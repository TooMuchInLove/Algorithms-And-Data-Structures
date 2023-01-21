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
# from quick_sort import quick_sort
from random import randint


if __name__ == '__main__':
    BEGIN = time()
    # print([randint(0, 100) for _ in range(15)])
    # print([i for i in range(1, 16)])

    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    value = 1
    print('Массив: %s, значение: %d' % (array, value))

    index, count = line_search(array, value)
    print('Найден индекс: %s' % (index))
    print('Линейный поиск. Кол-во итераций: %d' % (count))

    index, count = binary_search(array, value)
    print('Найден индекс: %s' % (index))
    print('Бинарный поиск. Кол-во итераций: %d' % (count))

    print('Время выполнения: %s' % (time() - BEGIN))
