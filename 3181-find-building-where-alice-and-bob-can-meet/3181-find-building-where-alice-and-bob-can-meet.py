class Solution:
    def leftmostBuildingQueries(self, building_heights, test_cases):
        stack = []
        results = [-1 for _ in range(len(test_cases))]
        processed_queries = [[] for _ in range(len(building_heights))]
        
        for i in range(len(test_cases)):
            start = test_cases[i][0]
            end = test_cases[i][1]
            if start > end:
                start, end = end, start
            if building_heights[end] > building_heights[start] or start == end:
                results[i] = end
            else:
                processed_queries[end].append((building_heights[start], i))

        for i in range(len(building_heights) - 1, -1, -1):
            stack_size = len(stack)
            for height, index in processed_queries[i]:
                position = self.binary_search(height, stack)
                if position < stack_size and position >= 0:
                    results[index] = stack[position][1]
            while stack and stack[-1][0] <= building_heights[i]:
                stack.pop()
            stack.append((building_heights[i], i))
        
        return results

    def binary_search(self, target_height, stack):
        left = 0
        right = len(stack) - 1
        found_position = -1
        while left <= right:
            mid = (left + right) // 2
            if stack[mid][0] > target_height:
                found_position = max(found_position, mid)
                left = mid + 1
            else:
                right = mid - 1
        return found_position
