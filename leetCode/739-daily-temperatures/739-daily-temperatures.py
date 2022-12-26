class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0]*n
        s = []
        for i in range(n):
            while (len(s) >0) and temperatures[s[-1]] < temperatures[i]:
                answer[s[-1]] = i - s[-1]
                s.pop()
            s.append(i)
                    
        return answer
                    
               
                
                
            
        
        
        
        