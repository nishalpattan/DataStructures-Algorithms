class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def flattenBinaryTree(root):
    # Write your code here.
	"""
	TC : O(n)
	SC : O(n)
	n --> number of nodes in tree
	"""
    inorder_nodes = get_inorder_nodes(root)
	for i in range(0, len(inorder_nodes) - 1):
		left_node = inorder_nodes[i]
		right_node = inorder_nodes[i+1]
		left_node.right = right_node
		right_node.left = left_node
	return inorder_nodes[0]

def get_inorder_nodes(root):
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