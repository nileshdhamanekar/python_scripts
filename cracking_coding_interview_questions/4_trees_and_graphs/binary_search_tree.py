class TreeNode:
    """
    Tree node
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Binary Search Tree
    """
    def __init__(self):
        self.root = None

    def add_node(self, current_node, value):
        if current_node is None:
            self.root = TreeNode(value)
        else:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = TreeNode(value)
                else:
                    self.add_node(current_node.left, value)
            else:
                if current_node.right is None:
                    current_node.right = TreeNode(value)
                else:
                    self.add_node(current_node.right, value)

    def print_in_order(self, node):
        if node is not None:
            self.print_in_order(node.left)
            print(node.value)
            self.print_in_order(node.right)

    def print_pre_order(self, node):
        if node is not None:
            print(node.value)
            self.print_pre_order(node.left)
            self.print_pre_order(node.right)

    def print_post_order(self, node):
        if node is not None:
            self.print_post_order(node.left)
            self.print_post_order(node.right)
            print(node.value)

b = BinarySearchTree()
b.add_node(b.root, 42)
b.add_node(b.root,23)
b.add_node(b.root,83)
b.add_node(b.root,40)
b.add_node(b.root, 12)
b.add_node(b.root, 60)
b.add_node(b.root, 95)
b.print_in_order(b.root)
print('-'*50)
b.print_pre_order(b.root)
print('-'*50)
b.print_post_order(b.root)