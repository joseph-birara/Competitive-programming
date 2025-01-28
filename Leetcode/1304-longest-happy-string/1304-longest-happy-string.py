import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Initialize a max heap for character counts
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))
        
        result = []
        
        while heap:
            # Take the character with the highest count
            count1, char1 = heapq.heappop(heap)
            
            # If adding this character violates the "no three consecutive" rule
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                if not heap:
                    break  # No other characters to use
                # Use the next most frequent character
                count2, char2 = heapq.heappop(heap)
                result.append(char2)
                if count2 + 1 < 0:  # Still has remaining count
                    heapq.heappush(heap, (count2 + 1, char2))
                # Push the previous character back
                heapq.heappush(heap, (count1, char1))
            else:
                # Safe to use char1
                result.append(char1)
                if count1 + 1 < 0:  # Still has remaining count
                    heapq.heappush(heap, (count1 + 1, char1))
        
        return ''.join(result)
