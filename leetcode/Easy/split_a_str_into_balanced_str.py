# https://leetcode.com/problems/split-a-string-in-balanced-strings
# Easy one, was able to do it myself

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balanced_string_count = 0
        count = 0
        for i in range(0, len(s)):
            if s[i] == "L":
                count += 1
            if s[i] == "R":
                count -= 1
            if count == 0:
                balanced_string_count += 1
                count = 0
        return balanced_string_count