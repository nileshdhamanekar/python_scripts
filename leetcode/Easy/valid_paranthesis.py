class Solution:
    def isValid(self, s: str) -> bool:
        matching_brackets = {"]": "[", 
                             ")": "(", 
                             "}": "{"
                             }
        s_stack = list()
        for char in s:
            if char in matching_brackets.values():
                s_stack.append(char)
            elif len(s_stack) > 0 and matching_brackets[char] == s_stack[-1]:
                s_stack.pop()
            else:
                return False
        if len(s_stack) > 0:
            return False
        else:
            return True
