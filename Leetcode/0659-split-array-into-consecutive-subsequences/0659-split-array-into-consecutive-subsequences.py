

class Solution:
    def isPossible(self, nums):
        # Create a frequency dictionary to store the count of each number
        freq = defaultdict(int)
        # Create a dictionary to store the count of subsequences that can be appended to each number
        appendfreq = defaultdict(int)

        # Count the frequency of each number in the input list
        for num in nums:
            freq[num] += 1

        # Iterate over each number in the input list
        for num in nums:
            # If the current number has been used up to form a subsequence, move to the next number
            if freq[num] == 0:
                continue
            # If there are subsequences that can be appended to the current number, append one and update the counts
            elif appendfreq[num] > 0:
                appendfreq[num] -= 1
                appendfreq[num + 1] += 1
            # If the next two consecutive numbers are available, use them to form a subsequence and update the counts
            elif freq[num + 1] > 0 and freq[num + 2] > 0:
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                appendfreq[num + 3] += 1
            # If none of the conditions above are met, it is not possible to form a valid subsequence
            else:
                return False

            # Decrease the frequency of the current number since it has been used
            freq[num] -= 1

        # If all numbers have been used to form valid subsequences, return True
        return True
