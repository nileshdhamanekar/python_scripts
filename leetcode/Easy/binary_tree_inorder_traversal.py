# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        tree_nodes = list()
        tree_nodes = self.traverse_inorder(root, tree_nodes)
        return tree_nodes
    
    def traverse_inorder(self, root, tree_nodes):
        if root != None:
            if root.left != None:
                tree_nodes = self.traverse_inorder(root.left, tree_nodes)
            tree_nodes.append(root.val)
            if root.right != None:
                tree_nodes = self.traverse_inorder(root.right, tree_nodes)
        return tree_nodes