# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:

        dummy = ListNode(next = head)
        left_pointer = dummy
        right_pointer = dummy

        for _ in range(n+1):
            right_pointer = right_pointer.next
        
        while right_pointer:
            left_pointer = left_pointer.next
            right_pointer = right_pointer.next

        point_none = left_pointer.next
        left_pointer.next = left_pointer.next.next
        point_none.next = None


        return dummy.next
        