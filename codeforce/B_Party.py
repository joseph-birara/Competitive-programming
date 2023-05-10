import sys
from collections import defaultdict

# Increase recursion limit to avoid stack overflow during DFS
sys.setrecursionlimit(2500)


def main():
    # Read in number of employees
    n = int(input())
    # Initialize empty adjacency list and list of "root" employees
    adjlist = defaultdict(list)
    roots = []

    # Loop through each employee and their manager
    for i in range(1, n + 1):
        emp = int(input())

        # If employee has no manager, add them to list of "root" employees
        if emp == -1:
            roots.append(i)
        # Otherwise, add this employee to their manager's list of direct reports
        else:
            adjlist[emp].append(i)

    # Initialize variable to store maximum depth found during DFS
    max_level = 0
    # Loop through each root employee and perform DFS to find maximum depth
    for root in roots:
        level = dfs(root, adjlist)
        max_level = max(level, max_level)

    # Output the maximum depth found
    print(max_level)

# Recursive DFS function to find depth of each employee in the tree


def dfs(cur, adjlist):
    # Initialize current depth to 0
    level = 0
    # Loop through each direct report of this employee and perform DFS to find maximum depth
    for nxt in adjlist[cur]:
        level = max(dfs(nxt, adjlist), level)
    # Add 1 to the maximum depth found for this employee
    return level + 1


# Call the main function to run the program
main()
