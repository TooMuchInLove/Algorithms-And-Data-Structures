#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Алгоритм поиска в ширину на примере графа с использованием очереди (fifo)
def search_in_width(_start, _end, _graph):

    start = _start # Начало пути
    end = _end # Конец пути
    graph = _graph # Граф путей

    fifo = [] # Очередь для вершин графа
    fifo.append(start)

    if start == end:
        return fifo

    next_nodes = graph[start]

    print(next_nodes)

    search_in_width(start, end, graph)

    # stack = fifo[0]
    #
    # count = 0
    # # while fifo:
    # while count < 5:
    #
    #     # length = len(fifo)
    #     # if graph[fifo[0]] == 'G': return
    #     # fifo = graph[fifo[0]] + fifo[0:length]
    #     # print(fifo, length)
    #     count += 1
    #
    #     # value = stack
    #     # if value == end:
    #     #     break
    #
    #     print(fifo)
    #
    #     next_nodes = []
    #
    #     # print(value)
    #     for next_node in stack:
    #
    #         next_nodes = graph[next_node]
    #
    #         # print(next_node, next_nodes)
    #
    #         # index = fifo.index(next_node)
    #         # index = len(fifo) - 1
    #         # fifo = fifo[0:index] + next_nodes
    #
    #         # fifo.append(next_nodes)
    #
    #         # fifo.append(start)
    #         if next_node != start:
    #             fifo.append(next_node)
    #
    #
    #
    #
    #         # if next_node not in visited:
    #         #     fifo.append(next_node)
    #         #     visited[value] = True
    #         #     visited[next_node] = False
    #
    #     stack = next_nodes
    #     # print(next_nodes)
    #     print(fifo)
    #
    #     # print(visited)
    #     #return visited



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
