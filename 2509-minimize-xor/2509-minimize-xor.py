class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Count the number of 1's in the binary representation of num2
        num2_ones = bin(num2).count('1')

        # Get the initial bits of num1
        num1_bits = [1 if (num1 & (1 << i)) else 0 for i in range(31, -1, -1)]
        
        # Build x to have the same number of 1's as num2, minimizing XOR
        x = 0
        count_ones = 0
        
        # Prioritize keeping the 1's from num1 (most significant bits first)
        for i in range(31, -1, -1):
            if num1_bits[31 - i] == 1 and count_ones < num2_ones:
                x |= (1 << i)  # Set the bit at position i
                count_ones += 1

        # If we still need more 1's, add them starting from the least significant bits
        for i in range(32):
            if count_ones == num2_ones:
                break
            if (x & (1 << i)) == 0:  # If the bit at position i is 0
                x |= (1 << i)  # Set the bit at position i
                count_ones += 1

        return x
