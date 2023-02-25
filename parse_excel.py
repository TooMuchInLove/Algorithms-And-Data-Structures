#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Аннотации типов
from typing import List
# Определяем текущую директорию
from pathlib import Path
# Взаимодействие с excel-файлами
from openpyxl import open

# Документ excel
EXCELObject = open
# Название файла
FILEName = str
# Вложенный список со значениями
LISTData = List[list]
# Список длин строк
LISTLengths = List[int]
# Общая сумма всех займов
Amount = float
# Фильтр для даты
Year = int


def _get_excel_data(_file_name: FILEName) -> EXCELObject:
    try: # Выбираем активную страницу в документе excel
        excel = open(Path.cwd()/_file_name, read_only=True).active
        # Возвращаем набор данных из документа
        return excel
    except FileNotFoundError:
        print("Имя файла %s не найдено." % (Path.cwd()/_file_name))
        exit(1)


def _parse_excel_data(_excel: EXCELObject) -> LISTData:
    # Хранилище данных
    storage = []
    # Количество строк (и вложенных списков)
    count = 0
    # Проходим по строкам/колонкам
    for row in _excel:
        # Вложенный список
        storage.append([])
        # Пробегаем по строкам
        for item in row:
            storage[count].append(str(item.value))
        count += 1
    # Возвращаем данные
    return storage


def _filter_amount_and_year(_storage: LISTData, _year: Year) -> Amount:
    # Общая сумма
    amount = 0
    # Определяем сумму всех займов, зарег. не позднее N года
    for row in _storage:
        # Год регистрации
        if row[1][:4].isalpha():
            continue
        else:
            current_year = int(row[1][:4])
        if current_year < _year:
            amount += float(row[3])
    # Возвращаем общую сумму (фильтр по году регистрации)
    return amount


def _get_list_of_lengths(_storage: LISTData) -> LISTLengths:
    # Список длин строк
    list_of_lengths = [0 for _ in _storage[0]]
    # Вывод данных (определённых столбцов)
    for row in _storage:
        # Получаем столбцы для вывода
        for i in range(len(list_of_lengths)):
            # Длина текущего элемента (в символах)
            length = len(row[i])
            if length > list_of_lengths[i]:
                list_of_lengths[i] = length
    # Возвращаем список длин строк
    return list_of_lengths


def _out_columns_data(_storage: LISTData, *_cols):
    # Список длин строк
    list_of_lengths = _get_list_of_lengths(_storage)
    # Вывод данных (определённых столбцов)
    for row in _storage:
        underline = ""
        # Получаем столбцы для вывода
        for col in _cols:
            try:
                space = (list_of_lengths[col] - len(row[col])) * " "
                underline += "|" + (list_of_lengths[col]+2) * "-"
                print("| %s%s" % (row[col], space), end=" ")
            except IndexError:
                pass
        print("\n%s" % (underline))


def excel(_file_name: FILEName) -> None:
    # Получаем набор данных
    excel = _get_excel_data(_file_name)
    # Парсим полученные данные
    data = _parse_excel_data(excel)
    # Вывод данных из документа
    _out_columns_data(data, 0, 1, 2, 3, 4)
