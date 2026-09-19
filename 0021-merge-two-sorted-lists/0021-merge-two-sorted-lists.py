# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        
        curr_list1 = list1
        curr_list2 = list2
        new_list = ListNode()
        curr_list = new_list

        while curr_list1 and curr_list2:
            if curr_list1.val <= curr_list2.val:
                curr_list.next = curr_list1
                curr_list1 = curr_list1.next
                curr_list = curr_list.next
            else:
                curr_list.next = curr_list2
                curr_list2 = curr_list2.next
                curr_list = curr_list.next
        
        if curr_list1 and not curr_list2:
            curr_list.next = curr_list1
        if curr_list2 and not curr_list1:
            curr_list.next = curr_list2
        
        return new_list.next

