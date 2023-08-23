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
    head = list1
    runner = head
    runner2 = list2
    i = 1
    while(runner2):
        print(i, runner.val, runner2.val, head)
        i += 1
        if (runner.val == runner2.val):
            temp = runner2.next
            runner2.next = runner.next
            runner.next = runner2
            runner = runner.next
            runner2 = temp
            continue
        elif (runner.val < runner2.val):
            if (runner.next == None):
                runner.next = runner2
                runner2 = runner2.next
                continue
            elif(runner.next.val >= runner2.val):
                temp = runner2.next
                runner2.next = runner.next
                runner.next = runner2
                runner2 = temp
                continue
            else:
                runner = runner.next
                continue
        else:
            temp = runner2.next
            runner2.next = runner
            if (runner2.val < head.val ):
                head = runner2
                runner = head
            runner2 = temp
            
    return head









test = mergeTwoLists([1,2,4], [1,3,4])
runner = test
while (runner):
    print(runner.val)
    runner = runner.next
