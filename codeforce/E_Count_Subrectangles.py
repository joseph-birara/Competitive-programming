def count_ones(segments, count_array):
    i = 0
    n = len(segments)

    while i < n:
        j = i
        while j < n and segments[j] == 1:
            j += 1

        len_ones = (j - i)
        count = 1
        while len_ones > 0:
            count_array[len_ones] += count
            len_ones -= 1
            count += 1

        i = j + 1


n, m, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_ones_count = [0] * (n + 1)
b_ones_count = [0] * (m + 1)

count_ones(a, a_ones_count)
count_ones(b, b_ones_count)

result_count = 0
for i in range(1, n + 1):
    subrectangle_width = i
    subrectangle_height = k // i
    remaining_cells = k % i

    if subrectangle_height <= m and remaining_cells == 0:
        result_count += (a_ones_count[i] * b_ones_count[subrectangle_height])

print(result_count)
