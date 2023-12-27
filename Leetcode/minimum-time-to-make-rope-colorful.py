class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        total_time = sum(neededTime)
        curr_max = neededTime[0]
        n = len(colors)
        left = 0
        for i in range(1,n):
            if colors[i] == colors[left]:
                curr_max = max(curr_max , neededTime[i])
            else:
                total_time -= curr_max
                left = i
                curr_max = neededTime[i]

        return total_time - curr_max
            
        