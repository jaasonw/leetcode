# 21. Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a new list. The new list should
# be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # edge case
        if (l1 == None):
            return l2
        if (l2 == None):
            return l1
        output_head = None
        output_tail = None
        while (l1 != None and l2 != None):
            if (l1.val <= l2.val):
                if (output_head == None):
                    output_head = l1
                    output_tail = output_head
                else:
                    output_tail.next = l1
                    output_tail = l1
                l1 = l1.next
            else:
                if (output_head == None):
                    output_head = l2
                    output_tail = output_head
                else:
                    output_tail.next = l2
                    output_tail = l2
                l2 = l2.next
        if (l1 != None):
            output_tail.next = l1
        if (l2 != None):
            output_tail.next = l2
        return output_head

