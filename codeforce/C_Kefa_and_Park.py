num_vertices, max_cats = map(int, input().split())
cat_count = list(map(int, input().split()))

adj_list = [[] for _ in range(num_vertices)]

for _ in range(num_vertices - 1):
    vertex_a, vertex_b = map(int, input().split())
    adj_list[vertex_a - 1].append(vertex_b - 1)
    adj_list[vertex_b - 1].append(vertex_a - 1)


def dfs(start_vertex, parent_vertex, start_cats):
    stack = [(start_vertex, parent_vertex, start_cats)]
    leaf_count = 0
    while stack:
        current_vertex, parent_vertex, current_cats = stack.pop()
        if current_cats > max_cats:
            continue
        is_leaf = True
        for neighbor in adj_list[current_vertex]:
            if neighbor != parent_vertex:
                is_leaf = False
                stack.append((neighbor, current_vertex, current_cats *
                             cat_count[neighbor] + cat_count[neighbor]))
        leaf_count += is_leaf
    return leaf_count


num_leafs = dfs(0, -1, cat_count[0])

print(num_leafs)
