class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Function to merge the max character counts across all words in words2
        def merge_max_counts(words):
            max_count = Counter()
            for word in words:
                word_count = Counter(word)
                for char, count in word_count.items():
                    max_count[char] = max(max_count[char], count)
            return max_count

        # Find the maximum frequency requirement for each character from words2
        max_requirements = merge_max_counts(words2)

        # Filter words1 based on the max requirements
        result = []
        for word in words1:
            word_count = Counter(word)
            if all(word_count[char] >= count for char, count in max_requirements.items()):
                result.append(word)

        return result
            