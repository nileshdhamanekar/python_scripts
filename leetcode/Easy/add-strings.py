# https://leetcode.com/problems/add-strings/
# Was able to solve by myself

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        addition = ""
        carry = current_sum = 0
        i, j = len(num1)-1, len(num2)-1
        while i >=0 or j >= 0:
            if i>= 0:
                current_sum += int(num1[i])
            if j>= 0:
                current_sum += int(num2[j])
            current_sum += carry
            carry = 0
            if current_sum >= 10:
                carry = current_sum // 10
                current_sum = current_sum % 10
            addition = "{0}{1}".format(str(current_sum), addition)
            current_sum = 0
            i -=1
            j -= 1
        if carry > 0:
            addition = "{0}{1}".format(str(carry), addition)
        return addition