def dfs(node, graph, visited):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited)


def main():
    n, m = map(int, input().split())
    languages = [list(map(int, input().split()[1:])) for _ in range(n)]

    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if any(lang in languages[i] for lang in languages[j]):
                graph[i].append(j)
                graph[j].append(i)

    visited = [False] * n
    components = 0

    for i in range(n):
        if not visited[i]:
            dfs(i, graph, visited)
            components += 1

    total_cost = components - 1
    print(total_cost)


main()
