class TrieNode:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def find_max_xor(self, num):
        node = self.root
        max_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            opposite_bit = 1 - bit
            if opposite_bit in node.children:
                max_xor |= (1 << i)
                node = node.children[opposite_bit]
            else:
                node = node.children[bit]
        return max_xor


def find_maximum_xor(nums):
    trie = Trie()
    max_xor = float('-inf')
    for num in nums:
        trie.insert(num)
        max_xor = max(max_xor, trie.find_max_xor(num))
    return max_xor


def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))

        max_xor = find_maximum_xor(nums)
        print(max_xor)


main()
