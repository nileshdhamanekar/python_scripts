def rotate_matrix(my_list):
	# First get transpose of a matrix
	print(my_list)
	n = len(my_list[0])
	print(n)
	for row in range(n):
		print("current row: {0}".format(my_list[row]))
		for col in range(row, n):
			print("Current item: {0}".format(my_list[row][col]))
			my_list[col][row], my_list[row][col] = my_list[row][col], my_list[col][row]
			print("Current state: {0}".format(my_list))
		print("Completed one row. Current state:{0}".format(my_list))

	for row in range(0, n):
		my_list[row].reverse()

	return(my_list)

my_list = [[1,2,3],
		   [4,5,6],
		   [7,8,9]
		  ]
print(rotate_matrix(my_list))

#Link: https://www.youtube.com/watch?v=kd5u3GEQkPY
