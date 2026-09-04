class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    self.prev = None
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2

node3.next = node4
node4.prev = node3

node4.next = node5
node5.prev  = node4

curr = node1
while curr:
  print(curr.data, end = "---->")
  curr = curr.next

curr = node5
while curr:
  print(curr.data, end="--->")
  curr = curr.prev

