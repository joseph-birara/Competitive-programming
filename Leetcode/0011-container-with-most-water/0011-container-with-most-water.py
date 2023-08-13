class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        vl = 0
        i = 0
        j = n-1
        while i< j:
            vl = max(min(height[j],height[i])*(j-i), vl)
            if height[j]>height[i]:
                i += 1 
            else:
                j -=1
        return vl
        