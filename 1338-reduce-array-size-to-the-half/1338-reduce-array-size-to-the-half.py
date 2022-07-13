from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        sort_nums = sorted(count.items(), key=lambda x: x[1], reverse=True)
        temp = 0
        sum = 0
        while  sum < len(arr)/2:
            sum += sort_nums[temp][1]
            temp +=1
        return temp
        