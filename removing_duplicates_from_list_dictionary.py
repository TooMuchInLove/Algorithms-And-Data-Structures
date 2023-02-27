#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Tuple, List, Dict

# --------------------------------------------------- #
# ----------------- Аннотация типов ----------------- #
# --------------------------------------------------- #
# Кол-во операций
COUNTSOperations = int
# Текущий индекс
CURRENTIndex = int
# Списко словарей
LISTDictionary = List[Dict[str, str]]
# Возвращаемый кортеж значение :param: List, count
RETURNTuple = Tuple[LISTDictionary, COUNTSOperations]


# удаление дубликатов из списка словарей
def removing_duplicates_from_list_dictionary(
        _count: COUNTSOperations,
        _index: CURRENTIndex,
        _list: LISTDictionary) -> RETURNTuple:
    # Кол-во операций, затраченных на удаление дубликатов
    count = _count
    
    # Список значений : Если список пуст, то завершаем работу
    listing = _list
    # Если список пуст, то завершаем работу
    if listing == []: return listing, count
    # Кол-во элементов в списке
    count_items = len(listing)
    
    # Текущий ключевой индекс
    key_index = _index
    # Если текущий индекс превышает(равен) кол-ву элементов в списке, то завершаем работу
    if key_index >= count_items: return (listing, count)
    # Текущее искомое значение
    value = listing[key_index]
    
    # Проходим по списку и сравниваем значения
    while count_items > 0:
        # Уменьшаем индекс позиции в списке
        count_items -= 1
        # Если значения совпадают:
        if listing[count_items] == value:
            # И если текущий индекс НЕравен начальному, то удаляем дубликат
            if count_items != key_index:
                listing.pop(count_items)
            # И если текущий индекс равен начальному, то завершаем поиск
            else: break
        # Кол-во итераций (итог)
        count += 1
    
    # Рекурсивный способ поиска и удаления дубликатов
    return removing_duplicates_from_list_dictionary(count, key_index+1, listing)
