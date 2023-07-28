def dfs(node, graph, letters, letter_freq, visited, on_path, k):
    visited[node] = True
    letter_freq[letters[node-1]] += 1
    on_path[node] = True

    max_freq = letter_freq[letters[node-1]]
    possible_path = False

    if max_freq >= k:
        possible_path = True

    for neighbor in graph[node]:
        if on_path[neighbor]:
            return -2  # Cycle detected
        if not visited[neighbor]:
            res = dfs(neighbor, graph, letters,
                      letter_freq, visited, on_path, k)
            if res == -2:
                return -2
            max_freq = max(max_freq, res)

    letter_freq[letters[node-1]] -= 1
    on_path[node] = False

    return max_freq


def largest_path_value(n, m, letters, edges):
    graph = [[] for _ in range(n + 1)]
    for x, y in edges:
        graph[x].append(y)

    letter_freq = [0] * 26  # To store frequency of each letter
    visited = [False] * (n + 1)
    on_path = [False] * (n + 1)

    max_value = -1

    for i in range(1, n + 1):
        if not visited[i]:
            res = dfs(i, graph, letters, letter_freq, visited, on_path, k)
            if res == -2:
                return -1  # Cycle detected, value can be arbitrarily large
            max_value = max(max_value, res)

    return max_value


# Read input
n, m = map(int, input().split())
letters = list(input().strip())  # Convert the string to a list of characters
edges = [tuple(map(int, input().split())) for _ in range(m)]
# The initial value of k, as mentioned in the problem, you can change this as needed.
k = 0

result = largest_path_value(n, m, letters, edges)
print(result)
