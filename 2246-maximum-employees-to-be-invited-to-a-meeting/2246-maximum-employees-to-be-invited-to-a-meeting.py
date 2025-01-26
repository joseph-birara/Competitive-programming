class Solution:
    def maximumInvitations(self, favorites: List[int]) -> int:        
        # Helper function to perform BFS and calculate the maximum path length
        def bfs(start: int, visited_set: set, reverse_graph: List[List[int]]) -> int:
            queue = deque([(start, 0)])  # Queue to store (current_node, current_distance)
            max_length = 0
            while queue:
                current, distance = queue.popleft()
                for neighbor in reverse_graph[current]:
                    if neighbor in visited_set:
                        continue  # Skip already visited nodes
                    visited_set.add(neighbor)
                    queue.append((neighbor, distance + 1))
                    max_length = max(max_length, distance + 1)
            return max_length

        num_employees = len(favorites)
        reverse_graph = [[] for _ in range(num_employees)]  # Adjacency list for the reversed graph

        # Build the reversed graph
        for employee in range(num_employees):
            reverse_graph[favorites[employee]].append(employee)

        max_cycle_length = 0
        max_two_cycle_sum = 0
        is_visited = [False] * num_employees

        # Traverse each employee
        for employee in range(num_employees):
            if not is_visited[employee]:
                # Track the distance of each visited node
                visited_map = {}
                current_employee = employee
                depth = 0

                # Explore the graph
                while True:
                    if is_visited[current_employee]:
                        break
                    is_visited[current_employee] = True
                    visited_map[current_employee] = depth
                    depth += 1
                    next_employee = favorites[current_employee]

                    # Check if we've encountered a cycle
                    if next_employee in visited_map:
                        cycle_size = depth - visited_map[next_employee]
                        max_cycle_length = max(max_cycle_length, cycle_size)

                        # Special handling for 2-cycles
                        if cycle_size == 2:
                            nodes_in_two_cycle = {current_employee, next_employee}
                            max_two_cycle_sum += (
                                2
                                + bfs(next_employee, nodes_in_two_cycle, reverse_graph)
                                + bfs(current_employee, nodes_in_two_cycle, reverse_graph)
                            )
                        break
                    current_employee = next_employee

        # Return the maximum of the largest cycle or the two-cycle extensions
        return max(max_cycle_length, max_two_cycle_sum)
