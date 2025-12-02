def reverse_string(my_str):
	new_str = ""
	for i in range(len(my_str)-1,-1,-1):
		new_str += my_str[i]
	return new_str

print(reverse_string("abcde"))
