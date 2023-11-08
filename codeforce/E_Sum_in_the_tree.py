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


# Example usage:
arr = [4, 2, -3, 1, 6]
result = countSubarray(arr)
print("Number of subarrays with sum 0:", result)
