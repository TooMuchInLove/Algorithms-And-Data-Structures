#!/usr/bin/env python
# -*- coding: utf-8 -*-


def bubble_sort(_array):
    count = 0 # Кол-во итераций для сортировки

    array = _array # Массив значений
    if array == []: # Если массив пуст
        return None, count
    length = len(array) # Кол-во элементов в массиве

    for i in range(length):
        for j in range(length):
            if array[i] < array[j]: # Перестановка элементов
                array[i], array[j] = array[j], array[i]
            count += 1

    return array, count
