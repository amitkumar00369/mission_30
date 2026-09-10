def removeOccurence(s,part):
  while part in s:
    s = s.replace(part,"",1)
    # print(s)
  return s
  
      
def removeOccurence(s,part):
  stack = []
  for ch in s:
    stack.append(ch)
    if len(stack)>=len(part):
      print("".join(stack[-len(part):]))
      if "".join(stack[-len(part):])==part:
        for _ in range(len(part)):
          stack.pop()

  return "".join(stack)
    
    

  # return word

print(removeOccurence("daabcbaabcbc","abc"))
    
