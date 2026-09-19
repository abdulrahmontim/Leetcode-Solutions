/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {

        ListNode* curr_list1 = list1;
        ListNode* curr_list2 = list2;
        ListNode* dummy_node = new ListNode();
        ListNode* curr_list = dummy_node;

        while (curr_list1 && curr_list2) {
            if (curr_list1->val <= curr_list2->val) {
                curr_list->next = curr_list1;
                curr_list1 = curr_list1->next;
            } else {
                curr_list->next = curr_list2;
                curr_list2 = curr_list2->next;
            }
            curr_list = curr_list->next;
        }

        if (curr_list1) curr_list->next = curr_list1;
        if (curr_list2) curr_list->next = curr_list2;

        
        return dummy_node->next;
        
    }
};