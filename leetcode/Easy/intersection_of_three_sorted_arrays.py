# https://leetcode.com/problems/intersection-of-three-sorted-arrays/submissions/
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        result = dict()
        for num in arr1:
            result[num] = result.get(num, 0) + 1
        for num in arr2:
            result[num] = result.get(num,0) + 1
        for num in arr3:
            result[num] = result.get(num, 0) + 1
        return [key for key in result.keys() if result[key] >= 3]