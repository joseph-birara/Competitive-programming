
def is_prime(num):
    if num < 2:
        return False
    if num % 2 == 0 and num != 2:
        return False
    if num % 3 == 0 and num != 3:
        return False
    if num != 5 and num % 5 == 0:
        return False
    for i in range(6, int((num**0.5)+1), 6):
        if num % i == 0:
            return False
    return True


k, n = map(int, input().split())
arr = list(map(int, input().split()))
magic_nums = [2, 3]
for i in range(max(arr)+1):
    if is_prime(i):
        magic_nums.append(i)
max_prizae = 0
for m in magic_nums:
    coin = k
    temp_prize = 0
    for num in arr:
        if num % m == 0:
            temp_prize += 1
        elif coin >= num:
            temp_prize += 1
            coin -= num
        else:
            break
    max_prizae = max(max_prizae, temp_prize)
print(max_prizae)
