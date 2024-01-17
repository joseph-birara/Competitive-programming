class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        return len(Counter(arr)) == len(list(set(Counter(arr).values())))
        