class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4


def showpairs(head):
    dummy = Node(0)
    dummy.next = head

    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = first.next

        # swap
        prev.next = second
        first.next = second.next
        second.next = first

        # move to next pair
        prev = first

    return dummy.next


result = showpairs(node1)

head = result

while head:
    print(head.val, end="----------->")
    head = head.next