#!/usr/bin/sudo python
# -*- coding: utf-8 -*-


# Очередь FIFO (first in, first out)
class FiFo:
    __HEAD = 0 # Указатель на "голову" очереди
    __TAIL = 0 # Указатель на "хвост" очереди
    __theStore = [] # Хранилище данных
    
    def set_size(self, _size: int):
        self.__SIZE = _size # Установить размер очереди
    
    def push(self, _value: str):
        # Добавление в очередь
        self.__theStore = [_value] + self.__theStore[self.__TAIL:]#self.__SIZE-1]
        print(self.__theStore)

    def pop(self):
        # Удаление из очереди
        self.__HEAD = len(self.__theStore)-1
        if self.__theStore != []:
            self.__theStore.pop(self.__HEAD)
        print(self.__theStore)
