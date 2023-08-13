from collections import defaultdict

class Solution:
    def loudAndRich(self, richer, quiet):
        # Step 1: Build the graph
        graph = defaultdict(list)
        for richer_person, poorer_person in richer:
            graph[poorer_person].append(richer_person)

        # Step 2: Perform DFS with memoization
        memo = {}

        def dfs(person):
            if person in memo:
                return memo[person]

            least_quiet = person  # Assume the current person is the least quiet

            for richer_person in graph[person]:
                candidate = dfs(richer_person)  # Recursively find the least quiet person
                if quiet[candidate] < quiet[least_quiet]:
                    least_quiet = candidate

            memo[person] = least_quiet
            return least_quiet

        # Step 3: Find the least quiet person for each person
        answer = []
        for person in range(len(quiet)):
            answer.append(dfs(person))

        return answer
