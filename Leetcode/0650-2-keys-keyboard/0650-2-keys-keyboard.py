class Solution:
    def minSteps(self, n: int) -> int:
        # num of As opeartions and As copied 
        screen = 1 
        operations = 0
        clipboard = 0
        
        while screen < n:
            if n % screen ==0:
                operations +=1
                clipboard = screen
            screen += clipboard
            operations +=1
        
        return operations 