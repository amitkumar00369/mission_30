class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        old_to_new = {}

        # 1. Create copy of every node
        current = head

        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        # 2. Connect next and random pointers
        current = head

        while current:
            copy = old_to_new[current]

            copy.next = old_to_new.get(current.next)
            copy.random = old_to_new.get(current.random)

            current = current.next

        return old_to_new[head]