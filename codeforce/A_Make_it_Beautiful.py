def is_beautiful_array(arr):
    n = len(arr)
    for i in range(2, n):
        if arr[i] == sum(arr[:i]):
            return False
    return True


def reorder_array(t, test_cases):
    for _ in range(t):
        n = test_cases[_][0]
        arr = test_cases[_][1]

        if is_beautiful_array(arr):
            print("YES")
            print(*arr)
            continue

        for i in range(1, n):
            if arr[i] == sum(arr[:i]):
                arr[i], arr[i-1] = arr[i-1], arr[i]
                break

        if is_beautiful_array(arr):
            print("YES")
            print(*arr)
        else:
            print("NO")


# Read the number of test cases
t = int(input())

test_cases = []
# Read the test cases
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    test_cases.append((n, arr))

# Solve the problem
reorder_array(t, test_cases)
