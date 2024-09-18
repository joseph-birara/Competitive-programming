class Solution:
    def smallestNumber(self, num: int) -> int:
        is_negative = num < 0
        digits = list(str(abs(num)))
        
        if is_negative:
            # Sort digits in descending order for negative numbers
            digits.sort(reverse=True)
        else:
            # Sort digits in ascending order for positive numbers
            digits.sort()
            # Avoid leading zeros
            if digits[0] == '0':
                # Find the first non-zero digit
                for i in range(1, len(digits)):
                    if digits[i] != '0':
                        # Swap the first non-zero digit with the leading zero
                        digits[0], digits[i] = digits[i], '0'
                        break
        
        # Join the digits and convert back to integer
        rearranged_num = int(''.join(digits))
        
        return -rearranged_num if is_negative else rearranged_num
            