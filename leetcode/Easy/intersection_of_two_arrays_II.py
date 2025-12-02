# https://leetcode.com/problems/intersection-of-two-arrays/
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_dict = dict()
        output = list()
        for num1 in nums1:
            nums_dict[num1] = nums_dict.get(num1, 0) + 1
        for num2 in nums2:
            if num2 in nums_dict and nums_dict[num2] != 0:
                nums_dict[num2] -= 1
                output.append(num2)
        return output