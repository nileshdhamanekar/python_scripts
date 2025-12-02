# https://leetcode.com/problems/bag-of-tokens/
# Reference: https://www.youtube.com/watch?v=1GubKefOabc
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens = sorted(tokens)
        points = i = max_points = 0
        j = len(tokens) - 1
        while i <= j:
            if power >= tokens[i]:
                power -= tokens[i]
                points += 1
                i += 1
                max_points = max(points, max_points)
            elif points > 0:
                power += tokens[j]
                points -= 1
                j -= 1
            else:
                return max_points
        return max_points