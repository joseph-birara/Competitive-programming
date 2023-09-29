
n, m = map(int, input().split())
chairs = []
for i in range(n):
    xi, yi = map(int, input().split())
    chairs.append((xi, yi))


results = []


for i in range(m):
    sxi, syi, exi, eyi = map(int, input().split())
    count = 0

    for xi, yi in chairs:
        if sxi <= xi <= exi and syi <= yi <= eyi:
            count += 1

    results.append(count)


for count in results:
    print(count)
