from collections import deque


def bfs_shortest_path(graph, start, end):
    # initialize the queue with the starting node
    queue = deque([(start, [start])])

    # keep track of visited nodes
    visited = set()

    while queue:
        # get the next node and path from the queue
        node, path = queue.popleft()

        # check if we have reached the end node
        if node == end:
            return path

        # mark the current node as visited
        visited.add(node)

        # add all unvisited neighbors to the queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    # if the end node is not reachable, return None
    return None
