# https://leetcode.com/problems/string-compression/

# Resource: https://www.youtube.com/watch?v=IhJgguNiYYk
class Solution:
    def compress(self, chars: List[str]) -> int:
        i = index = 0
        current = ""
        while i < len(chars):
            j = i
            while j < len(chars) and chars[i] == chars[j]:
                j += 1
            chars[index] = chars[i]
            index += 1
            if j - i > 1:
                for c in str(j-i):
                    chars[index] = c
                    index += 1
            i = j
        return index