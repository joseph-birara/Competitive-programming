

def is_perfect_number(n):
    return sum(map(int, str(n))) == 10


def perfect_integer(k):
    count = 0
    num = 19

    while count < k:
        if is_perfect_number(num):
            count += 1
        num += 9

    return num-9


k = int(input())
result = perfect_integer(k)
print(result)
