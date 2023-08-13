class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        right = len(needle)
        left = 0
        limit = len(haystack)
        while right <=limit:
            if haystack[left:right] == needle:
                return left
            else:
                left+=1
                right +=1
        return -1
        