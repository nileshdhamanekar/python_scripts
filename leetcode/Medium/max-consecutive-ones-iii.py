# Resource: https://www.youtube.com/watch?v=FQH1xNZz0tg&t=602s
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroes = start = res = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                zeroes += 1
            while zeroes > k:
                if nums[start] == 0:
                    zeroes -= 1
                start += 1
            res = max(res, end - start +1)
        return res