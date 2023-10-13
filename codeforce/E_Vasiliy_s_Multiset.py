A = set([0])
q = int(input())
result = []

# Process each query
for _ in range(q):
    query = input().split()
    op, x = query[0], int(query[1])

    if op == '+':
        A.add(x)
    elif op == '-':
        A.remove(x)
    elif op == '?':
        max_xor = 0
        for num in A:
            max_xor = max(max_xor, num ^ x)
        result.append(max_xor)


for xor in result:
    print(xor)
