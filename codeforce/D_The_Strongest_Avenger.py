def countSubarray(arr):
    count = 0
    prefixSum = 0
    prefixSumFreq = {}

    for num in arr:
        prefixSum += num
        if prefixSum == 0:
            count += 1
        if prefixSum in prefixSumFreq:
            count += prefixSumFreq[prefixSum]
        prefixSumFreq[prefixSum] = prefixSumFreq.get(prefixSum, 0) + 1

    return count


test = int(input())
for _ in range(test):
    n = int(input())
    arr = [int(el) for el in input()]

    for j in range(n):
        arr[j] -= 1
    print(countSubarray(arr))
