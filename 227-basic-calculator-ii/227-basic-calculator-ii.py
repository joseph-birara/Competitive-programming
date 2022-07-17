class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        num = 0
        operand = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in ['+', '-', '*', '/'] or i == len(s) - 1:
                if operand == '+':
                    stack.append(num)
                elif operand == '-':
                    stack.append(-num)
                elif operand == '*':
                    stack.append(stack.pop() * num)
                elif operand == '/':
                    stack.append(int(stack.pop() / num))
                operand = s[i]
                num = 0
        return sum(stack)