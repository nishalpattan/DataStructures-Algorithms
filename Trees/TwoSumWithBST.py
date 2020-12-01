# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Using Inorder traversal + Two sum approach
    TC : O(n)
    SC : O(n)
    """

    def findTarget(self, root: TreeNode, k: int) -> bool:
        inorder = self.inorderTraversal(root)
        start = 0
        end = len(inorder) - 1
        while start < end:
            currSum = inorder[start] + inorder[end]
            if currSum == k:
                return True
            elif currSum < k:
                start += 1
            elif currSum > k:
                end -= 1
        return False

    def inorderTraversal(self, root):
        inorder = list()
        stack = list()
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            inorder.append(root.val)
            root = root.right
        return inorder

