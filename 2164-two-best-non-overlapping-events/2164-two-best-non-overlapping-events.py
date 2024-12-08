class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        from bisect import bisect_right

        # Sort events by their end time
        events.sort(key=lambda x: x[1])  # Sort by endTime

        # Precompute the prefix maximum array
        n = len(events)
        max_value = 0
        prefix_max = [0] * n
        for i in range(n):
            prefix_max[i] = max(prefix_max[i - 1] if i > 0 else 0, events[i][2])

        # Precompute the end times for binary search
        end_times = [event[1] for event in events]

        # Iterate through events and find the best combination
        for i in range(n):
            start, end, value = events[i]

            # Binary search to find the latest non-overlapping event
            idx = bisect_right(end_times, start - 1) - 1

            # Calculate the max value considering the current event
            current_max = value
            if idx >= 0:
                current_max += prefix_max[idx]

            # Update the global maximum
            max_value = max(max_value, current_max)

        return max_value
