class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        m = len(popped)
        temp = []
        j = 0
        for i in range(n):
            temp.append(pushed[i])
            while temp and temp[-1] == popped[j] and j< m:
                temp.pop()
                j += 1
        return m == j
            
            
            
        
        