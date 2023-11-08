class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        binary = [Counter(bin(num))['1'] for num in arr]
        return [num[1] for num in sorted(zip(binary,arr))]
        