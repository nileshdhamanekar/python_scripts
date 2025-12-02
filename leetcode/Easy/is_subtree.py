# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# This solution doesn't work if first tree has duplicate values inside it. Needs to be fixed.
class Solution:
    def isSubtree(self, p1: TreeNode, p2: TreeNode) -> bool:
        if p1 is None and p2 is None:
            return True
        while p1 != None and p2 != None:
            if p1.val == p2.val:
                return self.isSubtree(p1.left, p2.left) and self.isSubtree(p1.right, p2.right)
            else:
                return self.isSubtree(p1.left, p2) or self.isSubtree(p1.right, p2)
        else:
            return False
        return True