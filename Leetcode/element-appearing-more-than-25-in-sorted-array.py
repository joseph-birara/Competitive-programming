class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counter = Counter(arr)
        max_element = max(counter, key=counter.get)
        return max_element
        