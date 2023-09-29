n = int(input())
arr = []

for i in range(n):
    arr.append(input())
for i in range(n):
    target = arr[i]
    max_len = 0
    for j in range(n):
        if i == j:
            continue
        k = 0
        while k < len(target) and k < len(arr[j]) and target[k] == arr[j][k]:
            k += 1
        max_len = max(max_len, k)

    print(max_len)
