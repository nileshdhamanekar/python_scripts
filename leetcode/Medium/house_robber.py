# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = rob2 = 0
        # Dynamic Programming. Source: https://www.youtube.com/watch?v=73r3KWiEvyk
        for num in nums:
            temp = max(rob2, num+rob1)
            rob1 = rob2
            rob2 = temp
        return rob2