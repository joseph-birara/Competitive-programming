# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        # Initialize the index to 0
        self.current_index = 0

    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        # Start the recovery process from the root (depth 0)
        return self._rebuild_tree(traversal, 0)

    def _rebuild_tree(self, traversal: str, current_depth: int) -> TreeNode:
        # If we've processed the entire string, return None (base case)
        if self.current_index >= len(traversal):
            return None

        # Count the number of dashes at the current position to determine the depth
        dash_count = 0
        while (
            self.current_index + dash_count < len(traversal)
            and traversal[self.current_index + dash_count] == "-"
        ):
            dash_count += 1

        # If the number of dashes doesn't match the expected depth, return None
        if dash_count != current_depth:
            return None

        # Move the index forward past the dashes
        self.current_index += dash_count

        # Extract the node's value from the traversal string
        node_value = 0
        while self.current_index < len(traversal) and traversal[self.current_index].isdigit():
            node_value = node_value * 10 + int(traversal[self.current_index])
            self.current_index += 1

        # Create the current tree node
        current_node = TreeNode(node_value)

        # Recursively build the left and right children of the current node
        current_node.left = self._rebuild_tree(traversal, current_depth + 1)
        current_node.right = self._rebuild_tree(traversal, current_depth + 1)

        # Return the constructed node
        return current_node
