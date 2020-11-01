# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # __init__ part of recursive approach
    def __init__(self):
        self.levels = []

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # Recursive approach
        if root is None:
            return self.levels
        self.helper(root, 0)
        return self.levels

    # helper method part of recursive approach
    def helper(self, curr_node, level):
        if len(self.levels) == level:
            self.levels.append([])
        self.levels[level].append(curr_node.val)
        if curr_node.left:
            self.helper(curr_node.left, level + 1)
        if curr_node.right:
            self.helper(curr_node.right, level + 1)
            # Iterative + queue appraoch
        # if root is None:
        #     return []
        # q = collections.deque()
        # q.append(root)
        # res = list()
        # while q:
        #     size = len(q)
        #     temp = list()
        #     for i in range(size):
        #         curr_node = q.popleft()
        #         temp.append(curr_node.val)
        #         if curr_node.left:
        #             q.append(curr_node.left)
        #         if curr_node.right:
        #             q.append(curr_node.right)
        #     res.append(temp)
        # return res