# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Solved on my own, haha!
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        telephone_dict = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }
        combinations = list()
        if len(digits) == 0:
            return combinations
        for i in range(len(digits)-1, -1, -1):
            if not combinations:
                combinations = telephone_dict[digits[i]]
            else:
                temp_list = list()
                for letter in telephone_dict[digits[i]]:
                    for combination in combinations:
                        temp_list.append("{0}{1}".format(letter, combination))
                combinations = temp_list
        return combinations