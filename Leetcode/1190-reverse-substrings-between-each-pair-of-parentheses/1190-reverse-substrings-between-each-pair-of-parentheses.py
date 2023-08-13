class Solution:
    def reverseParentheses(self, s: str) -> str:
        temp = []
        n = len(s)
        
        for i in range(n):
            if s[i] == '(':
                temp.append(i)
            elif s[i] == ')':        
                s2 = s[temp[-1]:i+1]              
                s = s[:temp[-1]] + s2[::-1] + s[i+1:]
                del temp[-1]
        res = ""
        for k in s:
            if k != '(' and k != ')':
                res += k
                
                
                
                
                
        return res
                
                
                