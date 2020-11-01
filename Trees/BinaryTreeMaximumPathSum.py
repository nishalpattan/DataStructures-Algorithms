# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    https://leetcode.com/problems/binary-tree-maximum-path-sum
    TC : O(N)
    SC : O(N)
    N --> number of nodes in tree
    """
    def __init__(self):
        self.max_path_sum = float("-inf")
    def maxPathSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.helper(root)
        return self.max_path_sum
    def helper(self,node):
        if node is None:
            return 0
        left = max(0,self.helper(node.left))
        right = max(0,self.helper(node.right))
        self.max_path_sum = max(self.max_path_sum, node.val + left + right)
        return max(right, left) + node.val