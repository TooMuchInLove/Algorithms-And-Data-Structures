#!/usr/bin/env python
# -*- coding: utf-8 -*-


def bubble_sort(_array):
    count = 0 # Кол-во итераций для сортировки

    array = _array # Массив значений
    if array == []: # Если массив пуст
        return None, count

    low = 0 # Начальный индекс массива
    high = len(array) # Конечный индекс массива

    for i in range(low, high):
        for j in range(low, high):
            if array[i] < array[j]: # Перестановка элементов
                array[i], array[j] = array[j], array[i]
            count += 1

    return array, count
