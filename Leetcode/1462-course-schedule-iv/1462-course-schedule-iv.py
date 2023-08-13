from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Step 1: Build the graph for prerequisites
        graph = defaultdict(list)
        for prerequisite in prerequisites:
            graph[prerequisite[0]].append(prerequisite[1])

        # Step 2: Perform DFS to check prerequisites for each query
        answer = []
        for query in queries:
            if self.hasPrerequisite(graph, query[0], query[1]):
                answer.append(True)
            else:
                answer.append(False)

        return answer

    def hasPrerequisite(self, graph: defaultdict(list), start: int, target: int) -> bool:
        stack = [start]
        visited = set()

        while stack:
            course = stack.pop()
            if course == target:
                return True

            visited.add(course)

            for prerequisite in graph[course]:
                if prerequisite not in visited:
                    stack.append(prerequisite)

        return False
