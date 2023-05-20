from collections import defaultdict, deque
num_users, num_groups = map(int, input().split())
graph = defaultdict(set)

for i in range(num_groups):
    group_members = list(map(int, input().split()))
    group_size = group_members[0]
    for j in range(1, group_size + 1):
        for k in range(j + 1, group_size+1):
            graph[group_members[j]].add(group_members[k])
            graph[group_members[k]].add(group_members[j])


res = [1] * num_users
for key in graph:
    visited = set()
    q = deque()
    visited.add(key)
    q.append(key)

    while q:
        node = q.popleft()
        for friend in graph[node]:
            if friend not in visited:
                visited.add(friend)
                q.append(friend)
    res[key-1] = (len(visited))

print(*res)
