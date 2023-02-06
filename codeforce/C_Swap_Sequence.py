def sort_array(n, arr):
    swaps = []
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swaps.append((i, j))
    return len(swaps), swaps

n = int(input().strip())
arr = list(map(int, input().strip().split()))
k, swaps = sort_array(n, arr)
print(k)
for i, j in swaps:
    print(i, j)