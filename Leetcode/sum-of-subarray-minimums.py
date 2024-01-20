class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        MOD = 10**9 + 7
        n = len(arr)

       
        n = len(arr)
        left_equal_smaller, right_smaller = [-1] * n, [n] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                right_smaller[stack.pop()] = i
            stack.append(i)
        
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                left_equal_smaller[stack.pop()] = i
            stack.append(i)
        # print(right_smaller)
        # print(left_equal_smaller)
        min_sums = 0
        for i in range(n):
            min_sums += (right_smaller[i] - i) *  (i - left_equal_smaller[i]) * arr[i]
            min_sums %= MOD
            
            
        return min_sums
