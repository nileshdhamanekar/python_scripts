# https://leetcode.com/problems/asteroid-collision/
class Stack:
    def __init__(self):
        self.stack_list = list()
    
    def push(self, item):
        self.stack_list.append(item)
        
    def pop(self):
        self.stack_list.pop()
        
    def is_empty(self):
        if len(self.stack_list) == 0:
            return True
        else:
            return False

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Doesn't work in case of input = [-2,1,-2,-2]
        # remaining_list = list()
        # if len(asteroids) == 1:
        #     return asteroids
        # i = 1
        # while i <= len(asteroids)-1:
        #     if asteroids[i-1] > 0 and asteroids[i] > 0:
        #         remaining_list.append(asteroids[i-1])
        #         if i == len(asteroids)-1:
        #             remaining_list.append(asteroids[i])
        #         i += 1
        #     elif (asteroids[i-1] < 0 and asteroids[i] < 0) or (asteroids[i-1] < 0 and asteroids[i] > 0):
        #         remaining_list.append(asteroids[i-1])
        #         if i == len(asteroids)-1:
        #             remaining_list.append(asteroids[i])
        #         i += 1
        #     elif asteroids[i-1] > 0 and asteroids[i] < 0:
        #         if asteroids[i-1] + asteroids[i] == 0:
        #             i += 2
        #         elif abs(asteroids[i-1]) > abs(asteroids[i]):
        #             remaining_list.append(asteroids[i-1])
        #             i += 2
        #         else:
        #             remaining_list.append(asteroids[i])
        #             remaining_list = self.asteroidCollision(remaining_list)
        #             i += 1
        #     continue
        # return remaining_list
        
        # Option 2: Using stack
        # Source: https://www.youtube.com/watch?v=5AV33YdtDYw
        i = 0
        stack = Stack()
        while i < len(asteroids):
            if asteroids[i] > 0:
                stack.push(asteroids[i])
            else:
                while not stack.is_empty() and stack.stack_list[-1] > 0 and abs(stack.stack_list[-1]) < abs(asteroids[i]):
                    stack.stack_list.pop()
                if stack.is_empty() or stack.stack_list[-1] < 0:
                    stack.push(asteroids[i])
                elif stack.stack_list[-1] == abs(asteroids[i]):
                    stack.pop()
            i += 1
        return stack.stack_list
            