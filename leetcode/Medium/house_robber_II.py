# https://leetcode.com/problems/house-robber-ii/
# Resource: https://www.youtube.com/watch?v=rWAJCfYYOvM

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[0:-1]))
        
    def helper(self, nums):
        rob1 = rob2 = 0
        for num in nums:
            temp = max(rob2, num+rob1)
            rob1 = rob2
            rob2 = temp
        return rob2