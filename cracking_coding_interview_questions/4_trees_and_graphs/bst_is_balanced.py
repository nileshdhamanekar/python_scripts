# References:
# https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/
# https://youtu.be/qIdVVH1tKM4
# https://www.youtube.com/watch?v=_SiwrPXG9-g


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Height:
    def __init__(self):
        self.height = 0


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add_node(self, root, value):
        node = Node(value)
        if root is None:
            self.root = node
        elif root.value > value:
            if root.left is None:
                root.left = node
            else:
                self.add_node(root.left, value)
        elif root.value < value:
            if root.right is None:
                root.right = node
            else:
                self.add_node(root.right, value)

    def print_pre_order(self, node):
        if node is not None:
            print(node.value)
            self.print_pre_order(node.left)
            self.print_pre_order(node.right)

    def is_balanced(self, root, height):
        lh = Height()
        rh = Height()
        if root is None:
            return True
        l = self.is_balanced(root.left, lh)
        r = self.is_balanced(root.right, rh)
        height.height = max(lh.height, rh.height) + 1
        if abs(lh.height - rh.height) <= 1:
            return l and r
        return False

b = BinarySearchTree()
b.add_node(b.root, 42)
b.add_node(b.root, 23)
b.add_node(b.root, 83)
b.add_node(b.root, 40)
b.add_node(b.root, 12)
b.add_node(b.root, 60)
b.add_node(b.root, 95)
b.add_node(b.root, 100)
b.add_node(b.root, 105)
b.print_pre_order(b.root)
print('-'*50)
# to store the height of tree during traversal
height_main = Height()
if b.is_balanced(b.root, height_main):
    print('Tree is balanced')
else:
    print('Tree is not balanced')