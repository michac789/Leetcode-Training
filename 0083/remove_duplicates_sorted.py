"""
Leetcode Problem 0083
Difficulty: Easy
Runtime: 34ms (68.41% faster)
Memory usage: 13.4MB (66.08% less)

Description:
Given the head of a sorted linked list, delete all duplicates.
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

def deleteDuplicates(head):
    used = None
    prev = None
    curr = head
    while curr:
        if curr.val == used: prev.next = curr.next
        else:
            used = curr.val
            prev = curr
        curr = curr.next
    return head

def setUp():
    next_val = None
    for i in [7, 7, 5, 3, 2, 2, 2, -3]:
        new_node = ListNode(i, next_val)
        next_val = new_node
    ll = new_node
    return ll

if __name__ == "__main__":
    ll = setUp()
    print(ll)
    result = deleteDuplicates(ll)
    print(result)
