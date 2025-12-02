# https://leetcode.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if any(c.isalpha() for c in s):
            return len(s.split()[-1])
        else:
            return 0