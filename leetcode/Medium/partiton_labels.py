# https://leetcode.com/problems/partition-labels/
# Resource: https://www.youtube.com/watch?v=ED4ateJu86I
# Time: O(n+n) = O(n)
# Space: O(n)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = dict()
        partitions = list()
        for i in range(len(s)):
            last_index[s[i]] = i
        i = 0
        while i < len(s):
            end = last_index[s[i]]
            j = i
            while j != end:
                end = max(end, last_index[s[j]])
                j += 1
            partitions.append(j - i + 1)
            i = j + 1
        return partitions