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

node5.next = node1
node1.prev = node5


print("/forward")

current_node = node1
start_node = node1
print(current_node.data, end=" -> ")
current_node = current_node.next
while current_node!=start_node:
  print(current_node.data, end = "----->")
  current_node = current_node.next

print()

print("/reverse")
current_node = node5
start_node = node5
print(current_node.data, end=" -> ")
current_node = current_node.prev
while current_node!=start_node:
  print(current_node.data, end="---->")
  current_node = current_node.prev

print("...")




