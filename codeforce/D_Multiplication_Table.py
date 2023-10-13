n, m, k = map(int, input().split())


def find_kth_largest(k):
    low, high = 1, n * m

    while low < high:
        mid = (low + high) // 2
        count = 0
        for i in range(1, n + 1):
            count += min(mid // i, m)

        if count < k:
            low = mid + 1
        else:
            high = mid

    return low


print(find_kth_largest(k))
