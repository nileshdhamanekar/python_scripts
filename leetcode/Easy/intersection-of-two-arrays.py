# https://leetcode.com/problems/intersection-of-two-arrays/submissions/
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = dict()
        for num1 in nums1:
            result[num1] = 0
        for num2 in nums2:
            if num2 in result.keys():
                result[num2] += 1
        return [key for key in result.keys() if result[key] > 0]