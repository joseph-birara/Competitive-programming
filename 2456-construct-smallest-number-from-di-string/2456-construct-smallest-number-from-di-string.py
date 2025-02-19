class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result = []
        num = 1  # Start numbering from '1'

        for i in range(len(pattern) + 1):
            stack.append(str(num))
            num += 1

            if i == len(pattern) or pattern[i] == 'I':  
                while stack:
                    result.append(stack.pop())

        return "".join(result)

        
        