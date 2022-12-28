class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [float(target - p ) / s for p, s in sorted(zip(position, speed))]
        prev = 0
        temp = 0
        for t in time[::-1]:
            if t <= prev:
                continue
            prev = t
            temp += 1
        return temp
            
        
        
        