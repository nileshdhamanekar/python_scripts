# https://leetcode.com/problems/max-consecutive-ones/submissions/
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        j = count = max_count = 0
        while j < len(nums):
            if nums[j] == 1:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 0
            j += 1
        return max(count, max_count)