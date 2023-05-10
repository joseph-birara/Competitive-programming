
import heapq


testsCase = int(input())

for _ in range(testsCase):
    n, m = map(int, input().split())

    nums = list(map(int, input().split()))
    operations = list(map(int, input().split()))

    heapq.heapify(nums)
    for num in operations:
        heapq.heappop(nums)
        heapq.heappush(nums, num)
    print(sum(nums))
