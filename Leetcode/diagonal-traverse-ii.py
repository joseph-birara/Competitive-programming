class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        hashmap = defaultdict(list)
        for row_num , row in enumerate(nums):
            for index, ele in enumerate(row):
                hashmap[row_num + index].append(ele)
        sorted_keys = sorted(hashmap.keys())
        

        res = []

        for key in sorted_keys:
            res.extend(hashmap[key][::-1])
        return res

        