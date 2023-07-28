q = int(input())

for _ in range(q):
    n, t = map(int, input().split())
    videos = list(map(int, input().split()))
    values = list(map(int, input().split()))
    curr_value = float('-inf')
    curr_index = -1

    for i, b in enumerate(values):
        if b > curr_value:
            if i + videos[i] <= t:
                curr_value = b
                curr_index = i + 1
    print(curr_index)
