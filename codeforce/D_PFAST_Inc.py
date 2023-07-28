from collections import defaultdict
import sys


input = sys.stdin.readline


def solve():
    n, m = map(int, input().split())

    idx = {}
    for i in range(n):
        name = input().strip()
        idx[name] = i

    adj = defaultdict(set)
    for _ in range(m):
        f1, f2 = map(lambda x: idx[x], input().strip().split())
        adj[f1].add(f2)
        adj[f2].add(f1)

    mx = 0
    for mask in range((1 << n) + 1):
        ok = True
        for i in range(n):
            for j in range(n):
                if (mask & (1 << i)) and (mask & (1 << j)) and j in adj[i]:
                    ok = False
                    break
            if not ok:
                break
        else:
            if bin(mask).count('1') > bin(mx).count('1'):
                mx = mask

    res = []
    for name, i in idx.items():
        if mx & (1 << i):
            res.append(name)

    res.sort()

    print(len(res))
    for x in res:
        print(x)


solve()
