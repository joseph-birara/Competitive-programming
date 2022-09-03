class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        for i in range(len(palindrome)):
            
            if palindrome[i] == 'a':
                continue
            v = palindrome[:i] + 'a' + palindrome[i+1:]
            if v == v[::-1]:
                continue
            return palindrome[:i] + 'a' + palindrome[i+1:]
        if len(palindrome) == 1:
            return ''
        elif palindrome[-1] == 'a':
            return palindrome[:-1] + 'b'
        return palindrome[:-1] + 'a'
