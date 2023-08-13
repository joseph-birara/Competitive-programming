class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        first = max(score )
        ans = [0]*len(score )
        memo = defaultdict(int)
        for index,num in enumerate (score):
            memo[num] = index 
        score.sort(reverse = True)
        for index,num in enumerate (score):
            if index  == 0:
                ans[memo[num]] = "Gold Medal"
            elif index  == 1:
                ans[memo[num]] = "Silver Medal"
            elif index  == 2:
                ans[memo[num]] = "Bronze Medal"
            else:
                ans[memo[num]] = str(index+1)
        return ans
                
                
        
        
        