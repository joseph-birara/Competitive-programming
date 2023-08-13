class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        temp =[]
        for num in matrix:
            temp.extend([x for x in num])
        temp.sort()
        return temp[k-1]
        