#!/usr/bin/sudo python
# -*- coding: utf-8 -*-


# Стэк LIFO (last in, first out)
class LiFo:
    __TAIL = 0 # Указатель на "хвост" очереди
    __theStore = [] # Хранилище данных

    def set_size(self, _size: int):
        self.__SIZE = _size # Установить размер очереди

    def push(self, _value: str):
        # Добавление в очередь
        self.__theStore.append(_value)
        print(self.__theStore)

    def pop(self):
        # Удаление из очереди
        if self.__theStore != []:
            self.__theStore.pop(self.__TAIL)
        print(self.__theStore)
