"""
Leetcode Problem ____
Difficulty: _____
Runtime: ___ms (__% faster)
Memory usage: ___MB (__% less)

Description:
TODO
"""

def func(peri):
    pass

if __name__ == "__main__":
    pass

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
