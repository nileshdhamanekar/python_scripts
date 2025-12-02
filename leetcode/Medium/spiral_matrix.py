# https://leetcode.com/problems/spiral-matrix/submissions/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Approach 1: Ugly looking solution; Doesn't work for [[3],[2]] and wouldn't work for huge spirals
        # final_list = list()
        # i = j = 0
        # m = len(matrix)
        # n = len(matrix[0])
        # if m <= 1 or n<=1:
        #     return matrix[0]
        # while j<= n-1:
        #     final_list.append(matrix[i][j])
        #     j += 1
        # j-=1; i+=1
        # while i <= m-1:
        #     final_list.append(matrix[i][j])
        #     i += 1
        # i-=1; j-=1
        # while j >= 0:
        #     final_list.append(matrix[i][j])
        #     j -= 1
        # j+=1; i-=1
        # while i >= 1:
        #     final_list.append(matrix[i][j])
        #     i -= 1
        # i+=1; 
        # if n >= 3:
        #     for j in range(1, n-1):
        #         final_list.append(matrix[i][j])
        # return final_list
        
        # Approach 2: Now check the below one. Resource: https://www.youtube.com/watch?v=BdQ2AkaTgOA
        final_list = list()
        left = 0; top = 0
        right = len(matrix[0])-1
        bottom = len(matrix)-1
        matrix_size = len(matrix) * len(matrix[0])
        while len(final_list) < matrix_size:
            i = left
            while i <= right and len(final_list) < matrix_size:
                final_list.append(matrix[left][i])
                i+=1
            top +=1
            i = top
            while i <= bottom and len(final_list) < matrix_size:
                final_list.append(matrix[i][right])
                i += 1
            right -= 1
            i = right
            while i >= left and len(final_list) < matrix_size:
                final_list.append(matrix[bottom][i])
                i -= 1
            bottom -= 1
            i = bottom
            while i >= top and len(final_list) < matrix_size:
                final_list.append(matrix[i][left])
                i -= 1
            left +=1
        return final_list