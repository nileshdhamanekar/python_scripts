# https://leetcode.com/problems/maximum-subarray
# Resource: https://www.youtube.com/watch?v=5WZl3MMT0Eg
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = float('-inf')
        for num in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += num
            max_sum = max(max_sum, current_sum)
        return max_sum
        