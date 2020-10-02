"""
InOrder Traversal
TC : O(n)
SC : O(n)
"""
class TreeNode:
    def __init__(self, val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root):
    stack = list()
    res = list()
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        root = root.right
    return res

if __name__ == "__main__":
    tree1 = TreeNode(2)
    tree1.left = TreeNode(1)
    tree1.right = TreeNode(3)
    print(inorder_traversal(tree1))


