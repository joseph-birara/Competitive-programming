class Solution:
    def findComplement(self, num: int) -> int:
        # number of bits
        bits = int(log(num,2)) +1
        # xor by all 1's
        return num ^ (2**bits-1)