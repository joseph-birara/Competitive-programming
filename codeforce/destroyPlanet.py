from collections import Counter


testCase = int(input())
for _ in range(testCase):
    num_planet , cost2 = map(int,input().split())
    planets = list(map(int,input().split()))
    totalCost =0

    count = Counter(planets)
    for orbit in count.keys():
        if count[orbit] > cost2:
            totalCost += cost2
        else:
            totalCost += count[orbit]
    print(totalCost)
