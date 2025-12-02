# https://leetcode.com/problems/first-missing-positive/
# Reference: https://www.youtube.com/watch?v=-lfHWWMmXXM&t=741s

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        correct_pos = 0
        n = len(nums)
        for i in range(n):
            correct_pos = nums[i] - 1
            while 1 <= nums[i] <= n and nums[i] != nums[correct_pos]:
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
                correct_pos = nums[i] - 1
        for i in range(n):
            if i+1 != nums[i]:
                return i+1
        return n+1