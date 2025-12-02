# https://leetcode.com/problems/pascals-triangle-ii/
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        master_list = list([[1]])
        prev_list = list([1])
        for i in range(1, rowIndex+1):
            current_list = list([1])
            for j in range(0, len(prev_list)-1):
                current_list.append(prev_list[j] + prev_list[j+1])
            current_list.append(1)
            master_list.append(current_list)
            prev_list = current_list
        return prev_list