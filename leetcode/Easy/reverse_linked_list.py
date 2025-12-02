# https://leetcode.com/problems/reverse-linked-list
# Resource: https://www.youtube.com/watch?v=G0_I-ZF0S38&t=337s
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous, current = None, head
        while current != None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous