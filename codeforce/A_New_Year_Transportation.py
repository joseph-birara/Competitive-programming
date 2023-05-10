n, b = map(int, input().split())

start = 0

path = list(map(int, input().split()))
curr = 0
while curr < n-1:
    curr += path[curr]

    if curr < n:
        if curr == b-1:
            print("YES")
            exit()
print("NO")
