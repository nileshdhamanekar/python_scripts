# Simpler alternate solution:
# >>> l1 = [1, 3, 4, 7]
# >>> l2 = [0, 2, 5, 6, 8, 9]
# >>> l1.extend(l2)
# >>> sorted(l1)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def merge_sorted_lists(list1, list2):
	merged_list = list()
	while len(list1) > 0 and len(list2) > 0:
		if list1[0] < list2[0]:
			merged_list.append(list1.pop(0))
		else:
			merged_list.append(list2.pop(0))
		print(merged_list)
	merged_list.extend(list1+list2)
	return merged_list

list1 = [1,2,5,7]
list2 = [3,4,6,8,10,12]
print(merge_sorted_lists(list1, list2))