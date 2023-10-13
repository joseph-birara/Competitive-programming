class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_indices = []

class WordFilter:
    def __init__(self, words):
        self.prefix_trie = TrieNode()
        self.suffix_trie = TrieNode()
        
        # Insert words into both prefix and suffix tries.
        for idx, word in enumerate(words):
            self._insert_word(self.prefix_trie, word, idx)
            self._insert_word(self.suffix_trie, word[::-1], idx)

    def _insert_word(self, trie, word, index):
        node = trie
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.word_indices.append(index)

    def _search(self, trie, word):
        node = trie
        for char in word:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.word_indices

    def f(self, prefix, suffix):
        prefix_indices = self._search(self.prefix_trie, prefix)
        reversed_suffix_indices = self._search(self.suffix_trie, suffix[::-1])

        # Find the largest common index between prefix and reversed suffix indices.
        i, j = len(prefix_indices) - 1, len(reversed_suffix_indices) - 1
        while i >= 0 and j >= 0:
            if prefix_indices[i] == reversed_suffix_indices[j]:
                return prefix_indices[i]
            elif prefix_indices[i] > reversed_suffix_indices[j]:
                i -= 1
            else:
                j -= 1

        return -1