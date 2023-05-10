def isPossible(start, target):
    res = [target]

    while target > start:
        if target % 2 == 0:
            target //= 2
            res.append(target)
        elif target % 10 == 1:
            target //= 10
            res.append(target)
        else:
            return "NO", []
    if target == start:
        return "YES", res
    else:
        return "NO", []


start, target = map(int, input().split())
answer = isPossible(start, target)

if answer[0] == "YES":
    print("YES")
    print(len(answer[1]))
    print(*answer[1][::-1])

else:
    print("NO")
