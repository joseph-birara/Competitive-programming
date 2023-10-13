testCase = int(input())

for _ in range(testCase):
    n = int(input())

    s = input()

    count = 1

    for index in range(n - 2):
        if s[index] != s[index + 2]:
            count += 1

    print(count)
