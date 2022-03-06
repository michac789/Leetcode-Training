"""
Leetcode Problem 0021
Difficulty: Easy
Runtime: 26ms (79.58% faster)
Memory usage: 13.1MB (99.50% less)

Description:
Given the heads of two sorted linked list, merge into one sorted list.
"""

from cv2 import merge


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        output = "ListNode: "
        output = output + str(self.val) + " -> "
        node = self.next
        while node:
            output = output + str(node.val) + " -> "
            node = node.next
        output = output[:-4:]
        return output

def mergeTwoLists(list1, list2):
    curr1 = list1
    curr2 = list2
    curr_new = ListNode("x", None)
    head = curr_new
    while curr1 and curr2:
        if curr1.val < curr2.val:
            curr_new.next = curr1
            curr1 = curr1.next
        else:
            curr_new.next = curr2
            curr2 = curr2.next
        curr_new = curr_new.next
    if not curr1: curr_new.next = curr2
    else: curr_new.next = curr1
    return head.next

def setUp():
    next_val = None
    for i in [i for i in [5, 2, -1, -5, -5, -7]]:
        new_node = ListNode(i, next_val)
        next_val = new_node
    ll1 = new_node
    next_val = None
    for i in [i for i in [1, -2, -3, -4]]:
        new_node = ListNode(i, next_val)
        next_val = new_node
    ll2 = new_node
    return ll1, ll2

if __name__ == "__main__":
    ll1, ll2 = setUp()
    print(ll1)
    print(ll2)
    result = mergeTwoLists(ll1, ll2)
    print(result)
