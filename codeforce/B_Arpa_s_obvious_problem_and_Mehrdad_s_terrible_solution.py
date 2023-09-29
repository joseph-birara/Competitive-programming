def read_integers(): return map(int, input().split())


test_cases, xor_value = read_integers()
element_counts = {}
valid_pairs_count = 0

for element in read_integers():
    xor_target = xor_value ^ element
    valid_pairs_count += element_counts.get(xor_target, 0)
    element_counts[element] = element_counts.get(element, 0) + 1

print(valid_pairs_count)
