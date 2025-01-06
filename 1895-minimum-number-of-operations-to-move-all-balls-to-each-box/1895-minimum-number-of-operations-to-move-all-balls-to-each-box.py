class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)

        ans = [0]*n

        for index in range(n):
            moves = 0
            for i in range(n):
                if boxes[i] == '1':
                    moves += abs(i - index)
            ans[index] = moves
        return ans



        