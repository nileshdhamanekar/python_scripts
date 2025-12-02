# https://leetcode.com/problems/shortest-way-to-form-string/
# Resource: https://www.youtube.com/watch?v=evesA3gr9BE
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        i = j = num_subsequences = 0
        while i < len(target):
            j = 0
            subsequence = ""
            while j < len(source) and target[i] != source[j]:
                j += 1
            while i < len(target) and j < len(source):
                if target[i] == source[j]:
                    subsequence += target[i]
                    i += 1
                    j += 1
                else:
                    j += 1
            if len(subsequence) == 0:
                return -1
            else:
                num_subsequences += 1
        return num_subsequences