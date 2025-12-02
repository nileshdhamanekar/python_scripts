# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        carry = 0
        l3_head = l3_current = None 
        while l1 != None or l2 != None:
            current_sum = 0
            if l1 is not None:
                current_sum += int(l1.val)
                l1 = l1.next
            if l2 is not None:
                current_sum += int(l2.val)
                l2 = l2.next
            current_sum += carry
            carry = 0
            if current_sum >= 10:
                carry = current_sum//10
                current_sum %= 10
            new_node = ListNode(current_sum)
            if l3_head == None:
                l3_head = l3_current = new_node
            else:
                l3_current.next = new_node
                l3_current = new_node
        if carry != 0:
            new_node = ListNode(carry)
            l3_current.next = new_node
        return l3_head