class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        rev =0
        while x >0:
            temp = x%10
            rev= rev*10 + temp
            x = x//10
        print(rev)
        if rev== original:
            return True 
        return False
        
