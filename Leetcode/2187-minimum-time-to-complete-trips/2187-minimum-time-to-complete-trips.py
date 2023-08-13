class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        low = 1
        m = max(time)
        high = totalTrips*m
        ans = None
        
        def isPossible(limit, totalTrips):
            t = 0
            for a in time:
                t += int(limit*1.0/a)
            return t >= totalTrips       
        
        while low <= high:
            mid = (low+high)//2            
            
            if isPossible(mid, totalTrips):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans