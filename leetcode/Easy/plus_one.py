# https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits)-1,-1,-1):
            if i == len(digits)-1:
                digits[i] = digits[i] + 1
            else:
                digits[i] = digits[i] + carry
                carry = 0
            if digits[i] >= 10:
                digits[i] = digits[i] % 10
                carry = 1
            if i == 0 and carry==1:
                if digits[0] == 0:
                    digits.insert(0,1)
                else:
                    digits[0] += carry
        return digits