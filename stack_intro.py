
class Stack:
  def __init__(self):
    self.stack = []
  def pushElement(self,val):
      return self.stack.append(val)
  def peak(self):
      if self.isEmpty():
        return "stack is empty"
      return self.stack[-1]
  def popELement(self):
    if self.isEmpty():
      return "stack is already empty"
    return self.stack.pop()
  def isEmpty(self):
    return len(self.stack)==0
  def sizeOfStack(self):
    return len(self.stack)


stack = Stack()
stack.pushElement(1)
stack.pushElement(2)
stack.pushElement(3)
stack.pushElement(4)


print(stack.peak())