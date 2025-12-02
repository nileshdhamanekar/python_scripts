# https://leetcode.com/problems/find-common-characters/
# Probably slowest but easy to read, self solved
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        final_list = list()
        char_dict = dict()
        for i, item in enumerate(A):
            for s in item:
                if s not in char_dict.keys():
                    char_dict[s] = dict({i: 1})
                elif i not in char_dict[s].keys():
                    char_dict[s][i] = 1
                else :
                    char_dict[s][i] += 1
        for char in char_dict.keys():
            if len(char_dict[char].keys()) == len(A):
                min_count = float('inf')
                for key in char_dict[char].keys():
                    min_count = min(char_dict[char][key], min_count)
                for i in range(min_count):
                    final_list.append(char)
        return final_list