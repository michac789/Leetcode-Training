"""
Leetcode Problem 0203
Difficulty: Easy
Runtime: 68ms (73.28% faster)
Memory usage: 19.9MB (98.87% less)

Description:
Given the head of a linked list and an integer val, remove all nodes
of the linked list that has value of val, then return the new head.
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

def removeElements(head, val):
    if not head: return
    curr = head
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    if head.val == val:
        head = head.next
    return head

def setUp():
    next_val = None
    for i in [7, 7, 5, 7, -3, 7, 7]:
        new_node = ListNode(i, next_val)
        next_val = new_node
    ll = new_node
    return ll

if __name__ == "__main__":
    ll = setUp()
    print(ll)
    result = removeElements(ll, 7)
    print(result)
