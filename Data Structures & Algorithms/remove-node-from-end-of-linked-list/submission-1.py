# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail = head
        size = 1

        while tail and tail.next:
            size += 1
            tail = tail.next

        target = size - n

        if target == 0:
            return head.next

        ctr = 1
        current = head

        while ctr < target:
            current = current.next
            ctr += 1

        current.next = current.next.next

        return head