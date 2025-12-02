# https://leetcode.com/problems/valid-parentheses/
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def print_stack(self):
        print(self.stack)


class MySolution():
    def __init__(self):
        self.my_stack = Stack()
        self.mapping = {
            "{": "}",
            "(": ")",
            "[": "]"
        }

    def get_key_by_value(self, value_to_search):
        for key, value in self.mapping.items():
            if value == value_to_search:
                return key
        else:
            return None

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for char in s:
            if char in self.mapping.keys():
                self.my_stack.push(char)
            else:
                if self.my_stack.stack and self.my_stack.stack[-1] == self.get_key_by_value(char):
                    self.my_stack.pop()
                else:
                    print("Mismatch! Current char:{0}, Stack:{1}".format(char, self.my_stack.print_stack()))
                    return False
        if len(self.my_stack.stack) != 0:
            self.my_stack.print_stack()
            return False
        else:
            return True


s = MySolution()
# print(s.isValid(""))
# print(s.isValid("()"))
# print(s.isValid("{}"))
# print(s.isValid("[]"))
# print(s.isValid("(){}[]"))
# print(s.isValid("(((())))"))
# print(s.isValid("({[]})"))
# print(s.isValid("((]}))"))
print(s.isValid(")"))
print(s.isValid("abcd"))
