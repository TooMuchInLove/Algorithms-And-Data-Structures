#!/usr/bin/env python
# -*- coding: utf-8 -*-


def line_search(_array, _value):
    count = 0 # Кол-во итераций для поиска

    array = _array # Массив значений
    value = _value # Искомое значение
    if array == []: # Если массив пуст
        return None, count

    low = 0 # Начальное значение массива
    high = len(array)-1 # Конечное значение массива
    if array[low] < value > array[high]: # Если значение не входит в массив
        return None, count

    for i in range(high):
        count += 1
        if value == array[i]:
            return i, count

    return None, count
