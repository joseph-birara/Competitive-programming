class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = defaultdict(int)  
        balls = {}  
        ans = []
        count = 0 

        for ball, color in queries:
            if ball in balls: 
                prev_color = balls[ball]
                if colors[prev_color] == 1:  
                    count -= 1
                colors[prev_color] -= 1  

            if colors[color] == 0:  
                count += 1
            
            colors[color] += 1 
            balls[ball] = color 

            ans.append(count) 

        return ans
