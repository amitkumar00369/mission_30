class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


class LinkedList:

  def mergedTwoList(self, list1, list2):

    dummy = Node(0)
    current = dummy
    print("init",current.val)
  

    while list1 and list2:

      if list1.val <= list2.val:
        print("list  value", list1.val)

        current.next = list1
      
        list1 = list1.next
        print("init",current.val)
        

      else:
        print("list  value", list2.val)
        

        current.next = list2
        list2 = list2.next

      current = current.next
      print("current ind",current.val)
    # if list1:
    #   current.next = list1
    # else:
    #   current.next = list2

    current.next = list1 or list2

    return dummy.next


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3


node21 = Node(1)
node22 = Node(2)
node23 = Node(3)

node21.next = node22
node22.next = node23

obj = LinkedList()

result = obj.mergedTwoList(node1, node21)
print("result",result.val)

current = result

while current:
    print(current.val, end=" → ")
    current = current.next