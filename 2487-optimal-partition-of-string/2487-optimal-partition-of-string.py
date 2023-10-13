class Solution:
    def partitionString(self, s: str) -> int:

        res = 1
        count = defaultdict(int)
        for char in s:
            if count[char] ==1:
                res +=1
                count = defaultdict(int)
            
            count[char] +=1
            # print(count)
            # print(res)
        return res
        

        