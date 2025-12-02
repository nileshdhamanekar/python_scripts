# https://leetcode.com/problems/climbing-stairs/
# Resource 1 (Most optimized version Tushar): https://www.youtube.com/watch?v=cETfFsSTGJI
# Resource 2 Code dojo: https://www.youtube.com/watch?v=5o-kdjv7FD0
class Solution:
    def climbStairs(self, num: int) -> int:
        # Solution 1: Slow version, re-calculates same value again and again, Time Limit Exceeded
        # if num == 0:
        #     return 1
        # if num == 1:
        #     return 1
        # return self.climbStairs(num-1) + self.climbStairs(num-2)
        
        # Solution 2: Dynamic Programming version which stores sum of previous numbers:
        n1 = 0
        n2 = 1
        sum = 0
        if n1 == num or n2 == num:
            return num
        for i in range(0,num):
            sum = n1 + n2
            n1 = n2
            n2 = sum
        return sum        