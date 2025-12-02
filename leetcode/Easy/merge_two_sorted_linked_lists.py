# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head_new = current = previous = None
        while l1 is not None or l2 is not None:
            if l1 is None and l2 is not None:
                current = ListNode(l2.val)
                l2 = l2.next
            elif l2 is None and l1 is not None:
                current = ListNode(l1.val)
                l1 = l1.next
            elif l1.val <= l2.val:
                current = ListNode(l1.val)
                l1 = l1.next
            else:
                current = ListNode(l2.val)
                l2 = l2.next
            if head_new is None:
                head_new = current
            else:
                previous.next = current
            previous = current
        return head_new