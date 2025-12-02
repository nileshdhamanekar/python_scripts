def remove_dups_from_string(my_str):
	unique_list = list()
	for ch in my_str:
		if ch not in unique_list:
			unique_list.append(ch)
	return ''.join(unique_list)

print(remove_dups_from_string("abbacd"))
