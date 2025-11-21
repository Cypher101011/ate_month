class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = Node(0)
        dummy.next = head
        slow = fast = dummy

        # Move fast pointer n+1 steps ahead
        for i in range(n + 1):
            if fast:
                fast = fast.next

        # Move both until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next

        # Delete the nth node from end
        if slow.next:
            slow.next = slow.next.next

        return dummy.next
