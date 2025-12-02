# https://leetcode.com/problems/house-robber-iii/
# No resource

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        # Why doesn't this approach work for: [2,1,3,null,4]
        # Ans: 4+3 = 7 is the optimal answer since they are not connected directly
        rob1 = temp = sum_nodes = 0
        if root is None:
            return 0
        current_nodes = [root]
        rob2 = root.val
        while current_nodes:
            new_nodes = list()
            for node in current_nodes:
                if node.left:
                    sum_nodes += node.left.val
                    new_nodes.append(node.left)
                if node.right:
                    sum_nodes += node.right.val
                    new_nodes.append(node.right)
            temp = max(rob2, rob1 + sum_nodes)
            rob1 = rob2
            rob2 = temp
            sum_nodes = 0
            current_nodes = new_nodes
        return rob2
            