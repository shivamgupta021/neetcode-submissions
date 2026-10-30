# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        while current != None:
            # save the link that we are going to break
            next_node = current.next
            # move the link to prev node
            current.next = previous
            # now that is linked, move previous to current
            previous = current
            # move ahead the current
            current = next_node
        
        return previous