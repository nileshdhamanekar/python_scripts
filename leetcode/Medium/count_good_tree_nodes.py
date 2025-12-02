# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Medium problem Solved myself within 30 mins with all tests passing on Leetcode :-)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            return self.good_nodes(root, 0, root.val)
        
    def good_nodes(self, node, count, max_val):
        if node.val >= max_val:
            count += 1
            max_val = node.val
        if node.left:
            count = self.good_nodes(node.left, count, max_val)
        if node.right:
            count = self.good_nodes(node.right, count, max_val)
        return count