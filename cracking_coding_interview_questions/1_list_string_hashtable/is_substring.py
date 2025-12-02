def is_substring(str1, str2):
	"""
	Without using "find", "in" or "index"
	"""
	for i in range(0, len(str1)):
		sum = 0
		for j in range(0, len(str2)):
			if str1[i+j] != str2[j]:
				break
			else:
				sum += 1
				if sum == len(str2):
					return(i)

print(is_substring("abacde", "e"))