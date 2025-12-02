# https://leetcode.com/problems/search-insert-position/


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if nums is None or len(nums) == 0:
        return 0
    position = None
    i = 0
    while i <= len(nums) - 1:
        if nums[i] == target or nums[i] > target:
            position = i
            break
        else:
            i += 1
    if position is None and nums[len(nums)-1] < target:
        position = len(nums)
    return position


# TODO: Solve using binary search

# print(searchInsert([1,3,5,6], 5))
# print(searchInsert([1,3,5,6], 2))
# print(searchInsert([1,3,5,6], 7))
# print(searchInsert([2,3,5,6], 1))
# print(searchInsert([], 5))
print(searchInsert([1], 0))
