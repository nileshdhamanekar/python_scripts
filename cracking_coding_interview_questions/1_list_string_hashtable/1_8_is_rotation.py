def is_rotation(str1, str2):
   #  1. Create a temp list_string and store concatenation of str1 to
   # str2 in temp.
   #                    temp = str1.str1
   #  2. If str2 is a substring of temp then str1 and str2 are 
   #     rotations of each other.

   #  Example:                 
   #                   str1 = "ABACD"
   #                   str2 = "CDABA"

     temp = str1.str1 = "ABACDABACD"
     Since str2 is a substring of temp, str1 and str2 are 
     rotations of each other.
	if len(str1) != len(str2):
		return False
	else:
		temp = str1 + str1
		if str2 in temp:
			return True
		else:
			return False