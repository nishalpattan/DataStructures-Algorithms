import collections


def nodeDepths(root):
    # Write your code here.
    depth = -1
    q = collections.deque()
    q.append(root)
    sum_of_depths = 0
    while q:
        depth += 1
        print(depth)
        size = len(q)
        for i in range(size):
            sum_of_depths += depth
            curr_node = q.popleft()
            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)
    return sum_of_depths


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

if __name__ == "__main__":
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(4)
    root.left.left.left = BinaryTree(8)
    root.left.left.right = BinaryTree(9)
    root.left.right = BinaryTree(5)
    root.right = BinaryTree(3)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    print(nodeDepths(root))