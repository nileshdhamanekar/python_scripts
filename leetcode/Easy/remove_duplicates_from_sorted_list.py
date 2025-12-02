# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Pythonic way:
# myList = sorted(set(myList))

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    j = i+1
    if len(nums) == 1:
        return 1
    if not nums:
        return 0
    while j != len(nums):
        print(i, j, nums)
        print('*'*50)
        if nums[i] < nums[j]:
            temp = nums[i+1]
            nums[i+1] = nums[j]
            nums[j] = temp
            i += 1
        j += 1
    return i+1


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
# print(removeDuplicates([]))
# print(removeDuplicates([0]))
# print(removeDuplicates([0,1,2,3,4]))
# print(removeDuplicates([0,0,0,0,0]))
# print(removeDuplicates([0,0,1,1,2,2,3,3,4,4]))
