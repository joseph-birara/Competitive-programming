class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for index, cr in enumerate(s):
            if count[cr] == 1:
                return index
        return -1
        