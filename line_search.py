# -*- coding: utf-8 -*-

# Аннотация типов
from typing import List, Tuple

# Массив чисел
IntArray = List[int]
# Кортеж значений индекса и количества операций
IndexAndCount = Tuple[int, int]


def line_search(_array: IntArray, _value: int) -> IndexAndCount:
    count = 0 # Кол-во итераций для поиска
    not_found = -1 # Значение по умолчанию

    array = _array # Массив значений
    value = _value # Искомое значение
    if array is []: # Если массив пуст
        return not_found, count
    if type(value) is not int: # Если значение НЕ является числом
        return not_found, count

    low = 0 # Начальный индекс массива
    high = len(array) # Конечный индекс массива
    for i in range(low, high): # Выполняем поиск по массиву
        count += 1
        if value == array[i]:
            return i, count
    # Если значение не найдено
    count = 0
    return not_found, count
