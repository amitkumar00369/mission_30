# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Start small. Ship something.")


class Node:
  def __init__(self,val):
    self.val = val
    self.next = None



node1 = Node(2)
node2 = Node(4)
node3 = Node(3)
node1.next = node2
node2.next = node3


node11  = Node(5)
node12 = Node(6)
node13 = Node(4)


node11.next = node12
node12.next = node13

def addTwoNumber(l1,l2):
  dummy = Node(0)
  curr = dummy
  carry =0
  while l1 or l2 or carry:
    x = l1.val if l1 else 0
    y = l2.val if l2 else 0
    total = x+y+carry
    digit = total%10
    carry = total//10
    curr.next = Node(digit)
    curr = curr.next
    if l1:
      l1 = l1.next
    if l2:
      l2 = l2.next

  return dummy.next


current = addTwoNumber(node1,node11)
while current:
  print(current.val, end = "----->")
  current = current.next
  

