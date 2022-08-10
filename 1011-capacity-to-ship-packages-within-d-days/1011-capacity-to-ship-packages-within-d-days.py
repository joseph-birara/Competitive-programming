class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def isPossible(mid):
            days = 1
            cur = 0
            for w in weights:
                if w > mid:
                    return False
                if cur + w > mid:
                    cur = 0
                    days += 1
                cur += w
            return days <= D

        l, r = 1, sum(weights)

        while l <= r:
            mid = (l + r) // 2
            if isPossible(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
        
        