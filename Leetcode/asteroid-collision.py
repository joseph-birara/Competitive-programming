from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for num in asteroids:
            while stack and num < 0 and stack[-1] > 0:
                if stack[-1] == -num:
                    stack.pop()
                    num = 0  # Both asteroids annihilate each other
                    break
                elif stack[-1] < -num:
                    stack.pop()
                else:
                    num = 0  # The negative asteroid is destroyed

            if num != 0:
                stack.append(num)

        return stack
