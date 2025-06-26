
"""reverse a linked list"""

#singly LL

class ListNode: 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    
class Solution:
    def iter(self, head: ListNode)-> ListNode:
        prev, curr = None, head
        
        while curr: # while curr is not null
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
            


class Solution_two:
    def iter(self, head: ListNode)-> ListNode:
        



# def recursively()