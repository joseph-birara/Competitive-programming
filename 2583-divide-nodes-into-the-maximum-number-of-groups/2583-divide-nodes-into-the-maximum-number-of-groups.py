from collections import deque

class Solution:

    # Main function to calculate the maximum number of magnificent sets
    def magnificentSets(self, num_nodes, edge_list):
        # Create adjacency list for the graph
        graph = [[] for _ in range(num_nodes)]
        for edge in edge_list:
            # Transition to 0-index
            graph[edge[0] - 1].append(edge[1] - 1)
            graph[edge[1] - 1].append(edge[0] - 1)

        # Initialize color array to -1
        node_colors = [-1] * num_nodes

        # Check if the graph is bipartite
        for node in range(num_nodes):
            if node_colors[node] != -1:
                continue
            # Start coloring from uncolored nodes
            node_colors[node] = 0
            if not self._isBipartite(graph, node, node_colors):
                return -1

        # Calculate the longest shortest path for each node
        node_distances = [
            self._calculateLongestPath(graph, node, num_nodes)
            for node in range(num_nodes)
        ]

        # Calculate the total maximum number of groups across all components
        total_max_groups = 0
        visited_nodes = [False] * num_nodes
        for node in range(num_nodes):
            if visited_nodes[node]:
                continue
            # Add the number of groups for this component to the total
            total_max_groups += self._calculateGroupsForComponent(
                graph, node, node_distances, visited_nodes
            )

        return total_max_groups

    # Checks if the graph is bipartite starting from the given node
    def _isBipartite(self, graph, node, node_colors):
        for neighbor in graph[node]:
            # If a neighbor has the same color as the current node, the graph is not bipartite
            if node_colors[neighbor] == node_colors[node]:
                return False
            # If the neighbor is already colored, skip it
            if node_colors[neighbor] != -1:
                continue
            # Assign the opposite color to the neighbor
            node_colors[neighbor] = (node_colors[node] + 1) % 2
            # Recursively check bipartiteness for the neighbor; return false if it fails
            if not self._isBipartite(graph, neighbor, node_colors):
                return False
        # If all neighbors are properly colored, return true
        return True

    # Computes the longest shortest path (height) in the graph starting from the source node
    def _calculateLongestPath(self, graph, start_node, num_nodes):
        # Initialize a queue for BFS and a visited array
        node_queue = deque([start_node])
        visited_nodes = [False] * num_nodes
        visited_nodes[start_node] = True
        max_distance = 0

        # Perform BFS layer by layer
        while node_queue:
            # Process all nodes in the current layer
            for _ in range(len(node_queue)):
                current_node = node_queue.popleft()
                # Visit all unvisited neighbors of the current node
                for neighbor in graph[current_node]:
                    if visited_nodes[neighbor]:
                        continue
                    visited_nodes[neighbor] = True
                    node_queue.append(neighbor)
            # Increment the distance for each layer
            max_distance += 1

        # Return the total distance (longest shortest path)
        return max_distance

    # Calculates the maximum number of groups for a connected component
    def _calculateGroupsForComponent(self, graph, node, node_distances, visited_nodes):
        # Start with the distance of the current node as the maximum
        max_groups = node_distances[node]
        visited_nodes[node] = True

        # Recursively calculate the maximum for all unvisited neighbors
        for neighbor in graph[node]:
            if visited_nodes[neighbor]:
                continue
            max_groups = max(
                max_groups,
                self._calculateGroupsForComponent(
                    graph, neighbor, node_distances, visited_nodes
                ),
            )
        return max_groups
