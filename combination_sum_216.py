def combination(k,n):
  result = []
  
  def backtrack(start,path,total):
    if len(path)==k:
      if total==n:
        result.append(path.copy())
      return
    for num in range(start,10):
      if total+num>n:
        break
      path.append(num)
      backtrack(num+1,path,total+num)
      path.pop()
      
    
    pass
  backtrack(1,[],0)
  return result

k = 3
n = 7
print(combination(3,7))