class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False  # Odd-length strings cannot be valid
        
        # First pass: Left to right
        min_open, max_open = 0, 0
        for i in range(n):
            if locked[i] == '1':
                if s[i] == '(':
                    min_open += 1
                    max_open += 1
                else:  # s[i] == ')'
                    min_open = max(0, min_open - 1)
                    max_open -= 1
            else:  # s[i] is flexible
                min_open = max(0, min_open - 1)
                max_open += 1
            
            if max_open < 0:
                return False  # Too many closing parentheses

        # Second pass: Right to left
        min_close, max_close = 0, 0
        for i in range(n - 1, -1, -1):
            if locked[i] == '1':
                if s[i] == ')':
                    min_close += 1
                    max_close += 1
                else:  # s[i] == '('
                    min_close = max(0, min_close - 1)
                    max_close -= 1
            else:  # s[i] is flexible
                min_close = max(0, min_close - 1)
                max_close += 1
            
            if max_close < 0:
                return False  # Too many opening parentheses
        
        return min_open == 0
