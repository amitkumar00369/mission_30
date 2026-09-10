def dailyTemperatures(nums):
  rating = [0]*len(nums)
  day = 1
  for i in range(0,len(nums)):
    for j,n in enumerate(nums[i:],0):
      if nums[i]<n:
        rating[i] = j
        break
    
  
  return rating
temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))

# optimal solution
def dailyTemperatures(temperature):
  rating = [0]*len(temperature)
  stack = []
  for i in range(len(temperature)):
    while stack and temperature[i]>temperature[stack[-1]]:
      prev = stack.pop()
      rating[prev] = i-prev
    stack.append(i)
    
  
  return rating
temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))
      