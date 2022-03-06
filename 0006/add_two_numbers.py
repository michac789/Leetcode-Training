"""
Leetcode Problem 0006
Difficulty: Medium
Runtime: 60ms (86.21% faster)
Memory usage: 13.3MB (90.68% less)

Description:
Given two non-empty linked lists representing two non-negative integers
in reversed order, with each node containing a single digit, add the numbers
and return the sum as a linked list (also in reverse order).
"""

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
    
def addTwoNumbers1(l1, l2):
    curr1 = l1
    curr2 = l2
    num = -1
    first_node = ListNode(num)
    prev_node = first_node
    while(curr1 or curr2):
        num = (1 if num >= 10 else 0)
        if curr1: num += curr1.val
        if curr2: num += curr2.val
        new_node = ListNode(num % 10)
        prev_node.next = new_node
        prev_node = new_node
        if curr1: curr1 = curr1.next
        if curr2: curr2 = curr2.next
    if num >= 10:
        new_node = ListNode(1)
        prev_node.next = new_node
    return first_node.next

def addTwoNumbers2(l1, l2):
    curr = l1
    num1 = ""
    while curr:
        num1 = str(curr.val) + num1
        curr = curr.next
    curr = l2
    num2 = ""
    while curr:
        num2 = str(curr.val) + num2
        curr = curr.next
    add = str(int(num1) + int(num2))
    next_node = None
    for char in add:
        new_node = ListNode(int(char), next_node)
        next_node = new_node
    return next_node

def setUp():
    next_val = None
    for i in [3, 4, 2]:
        new_node = ListNode(i, next_val)
        next_val = new_node
    ll1 = new_node
    next_val = None
    for i in [4, 6, 5]:
        new_node = ListNode(i, next_val)
        next_val = new_node
    ll2 = new_node
    return ll1, ll2

if __name__ == "__main__":
    ll1, ll2 = setUp()
    result1 = addTwoNumbers1(ll1, ll2)
    print(result1)
    result2 = addTwoNumbers2(ll1, ll2)
    print(result2)
