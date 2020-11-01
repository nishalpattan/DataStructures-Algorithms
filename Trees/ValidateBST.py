"""
    https://leetcode.com/problems/validate-binary-search-tree
    TC : O(n)
    SC : O(n)
    n --> number of nodes in tree
    """
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float("-inf"), float("inf"))
    def helper(self, root, _min, _max):
        if root is None:
            return True
        if not(_min < root.val < _max):
            return False
        else:
            return self.helper(root.left, _min, root.val) and self.helper(root.right, root.val, _max)