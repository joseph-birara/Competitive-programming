s1 = input()
s2 = input()
first_diff = len(s1) - 1

for i in range(len(s2)):
    if s1[i] != s2[i]:
        first_diff = i
        break

for i in range(first_diff + 1, len(s1)):
    if s1[i] != s2[i - 1]:
        print(0)
        exit()

i = first_diff

while i > 0 and s1[first_diff] == s1[i - 1]:
    i -= 1

length_of_difference = first_diff - i + 1
print(length_of_difference)
print(' '.join(map(str, range(i + 1, first_diff + 2))))
