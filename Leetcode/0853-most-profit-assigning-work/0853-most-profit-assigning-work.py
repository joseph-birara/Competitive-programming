from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        res = 0
        arr = []
        n = len(profit)
        
        # Combine difficulty and profit into a list of tuples
        for index in range(n):
            arr.append((difficulty[index], profit[index]))       

        # Sort the array by difficulty, then by profit
        arr.sort()
        
        # Update the profit to be the maximum profit up to that difficulty
        for index in range(1, n):
            arr[index] = (arr[index][0], max(arr[index][1], arr[index-1][1]))
        
        # For each worker, find the maximum profit they can achieve
        for man in worker:
            left = 0
            right = n - 1
            best_profit = 0
            
            while left <= right:
                mid = (left + right) // 2
                if arr[mid][0] <= man:
                    best_profit = arr[mid][1]
                    left = mid + 1
                else:
                    right = mid - 1

            res += best_profit

        return res
