"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# Source: https://www.youtube.com/watch?v=EHpS2TBfWQg&t=355s
# Code isn't working, needs fix. 
# Gives error: Random pointer of node with label 13 points to a node from the original list.
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        orig_current = orig_previous = head
        clone_head = clone_current = clone_previous = None
        while orig_current != None:
            clone_current = Node(orig_current.val)
            if clone_head == None:
                clone_head = clone_previous = clone_current
            else:
                orig_previous.next = clone_previous
                clone_previous.next = clone_current
                clone_previous.random = orig_previous
            orig_previous = orig_current
            orig_current = orig_current.next
            clone_previous = clone_current

        orig_current = head
        clone_current = clone_head
        while orig_current != None:
            if clone_current.random.random == None:
                clone_current.random = None
            else:
                clone_current.random = clone_current.random.random.next
            orig_current.next = orig_current.next.next.random
            orig_current = orig_current.next
            clone_current = clone_current.next
        return clone_head
            