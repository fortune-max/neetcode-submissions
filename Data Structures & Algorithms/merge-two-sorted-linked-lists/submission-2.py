# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def node_min(list1: Optional[ListNode], list2: Optional[ListNode]) -> (int, int):
    # return smaller ListNode, 0 or 1
    if not list2:
        return list1, 0
    elif not list1:
        return list2, 1
    if list1.val <= list2.val:
        return list1, 0
    return list2, 1

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        elif not list2: return list1

        lst, idx = node_min(list1, list2)
        head = lst; curr = head

        if idx == 0: list1 = list1.next
        else: list2 = list2.next

        while list1 or list2:
            lst, idx = node_min(list1, list2)
            curr.next = lst
            curr = curr.next
            if idx == 0: list1 = list1.next
            else: list2 = list2.next

        return head
