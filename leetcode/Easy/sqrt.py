# https://leetcode.com/problems/sqrtx/submissions/
class Solution:
    def mySqrt(self, num: int) -> int:
        if num <= 1:
            sqrt = num
        else:
            # Binary search to find sqrt.
            # e.g. sqrt of 90 --> 90/2=45, 45/2=22, 22/2=11, 11/2=5
            # Then for i in range(5, num/2) check each number
            sqrt = int(num/2)
            while sqrt*sqrt > num:
                sqrt = int(sqrt/2)
            for i in range(int(sqrt), int(num/2)):
                if i*i <= num:
                    sqrt = i
                else:
                    sqrt = i - 1
                    break
        return int(sqrt)