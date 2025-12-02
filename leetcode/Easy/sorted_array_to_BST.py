# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/submissions/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        mid = int(len(nums)/2)
        node = TreeNode(nums[mid])
        if len(nums) <= 2:
            if len(nums) == 2:
                node.left = TreeNode(nums[0])
            return node
        node.left = self.sortedArrayToBST(nums[0:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:len(nums)])
        return node