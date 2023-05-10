
from collections import defaultdict


def possibleBipartition(graph):

    color = defaultdict(int)

    def dfs(node, col):
        color[node] = col
        for adjacent in graph[node]:
            if adjacent not in color:
                if not dfs(adjacent, 3 - col):
                    return False
            else:
                if color[adjacent] == color[node]:
                    return False
        return True

    for node in graph:
        if node not in color:
            if not dfs(node, 1):
                return False
    return True


while True:
    n = int(input())

    if n == 0:
        break
    edges = int(input())
    graph = defaultdict(list)

    for i in range(edges):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    result = possibleBipartition(graph)

    if result:
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")
