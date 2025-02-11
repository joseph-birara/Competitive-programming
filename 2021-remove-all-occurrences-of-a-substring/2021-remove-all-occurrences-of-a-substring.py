class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        n = len(part)

        for char in s:
            stack.append(char)
            if len(stack) >= n and stack[-n:] == list(part):
                stack[-n:] = []  

        return ''.join(stack)
