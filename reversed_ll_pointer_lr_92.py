class Node:
  def __init__(self,val):
    self.val = val
    self.next = None




node1  = Node(1)
node2  = Node(2)

node3  = Node(3)

node4  = Node(4)

node5  = Node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


head = node1
while head:
  print(head.val, end = "----------->")
  head = head.next

def reverseBetween(head,left,right):
  dummy = Node(0)
  dummy.next = head
  prev = dummy

  for _ in range(left-1):
    prev = prev.next
  curr = prev.next
  for _ in range(right-left):
    temp = curr.next
    curr.next = temp.next
    temp.next = prev.next
    prev.next = temp

  return dummy.next
head = node1
left = 2
right = 4
result = reverseBetween(head,left,right)

head = result
while head:
  print(head.val, end = "----------->")
  head = head.next