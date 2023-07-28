import math


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def count_bonus_numbers(n):
    count = n

    for i in range(2, 11):
        if is_prime(i):
            count -= n // i

    for i in range(2, 11):
        for j in range(i + 1, 11):
            if is_prime(i) and is_prime(j):
                count += n // (i * j)

    for i in range(2, 11):
        for j in range(i + 1, 11):
            for k in range(j + 1, 11):
                if is_prime(i) and is_prime(j) and is_prime(k):
                    count -= n // (i * j * k)

    return count


# Read the input
n = int(input())

# Calculate the number of bonus numbers
result = count_bonus_numbers(n)

# Print the result
print(result)
