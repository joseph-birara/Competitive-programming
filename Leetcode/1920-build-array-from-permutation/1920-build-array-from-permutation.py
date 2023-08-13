class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        answerArray = []
        
        for index in range(len(nums)):
            answerArray.append(nums[nums[index]])
        return answerArray