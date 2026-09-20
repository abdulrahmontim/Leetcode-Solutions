# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        # using merge two list method, trying to divide and conquer
        ll_size = len(lists)

        merged_list = ListNode(val=-float("inf"))
        curr_merged_list = merged_list
        
        for ll in lists:
            curr_merged_list = self.mergeTwoLists(curr_merged_list, ll)
        
        return merged_list.next

    
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        curr_list = dummy

        curr_list1 = list1
        curr_list2 = list2

        while (curr_list1 and curr_list2):
            if curr_list1.val <= curr_list2.val:
                curr_list.next = curr_list1
                curr_list1 = curr_list1.next
            else:
                curr_list.next = curr_list2
                curr_list2 = curr_list2.next

            curr_list = curr_list.next

        if curr_list1:
            curr_list.next = curr_list1
        if curr_list2:
            curr_list.next = curr_list2
        
        return dummy.next
            