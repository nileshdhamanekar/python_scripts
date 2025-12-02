# https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        previous = head
        current = head.next
        while current.next != None:
            if current.val == previous.val:
                current = current.next
                previous.next = current
            else:
                previous.next = current
                previous = current
                current = current.next
        if current.next == None and previous.val == current.val:
            previous.next = None
        return head