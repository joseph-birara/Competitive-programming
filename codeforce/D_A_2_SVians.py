len_team = int(input())
members = list(input().split())
bad = list(input().split())
res = 0
for index in range(len_team):
    n = len(members[index])
    insta = True

    if members[index] in bad:
        continue
    else:
        for i in range(n-1):
            for j in range(i+1, n):
                if members[index].count(members[index][i]) != members[index].count(members[index][j]):
                    insta = False
                    break
            if not insta:
                break
    if insta:
        res += 1
