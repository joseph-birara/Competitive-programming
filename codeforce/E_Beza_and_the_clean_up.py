n, m, s, A, B = map(int, input().split())
ai = list(map(int, input().split()))
bi = list(map(int, input().split()))

for i in range(n):
    ai[i] = [ai[i]/A, A, ai[i]]
for i in range(m):
    bi[i] = [bi[i]/B, B, bi[i]]

ai.sort()
bi.sort()

i = j = 0
curr_weight = 0
curr_cost = 0
while (i < n or j < m) and s > 0:
    if i < n and j < m:
        if ai[i][0] < bi[j][0]:
            if s >= ai[i][1]:
                curr_cost += ai[i][2]
                s -= ai[i][1]
                i += 1
            elif s >= bi[j][1]:
                curr_cost += bi[j][2]
                s -= bi[j][1]
                j += 1
        else:
            if s >= bi[j][1]:
                curr_cost += bi[j][2]
                s -= bi[j][1]
                j += 1
            elif s >= ai[i][1]:
                curr_cost += ai[i][2]
                s -= ai[i][1]
                i += 1
    elif i < n:
        if s >= ai[i][1]:
            curr_cost += ai[i][2]
            s -= ai[i][1]
            i += 1
    elif j < m:
        if s >= bi[j][1]:
            curr_cost += bi[j][2]
            s -= bi[j][1]
            j += 1
    if s == 0:
        break


print(curr_cost)
