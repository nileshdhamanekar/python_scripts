def remove_dups_from_list(myList):
	unique_list = list()
	for item in myList:
		if item not in unique_list:
			unique_list.append(item)
	return unique_list

print(remove_dups_from_list([1, 2, 1, 5, 2]))

