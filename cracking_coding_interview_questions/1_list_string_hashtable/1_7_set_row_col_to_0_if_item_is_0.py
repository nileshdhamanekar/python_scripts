def entire_row_col_0(my_list):
	found_pairs = []
	for row in range(0, len(my_list)):
		for col in range(len(my_list[0])):
			if my_list[row][col] == 0:
				found_pairs.append((row,col))

	print(found_pairs)

	for pair in found_pairs:
		row, col = pair
		for i in range(len(my_list[0])):
			my_list[row][i] = 0
		for j in range(len(my_list)):
			my_list[j][col] = 0

	return(my_list)

my_list = [[1,2,0],
		   [4,5,6],
		   [7,0,9]
		  ]

print(entire_row_col_0(my_list))

# Link: https://stackoverflow.com/questions/40072787/if-an-element-in-an-mxn-matrix-is-0-its-entire-row-and-column-is-set-to-0