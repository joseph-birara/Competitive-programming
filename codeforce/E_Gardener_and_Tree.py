from collections import defaultdict, deque


t = int(input())
for _ in range(t):
    input()
    n, k = map(int, input().split())

    graph = defaultdict(list)
    indegree = defaultdict(int)

    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        indegree[u] += 1
        indegree[v] += 1

    queue = deque()

    for node in graph:
        if indegree[node] == 1:
            queue.append(node)

    steps = 0
    count = 0
    while queue:

        if steps == k:
            break

        size = len(queue)
        count += size
        for _ in range(size):
            cur = queue.popleft()
            indegree[cur] -= 1

            for neigh in graph[cur]:
                indegree[neigh] -= 1
                if indegree[neigh] == 1:
                    queue.append(neigh)

        steps += 1

    print(len(graph) - count)
