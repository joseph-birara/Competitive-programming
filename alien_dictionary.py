from collections import *
class Solution:
    def findOrder(self,alien_dict, N, K):
        
        graph = defaultdict(list)
        in_degree = {ch : 0 for word in alien_dict for ch in  word}
        
        for i in range(N-1):
            
            first_word = alien_dict[i]
            second_word = alien_dict[i+1]
            small = min(len(first_word),len(second_word))
            
            for j in range(small):
                if first_word[j] != second_word[j]:
                    graph[first_word[j]].append(second_word[j])
                    in_degree[second_word[j]] += 1
                    break
        
        arr = [ch for ch in in_degree if in_degree[ch] == 0]
        
        queue = deque(arr)
        ans = []
        while queue:
            
            node  = queue.popleft()
            ans.append(node)
            
            for edge in graph[node]:
                
                in_degree[edge] -= 1
                if in_degree[edge] == 0:
                    
                    queue.append(edge)
        return ans
                    
