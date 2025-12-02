# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Resource: https://www.youtube.com/watch?v=W5DzOFR_m9Y
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left == None and root.right == None:
            return 1
        min_depth = float('Inf')
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)
        return min_depth + 1