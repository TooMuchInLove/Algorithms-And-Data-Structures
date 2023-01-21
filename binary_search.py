#!/usr/bin/env python
# -*- coding: utf-8 -*-


def binary_search(_array, _value):
    count = 0 # Кол-во итераций для поиска

    array = _array # Массив значений
    value = _value # Искомое значение
    if array == []: # Если массив пуст
        return None, count

    low = 0 # Начальный индекс массива
    high = len(array)-1 # Конечный индекс массива
    if array[low] < value > array[high]: # Если значение не входит в массив
        return None, count


    while low <= high:
        mid = int((low + high)/2)
        count += 1
        if value == array[mid]:
            return mid, count
        if value < array[mid]:
            high = mid - 1
        if value > array[mid]:
            low = mid + 1

    return None, count
