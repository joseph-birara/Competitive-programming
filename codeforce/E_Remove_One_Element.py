list_length = int(input())
numbers = list(map(int, input().split()))
lengths = [1] * list_length
max_lengths = [1] * list_length

for i in range(1, list_length):
    if numbers[i] > numbers[i - 1]:
        lengths[i] = lengths[i - 1] + 1
        max_lengths[i] = max_lengths[i - 1] + 1

    if i >= 2 and numbers[i] > numbers[i - 2]:
        max_lengths[i] = max(max_lengths[i], lengths[i - 2] + 1)

max_length = max(max_lengths)
print(max_length)
