"""
Leetcode Problem 0016
Difficulty: Medium
Runtime: 20ms (87.35% faster)
Memory usage: 13.3MB (91.33% less)

Description:
Given the head of a linked list, remove the nth node from the end.
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

def removeNthFromEnd(head, n):
    curr = head
    length = 0
    while curr:
        curr = curr.next
        length += 1
    if n == length:
        return head.next
    curr = head
    for i in range(length - n - 1):
        curr = curr.next
    curr.next = curr.next.next
    return head

def setUp():
    next_val = None
    for i in [i for i in range(5, 0, -1)]:
        new_node = ListNode(i, next_val)
        next_val = new_node
    ll = new_node
    return ll

if __name__ == "__main__":
    head = setUp()
    print(head)
    result = removeNthFromEnd(head, 2)
    print(result)
