class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if (len(changed) % 2) !=0:
            return []
        
        result = []
        count = Counter(changed)
        for n in sorted(changed):
            if count[n] == 0:
                continue
            if 2 * n not in count:
                return []
            count[n] -= 1
            count[2 * n] -= 1
            if count[2 * n] == 0:
                count.pop( 2 * n)
            result.append(n)
        return result