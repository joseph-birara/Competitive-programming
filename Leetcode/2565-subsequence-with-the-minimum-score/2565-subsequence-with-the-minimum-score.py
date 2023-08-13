class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        len_s, len_t = len(s), len(t)
        suffix_indices, t_pointer = [0] * len_s, len_t

        # Step 1: Fill the suffix_indices list
        for i in range(len_s)[::-1]:
            if t_pointer > 0 and s[i] == t[t_pointer - 1]:
                t_pointer -= 1
            suffix_indices[i] = t_pointer - 1

        min_score, t_pointer = t_pointer, 0

        # Step 2: Calculate the minimum possible score
        for i in range(len_s):
            min_score = min(min_score, max(0, suffix_indices[i] - t_pointer + 1))
            if t_pointer < len_t and s[i] == t[t_pointer]:
                t_pointer += 1

        return min(min_score, len_t - t_pointer)
