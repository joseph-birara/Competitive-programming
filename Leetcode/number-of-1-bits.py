class Solution:
    def hammingWeight(self, n: int) -> int:
        return Counter(bin(n))['1']
        