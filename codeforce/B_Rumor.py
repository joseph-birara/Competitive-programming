from collections import defaultdict, deque

n, m = map(int, input().split())
golds = list(map(int, input().split()))

d = defaultdict(list)

for _ in range(m):
    source, dest = map(int, input().split())
    d[source].append(dest)
    d[dest].append(source)

visited = set()
total_gold = 0

# Start BFS from each unvisited character
for i in range(1, n+1):
    if i not in visited:
        # Initialize the queue and visited set for BFS
        q = deque([i])
        visited.add(i)
        min_gold = golds[i-1]

        # BFS to spread the rumor to all connected characters
        while q:
            curr = q.popleft()
            for neighbor in d[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
                    # Update the minimum gold required to spread the rumor to the neighbor
                    min_gold = min(min_gold, golds[neighbor-1])

        # Add the minimum gold required to spread the rumor to all connected characters
        total_gold += min_gold

print(total_gold)
