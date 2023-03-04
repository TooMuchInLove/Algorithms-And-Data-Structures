# -*- coding: utf-8 -*-

# Аннотация типов
from typing import List, Tuple

# Массив чисел
IntArray = List[int]
# Кортеж значений индекса и количества операций
IndexAndCount = Tuple[int, int]


def binary_search(_array: IntArray, _value: int) -> IndexAndCount:
    count = 0 # Кол-во итераций для поиска
    not_found = -1 # Значение по умолчанию

    array = _array # Массив значений
    if array is []: # Если массив пуст
        return not_found, count
    value = _value # Искомое значение
    if type(value) is not int: # Если значение НЕ является числом
        return not_found, count

    low = 0 # Начальный индекс массива
    high = len(array)-1 # Конечный индекс массива
    while low <= high: # Выполняем поиск по массиву
        count += 1
        mid = int((low + high)/2)
        if value == array[mid]:
            return mid, count
        if value < array[mid]:
            high = mid - 1
        if value > array[mid]:
            low = mid + 1
    # Если значение не найдено
    count = 0
    return not_found, count
