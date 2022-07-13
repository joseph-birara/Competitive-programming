class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        n = len(s)
        op = ['(','{','[']
        cl = [')','}',']']
        if n%2 != 0:
            return False
        
        for i in s:
            if i in op:
                temp.append(i)
            elif i in cl and len(temp) != 0:
                if  (( i == ')' and temp[-1] == '(' ) or ( i == '}' and temp[-1] == '{') or (i == ']' and temp[-1] == '[') ) == False:
                    return False
                
                del temp[-1]
            else:
                return False
        if len(temp) != 0:
            return False
        return True
                    
        
        