# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    https://leetcode.com/problems/find-bottom-left-tree-value/
    TC : O(n)
    SC : O(n)
    """
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            return root.val
        q = collections.deque()
        q.append(root)
        result = 0
        while q:
            size = len(q)
            for i in range(size):
                curr_node = q.popleft()
                if i == 0:
                    result = curr_node.val
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
        return result