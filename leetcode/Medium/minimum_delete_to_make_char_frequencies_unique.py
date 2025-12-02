# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/submissions/
# Reference: https://www.youtube.com/watch?v=xzsAFSFiVF8
class Solution:
    def minDeletions(self, s: str) -> int:
        char_count = dict()
        for char in s:
            if char in char_count.keys():
                char_count[char] += 1
            else:
                char_count[char] = 1
        sorted_char_count = sorted([value for value in char_count.values()], reverse=True)
        min_delete = 0
        max_frequency = sorted_char_count[0] - 1
        for i in range(1, len(sorted_char_count)):
            if sorted_char_count[i] > max_frequency:
                min_delete += sorted_char_count[i] - max_frequency
                sorted_char_count[i] = max_frequency
            if max_frequency > 0:
                max_frequency = min(max_frequency, sorted_char_count[i] -1)
        return min_delete