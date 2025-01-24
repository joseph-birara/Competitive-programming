class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:  
            return s

        ans = [0, 1]  

        def expandAroundCenter(left: int, right: int) -> None:
            nonlocal ans
            while left >= 0 and right < n and s[left] == s[right]:
                if (right - left + 1) > (ans[1] - ans[0]):
                    ans = [left, right + 1]
                left -= 1
                right += 1

        for i in range(n):
            
            expandAroundCenter(i, i)
            
            expandAroundCenter(i, i + 1)

        return s[ans[0]:ans[1]]
