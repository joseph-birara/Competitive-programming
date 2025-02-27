
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        max_len = 0
        n = len(arr)
        s = set(arr)

        for i in range(n):
            for j in range(i + 1, n):
                first, second = arr[i], arr[j]
                curr_len = 2

                while first + second in s:
                    third = first + second
                    first, second = second, third
                    curr_len += 1
                    max_len = max(max_len, curr_len)

        return max_len if max_len >= 3 else 0  
