# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:

        curr_node = head
        prev_node = None

        while curr_node is not None:
            if curr_node.next is None:
                head = curr_node
            remaining_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = remaining_node

        return head