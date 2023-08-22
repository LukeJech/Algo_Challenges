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
# Output: [0]
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Start with the first value as the head
# Check next in the list if it's less than or greater than
# If less than, add to front of the list, new head
# If it's greater then add to back of the list
def mergeTwoLists(list1, list2):
    head = ListNode(list1[0])
    runner = head
    for i in range(1,len(list1)):
        runner.next = ListNode(list1[i])
        runner = runner.next
    
    runner = head 
    for num in list2:
        newNode = ListNode(num)
        while(True):
            if (runner.val == newNode.val):
                newNode.next = runner.next
                runner.next = newNode
                runner = runner.next
                break
            elif (runner.val < newNode.val):
                if (runner.next == None):
                    runner.next = newNode

                    break
                else:
                    runner = runner.next
                    continue
            else:
                newNode.next = runner.next
                runner.next = newNode
                break
    return head









test = mergeTwoLists([1,2,4], [1,3,4])
runner = test
while (test.next):
    print(runner.val)
    runner = runner.next
