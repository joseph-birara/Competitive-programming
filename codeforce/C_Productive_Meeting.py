from heapq import heappush, heappop

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    pairs = []
    heap = []
    for i in range(n):
        if a[i] == 0:
            continue
        heappush(heap, (-a[i], i+1))

    while len(heap) > 1:

        _, u = heappop(heap)
        _, v = heappop(heap)
        pairs.append((u, v))
        a[u-1] -= 1
        a[v-1] -= 1
        if a[u-1] > 0:
            heappush(heap, (-a[u-1], u))
        if a[v-1] > 0:
            heappush(heap, (-a[v-1], v))

    print(len(pairs))
    for u, v in pairs:
        print(u, v)
