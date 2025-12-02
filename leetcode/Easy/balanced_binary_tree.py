# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # This is approach 1
    # Approach 2 TBD. Refer Solutions section in Leetcode to do bottom up recursion to avoid calculating height repeatatively 
    def height(self, root: TreeNode) -> int:
        if root == None:
            return -1
        else:
            return max(self.height(root.left), self.height(root.right)) + 1
        
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return abs(self.height(root.left) - self.height(root.right)) < 2 and \
            self.isBalanced(root.left) and self.isBalanced(root.right)
        
            
            
        