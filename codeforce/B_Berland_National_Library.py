recods = int(input())
seen = set()
room = 0
for i in range(recods):
    event = list(input().split())

    # print(event[-1])
    if event[0] == '+':
        seen.add(int(event[-1]))
        if len(seen) > room:
            room += 1
    else:
        if int(event[-1]) in seen:
            seen.remove(int(event[-1]))
        else:
            room += 1


print(room)
