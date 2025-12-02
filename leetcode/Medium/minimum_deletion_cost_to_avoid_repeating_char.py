# https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        i = min_delete = 0
        max_temp = float('Inf')
        prev_char = ""
        while i < len(s):
            if s[i] == prev_char:
                min_delete += min(max_temp, cost[i])
                max_temp = max(max_temp, cost[i])
            else:
                prev_char = s[i]
                max_temp = cost[i]
            i += 1
        return min_delete