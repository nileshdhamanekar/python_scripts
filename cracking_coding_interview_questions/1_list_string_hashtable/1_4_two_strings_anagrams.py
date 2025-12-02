# e.g. LISTEN and SILENT
# Option 1: Create 2 dictionaries one for each list_string and store count of each character and compare the count of keys in one dict to other
# Option 2: Sort the two strings and check if they are equal
def anagram(str1, str2):
	if len(str1) != len(str2):
		return False
	if sorted(str1) != sorted(str2):
		return False
	else:
		return True

print(anagram("LISTEN", "SILNT"))