def str_has_unique_chars(my_str):
	chars = set() # Using set because sets by default store unique values and have O(1) on membership test compared to list
	for char in my_str:
		if char in chars:
			return False
		else:
			chars.add(char) #Sets have add(), not append() like list
	return True

def str_has_unique_chars2(my_str)
	my_dict = dict()
	for char in my_str:
		if my_dict.has_key(char):
			return False
		else:
			my_dict[char] = 1
	else:
		return True

print(str_has_unique_chars2("abcd"))
print(str_has_unique_chars2("abbd"))