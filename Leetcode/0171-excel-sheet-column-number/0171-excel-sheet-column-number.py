class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        result = 0
        for char in columnTitle:
            # Convert the character to its corresponding numeric value (A -> 1, B -> 2, ..., Z -> 26)
            num = ord(char) - ord('A') + 1
            # Update the result by multiplying it by 26 and adding the numeric value of the current character
            result = result * 26 + num
        return result
