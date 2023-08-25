# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]class ListNode(object):
def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()  # Create a dummy node to simplify list construction
        current = dummy  # Pointer to the current node in the merged list

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach any remaining nodes from either list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next 