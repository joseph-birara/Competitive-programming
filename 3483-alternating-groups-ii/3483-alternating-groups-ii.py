class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        for i in range(k - 1):
            colors.append(colors[i])

        size = len(colors)
        count = 0
        start = 0
        end = 1

        while end < size:
            if colors[end] == colors[end - 1]:
                start = end
                end += 1
                continue

            end += 1

            if end - start < k:
                continue

            count += 1
            start += 1

        return count
