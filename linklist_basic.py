# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Start small. Ship something.")

class Node:
    def __init__(self,data):
      self.data = data
      self.next = None




node1  = Node(3)   # sassing 2
node2 = Node(4)   #assing 4
node3 = Node(5)    #assing
node4 = Node(2)    #assign 2



node1.next = node2   # 3 points 4
node2.next = node3   # 4 points 5
node3.next = node4   # 5 points 2

# 3-->4-->5-->2

curr  = node1
while curr:
  # print(curr.data,"---->")
  curr = curr.next
print("null")


prev = None
curr = node1
while curr:
  print(curr.data, "---->")
  next_node = curr.next
  print("next_node",next_node)
  curr.next = prev
  print("crr next",  curr.next)
  prev = curr
  print("prev",  prev,curr.data)
  
  curr = next_node
  print("curr",curr)

curr  = prev
while curr:
  print(curr.data,"---->")
  curr = curr.next
print("null")
