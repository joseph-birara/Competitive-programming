t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    need = list(map(int, input().split()))
    inc = list(map(int, input().split()))
    temp = []
    for i in range(n):
        temp.append([need[i],inc[i]])
    temp.sort()
    for b in range(n):
        if k >= temp[b][0]:
            k += temp[b][1]
        else:
            break
    print(k)