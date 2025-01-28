class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        bannedD = defaultdict(int)
        for num in banned :
            bannedD[num] = 1
        
        curr_sum = 0
        cnt = 0
        for i in range(1,n+1):
            if curr_sum + i >maxSum:
                return cnt
            if not bannedD[i]:
                curr_sum += i
                cnt += 1
        return cnt
            




        
        