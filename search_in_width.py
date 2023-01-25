#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Алгоритм поиска в ширину на примере графа с использованием очереди (fifo)
def search_in_width(_start, _end, _graph):

    start = _start # Начало пути
    end = _end # Конец пути
    graph = _graph # Граф путей

    fifo = [] # Очередь для вершин графа
    fifo.append(start)

    # if start == end:
    #     return fifo

    stack = fifo[0]

    count = 0
    while fifo:
    # while count < 5:
        current = fifo[0]
        print(fifo)
        #if fifo[0] != start:
        fifo = fifo[1:]
        print(fifo)
        if graph[current] == []:
            graph[current] = []
        if graph[current] == [end]:
            print(True)
            return True
        else:
            fifo = fifo + graph[current]

    print(False)
    return False




graph = {
    'A': ['B', 'C'],
    'B': ['F'],
    'C': ['D', 'E'],
    'D': ['F'],
    'E': ['F'],
    'F': ['G'],
    'G': [],
    #
    # 'A': ['B', 'C'],
    # 'B': ['A', 'F'],
    # 'C': ['A', 'D', 'E'],
    # 'D': ['C', 'F'],
    # 'E': ['C', 'F'],
    # 'F': ['B', 'D', 'E', 'G'],
    # 'G': ['F'],
}

search_in_width('A', 'G', graph)
