class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        temp = []
        op = ['+', '-', '*','/']
        for i in tokens:
            
            if i not in op:
                temp.append(int(i))
            else:
                op1 = temp.pop()
                op2 = temp.pop()
                
                if i == '+':
                    temp.append(op2 + op1)
                if i == '-':
                    temp.append(op2 - op1)
                if i == '*':
                    temp.append(op2 * op1)
                    
                if i == '/':
                    if op2 * op1 >0:
                        temp.append(op2 // op1)
                    else:
                        temp.append((op2 +(-op2%op1)) //op1)
                    
        return temp[0]
                        
            
        