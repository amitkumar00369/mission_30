class MinStack:
  def __init__(self):
    self.stack = []
    self.min_stack = []

  def push(self,val):
    self.stack.append(val)
    if not self.min_stack:
      self.min_stack.append(val)
    else:
      self.min_stack.append(min(val, self.min_stack[-1]))
  def pop(self):
    self.stack.pop()
    self.min_stack.pop()
  def top(self):
    return self.stack[-1]
  def getMin(self):
    return self.min_stack[-1]

minStack =MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); #// return -3
minStack.pop();
minStack.top();   # // return 0
minStack.getMin(); #// return -2
 