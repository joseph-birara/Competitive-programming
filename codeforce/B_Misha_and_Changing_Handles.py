num_pairs = int(input())

pair_dict = {}

for i in range(num_pairs):
    old_value, new_value = input().split()

    pair_dict[new_value] = pair_dict.get(old_value, old_value)

    pair_dict.pop(old_value, None)

print(len(pair_dict))

for new_value, old_value in pair_dict.items():
    print(old_value, new_value)
