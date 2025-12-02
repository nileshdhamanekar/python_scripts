#https://leetcode.com/problems/reverse-words-in-a-string/
class Solution:
    def reverseWords(self, s: str) -> str:
        # One liner Python:
        # return " ".join(reversed(s.split()))
        reverse_str = ""
        if len(s) == 0:
            return s
        last_index = len(s)
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                if i!= len(s)-1 and s[i+1] != " ":
                    reverse_str += s[i+1:last_index]
                    reverse_str += " "
                last_index = i
            else:
                continue
        if last_index >= 0:
            reverse_str += s[0:last_index]
        return reverse_str.strip()