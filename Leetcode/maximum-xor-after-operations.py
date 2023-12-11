from typing import List

class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        res = [0] * 32

        for num in nums:
            for i in range(32):
                if (num >> i) & 1:
                    res[i] += 1

        result = 0
        for i in range(31, -1, -1):
            result <<= 1
            if res[i] > 0:
                result |= 1

        return result
