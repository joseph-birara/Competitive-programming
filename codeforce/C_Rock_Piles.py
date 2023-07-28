def nim_sum(a, b):
    return a ^ b


def determine_winner(N, M):
    nim_sum_val = nim_sum(N, M)
    if nim_sum_val == 0:
        return "abdullah"
    else:
        return "hasan"


# Read the number of test cases
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    result = determine_winner(N, M)
    print(result)
