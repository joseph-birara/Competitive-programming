
num_tiles = int(input())


tile_values = list(map(int, input().split()))


count_ones = tile_values.count(1)
count_twos = tile_values.count(2)


if count_ones == 0 or count_twos == 0:

    print(*tile_values)
else:
    permutation = [2, 1] + [2] * (count_twos - 1) + [1] * (count_ones - 1)
    print(*permutation)
