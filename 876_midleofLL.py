class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def middleNode(head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

head = node1
middle = middleNode(head)
print("Middle node value:", middle.val)  # Output: Middle node value: 3