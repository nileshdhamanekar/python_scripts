def convert_to_base_9(count, char):
	encoded_str = ""
	while count > 9:
		encoded_str = encoded_str + "9" + char
		count -= 9
	encoded_str = encoded_str + str(count) + char
	return encoded_str

def run_length_encoding(my_str):
	if len(my_str) == 0:
		return None
	encoded_str = ""
	current_char = previous_char= my_str[0]
	count = 1
	for i in range(1, len(my_str)):
		if my_str[i] == current_char:
			count += 1
		else:
			encoded_str += convert_to_base_9(count, previous_char)
			count = 1
		current_char = previous_char = my_str[i]
	if count != 0:
		encoded_str += convert_to_base_9(count, current_char)
	return encoded_str

print(run_length_encoding("AAAAAAAAAAAABBCDDDDDDDDDD")) # 12A's 2B's 1C 10D's
print(run_length_encoding(""))
print(run_length_encoding("A"))
print(run_length_encoding("AAAAAAAAAAAAAAAAAAAA")) #20A's
print(run_length_encoding("ABBBBBBBBBBBBBBC")) # 14B's 