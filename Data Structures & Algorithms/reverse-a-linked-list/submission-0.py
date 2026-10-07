# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_head = None
        while head:
            curr_head = ListNode(head.val, curr_head)
            head = head.next
        return curr_head