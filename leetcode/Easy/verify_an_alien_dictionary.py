# https://leetcode.com/problems/verifying-an-alien-dictionary/
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        i = j = k = 0
        previous = words[0]
        for item in range(1, len(words)):
            current = words[item]
            while i < len(current) and j < len(previous) and current[i] == previous[j] :
                i += 1
                j += 1
            if j >= len(previous):
                return True
            if i >= len(current):
                return False
            curr_index = prev_index = -1
            while curr_index == -1 or prev_index == -1:
                if j < len(previous) and previous[j] == order[k]:
                    prev_index = k
                if i < len(current) and current[i] == order[k]:
                    curr_index = k
                k += 1
            if prev_index > curr_index:
                return False
            previous = current
            i = j = k = 0
        return True