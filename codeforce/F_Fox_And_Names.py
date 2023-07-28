from heapq import heappop, heappush
from string import ascii_lowercase
from sys import stdin


n = int(stdin.readline().rstrip())


arr = []


for _ in range(n):
    arr.append(stdin.readline().rstrip())


graph = {x: [] for x in ascii_lowercase}
in_degree = {x: 0 for x in ascii_lowercase}


for i in range(n - 1):

    s1, s2 = arr[i], arr[i + 1]

    for j in range(len(s1)):
        if j >= len(s2):
            print("Impossible")
            exit()

        if s1[j] != s2[j]:
            graph[s1[j]].append(s2[j])
            in_degree[s2[j]] += 1
            break


starting_nodes = list(filter(lambda x: in_degree[x] == 0, ascii_lowercase))


que = starting_nodes
order = []


while que:
    letter = heappop(que)
    order.append(letter)

    for nei in graph[letter]:
        in_degree[nei] -= 1
        if in_degree[nei] == 0:
            heappush(que, nei)


if len(order) != 26:
    print("Impossible")
else:
    print(*order, sep="")
