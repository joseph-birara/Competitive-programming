def determine_coin_denominations(results):
    weights = {'A': 0, 'B': 0, 'C': 0}

    for result in results:
        coin1, operator, coin2 = result

        if operator == '>':
            weights[coin1] += 1
            weights[coin2] -= 1
        else:  # operator == '<'
            weights[coin1] -= 1
            weights[coin2] += 1

    sorted_coins = sorted(weights, key=lambda x: weights[x])

    if weights[sorted_coins[0]] == 0 and weights[sorted_coins[1]] == 0:
        print("Impossible")
    else:
        print(sorted_coins[0] + sorted_coins[1] + sorted_coins[2])


# Read the weighing results
results = []
while True:
    try:
        result = input().strip()
        if not result:
            break
        results.append((result[0], result[1], result[2]))
    except EOFError:
        break

# Solve the problem
determine_coin_denominations(results)
