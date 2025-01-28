class Solution:
    def minimumLength(self, s: str) -> int:
        hashmap = Counter(s)
        count = 0

        for key, value in hashmap.items():
            if value >2 :
                if value % 2 == 1:
                    count += 1
                else :
                    count += 2
            else :
                count += value
        return count
        

        