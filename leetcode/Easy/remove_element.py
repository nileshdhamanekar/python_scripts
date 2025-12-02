# https://leetcode.com/problems/remove-element/


def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    if not nums:
        print("List is None")
        return -1
    i = 0
    j = len(nums) - 1
    print(nums)
    if len(nums) == 1 and val in nums:
        return None
    while i <= j:
        print(nums)
        while nums[j] == val and i < j:
            j -= 1
        print("Settled j at {0}".format(j))
        if i < j:
            if nums[i] == val:
                print("swapping")
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                print("After swapping: {0}".format(nums))
                j -= 1
        else:
            break
        i += 1
    return i + 1


def removeElementPythonic(nums, val):
    nums = [x for x in nums if x != val]
    return len(nums)

def removeElementPythonic2(nums, val):
    while nums.count(val) >  0:
        nums.remove(val)
    return len(nums)

# print(removeElement([3,2,2,3], 3))
# print(removeElement([0,1,2,2,3,0,4,2],2))
# print(removeElement([3],2))
# print(removeElement([2],2))
# print(removeElement([],2))
# print(removeElement(None,2))
# print(removeElement([3,2],2))
# print(removeElement([2,3],2))
# print(removeElement([3,3],2))
# print(removeElement([2,3,3],2))
# print(removeElement([3,3,3],2))

print(removeElementPythonic([3,2,2,3,3,3],2))

print(removeElementPythonic2([3,2,2,3,3,3],2))