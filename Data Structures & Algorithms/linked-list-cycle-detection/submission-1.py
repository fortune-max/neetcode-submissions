# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hare = head; tortoise = head
        while hare:
            hare = hare.next
            if not hare:
                return False
            hare = hare.next

            tortoise = tortoise.next
            if hare == tortoise:
                return True
        return False
