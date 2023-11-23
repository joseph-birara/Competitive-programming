class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        limit = max(arr)
        for num in range(1,limit+1):
            if num not in arr:
                k-=1
                if not k:
                    return num
        return limit + k
            
                
        