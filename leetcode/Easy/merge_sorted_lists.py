# https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # This solution doesn't work on Leedcode for nums1=[0], nums2=[1], m=0, n=1
        # And also isn't optimal due to use of pop() and extend()
        # if n == 0:
        #     return nums1
        # if m == 0:
        #     nums1 = nums2
        #     return nums1
        # i = j = 0
        # while i < m and j < n:
        #     if nums1[i] >= nums2[j]:
        #         nums1.insert(i, nums2[j])
        #         j+=1
        #     else:
        #         i+=1
        # while nums1[-1] == 0:
        #     nums1.pop()
        # nums1.extend(nums2[j:])
        # return nums1
        
        # Using 3 pointers
        # Time O(n), Space O(1) because no additinal list is requried to store the result
        last = m + n -1
        while m > 0 and n > 0:
            if nums1[m-1] < nums2[n-1]:
                nums1[last] = nums2[n-1]
                n -= 1
            else:
                nums1[last] = nums1[m-1]
                m -= 1
            last -= 1
        while n > 0:
            nums1[last] = nums2[n-1]
            last, n = last-1, n-1
        return nums1
        