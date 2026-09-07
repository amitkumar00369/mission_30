print("Start small. Ship something.")


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)


# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


def orderedList(head):

    if not head or not head.next:
        return

    # 1. Find middle
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 2. Split the list
    second = slow.next
    slow.next = None

    # 3. Reverse second half
    prev = None
    curr = second

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    second = prev

    # 4. Merge two halves
    first = head

    while second:
        tmp1 = first.next
        tmp2 = second.next

        first.next = second
        second.next = tmp1

        first = tmp1
        second = tmp2

    return head


# Call function
curr = node1
current = orderedList(curr)


# Print result
while current:
    print(current.val, end="---------->")
    current = current.next