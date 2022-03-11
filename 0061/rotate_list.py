"""
Leetcode Problem 0061
Difficulty: Medium
Runtime: 20ms (97.02% faster)
Memory usage: 13.4MB (84.00% less)

Description:
Given the head of a linked list, rotate the list to the right by k places.
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

def rotateRight(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if not head: return
    curr = head
    length = 1
    while curr.next:
        length += 1
        curr = curr.next
    n = length - k % length
    if n == length:
        return head
    curr.next = head
    curr = head
    for i in range(n):
        if i == n - 1: prev = curr
        curr = curr.next
    head = curr
    prev.next = None
    return head

def setUp():
    next_val = None
    for i in [1, 2, 3, 4, 5]:
        new_node = ListNode(i, next_val)
        next_val = new_node
    ll = new_node
    return ll

if __name__ == "__main__":
    ll = setUp()
    k = 2
    print(ll)
    ll2 = rotateRight(ll, k)
    print(ll2)
