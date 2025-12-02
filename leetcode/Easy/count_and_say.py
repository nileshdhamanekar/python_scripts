# https://leetcode.com/problems/count-and-say/

# def countAndSay(n):
#     """
#     :type n: int
#     :rtype: str
#     """
#     current_str = "11"
#     if n <= 2:
#         return current_str[0:n]
#     global_pointer = 0
#     for i in range(2, n):
#         print("Inside for")
#         new_str = ""
#         count = 0
#         while global_pointer != len(current_str) - 1:
#             print("Inside first while")
#             while current_str[global_pointer] != current_str[global_pointer+1]:
#                 print("Inside second while")
#                 count += 1
#                 global_pointer += 1
#             new_str = new_str + count * current_str[global_pointer]
#             global_pointer += 1
#             if global_pointer <= current_str[-2]:
#                 new_str
#         current_str = new_str
#     return current_str

import itertools
def countAndSay(n):
    new_value = ''
    value = "11"
    for digit, group in itertools.groupby(value):
        count = sum(1 for _ in group)
        new_value += str(count) + digit
    return new_value
print(countAndSay(5))