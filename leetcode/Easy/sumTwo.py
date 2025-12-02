def sumTwo(nums, target):
	# Time complexity: O(n*n) --> n square
	for index, item in enumerate(nums):
		diff = target-item
		if diff in nums:
			if nums.index(diff) != index:
				return [index, nums.index(diff)]


def sumTwo_Optimized(nums, target):
	# Time complexity:O(log n)
	# Because dictionary lookup is constant time (instant) --> log(1)
	my_dict = dict()
	for i in range(len(nums)):
		second_number = target - nums[i]
		if second_number in my_dict.keys():
			second_index = nums.index(second_number)
			if i != second_index:
				return sorted([i, second_index])
		else:
			my_dict.update({nums[i]: i})

print(sumTwo_Optimized([2,5,9,10], 11))