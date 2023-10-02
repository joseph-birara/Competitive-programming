class Solution:
    def findNthDigit(self, n: int) -> int:


        # Step 1: Determine the length of numbers in each group
        length = 1
        count = 9
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10

        # Step 2: Calculate the total number of digits in the groups up to the target group
        start = 10 ** (length - 1)

        # Step 3: Find the exact number in the target group
        num = start + (n - 1) // length

        # Step 4: Extract the nth digit from the number
        digit_index = (n - 1) % length
        return int(str(num)[digit_index])

   
   
        
        