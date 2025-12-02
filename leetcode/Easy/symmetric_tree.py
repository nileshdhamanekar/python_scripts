# https://leetcode.com/problems/symmetric-tree/
# Reference: https://www.youtube.com/watch?v=K7LyJTWr2yA
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.isMirror(root, root)
    
    def isMirror(self, t1: TreeNode, t2: TreeNode):
        if t1 == None or t2 == None:
            return t1 == t2
        if t1.val != t2.val:
            return False
        return self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)