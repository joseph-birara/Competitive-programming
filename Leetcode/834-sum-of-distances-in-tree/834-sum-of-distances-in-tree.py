class Solution:
    def sumOfDistancesInTree(self, N, edges):
    
        result = [0] * N
        cnt = [1] * N
        tree = defaultdict(set)

        for u, v in edges:
            tree[u].add(v)
            tree[v].add(u)

        def postorder(node, parent=None):
            for child in tree[node]:
                if child == parent:
                    continue
                postorder(child, node)
                cnt[node] += cnt[child]
                result[node] += result[child] + cnt[child]

        def preorder(node, parent=None):

            for child in tree[node]:
                if child == parent:
                    continue
               
                result[child] = result[node] - cnt[child] + (N - cnt[child])
                preorder(child, node)

        postorder(0)
        preorder(0)
        return result
        