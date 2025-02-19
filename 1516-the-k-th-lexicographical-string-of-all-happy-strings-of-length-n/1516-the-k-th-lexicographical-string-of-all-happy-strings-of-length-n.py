class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []
    
        def backtrack(curr):
            if len(curr) == n:
                result.append(curr)
                return
            
            for char in 'abc':
                if not curr or curr[-1] != char:
                    backtrack(curr + char)
        
        backtrack("")
        
        return result[k - 1] if k <= len(result) else ""

        