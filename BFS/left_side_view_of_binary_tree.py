import collections
class Node:
    def __init__(self, val=0, right=None,left=None):
        self.val = val
        self.right = right
        self.left = left


def left_side_of_bt(root):
    q = collections.deque()
    q.append(root)
    res = list()
    while q:
        size = len(q)
        for i in range(size):
            curr_node = q.popleft()
            if i == 0:
                res.append(curr_node.val)
            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)
    return res

if __name__ == "__main__":
    tree1 = Node(4)
    tree1.left = Node(2)
    tree1.right = Node(7)
    print(left_side_of_bt(tree1))
    tree2 = Node(7)
    tree2.left = Node(4)
    tree2.right = Node(9)
    tree2.left.left = Node(1)
    tree2.left.right = Node(4)
    tree2.right.left = Node(8)
    tree2.right.right = Node(9)
    tree2.right.right.right = Node(9)
    print(left_side_of_bt(tree2))