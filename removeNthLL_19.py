class Node:
  def __init__(self,val):
    self.val = val
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
current = node1
n = 0
while current:
  print(current.val, end ="------------>")
  current = current.next
  n +=1


print()

print("lenght of list" , n)

def removeNthFromEnd(head, n):
  dummy = Node(0)
  dummy.next = head
  first = dummy
  second = dummy

  for i in range(n + 1):
    first = first.next

  while first:
    first = first.next
    second = second.next

  second.next = second.next.next

  return dummy.next

print("n value", n)
new_head = removeNthFromEnd(node1, 2)