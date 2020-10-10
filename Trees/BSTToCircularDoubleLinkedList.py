"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        """
        https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list
        TC : O(n)
        SC : O(n)
        """
        if root is None:
            return None
        inorder_nodes = self.get_inorder_nodes(root)

        for i in range(0, len(inorder_nodes) - 1):
            left_node = inorder_nodes[i]
            right_node = inorder_nodes[i + 1]
            left_node.right = right_node
            right_node.left = left_node
        inorder_nodes[0].left = inorder_nodes[-1]
        inorder_nodes[-1].right = inorder_nodes[0]
        return inorder_nodes[0]

    def get_inorder_nodes(self, root):
        inorder = list()
        stack = list()
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            inorder.append(root)
            root = root.right
        return inorder
