#!/usr/bin/env python
# -*- coding: utf-8 -*-


count = 0 # Кол-во итераций для сортировки

def quick_sort(_array):
    global count

    array = _array # Массив значений
    length = len(array) # Кол-во элементов в массиве
    if array == [] or length == 1: # Если массив пуст
        return array, count
    array_left = [] # Массив с меньшими элементами
    array_right = [] # Массив с большими элементами

    mid = int(length/2)-1
    if length % 2 != 0:
        mid = int(length/2)
    value = array[mid]

    for i in range(length):
        if i == mid: continue
        if array[i] < value:
            array_left.append(array[i])
        else:
            array_right.append(array[i])
        count += 1

    return quick_sort(array_left)[0]+[array[mid]]+quick_sort(array_right)[0], count
