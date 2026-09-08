def findMostConsecutiveOnes(arr):
  left = 0
  ones = 0
 
  for ch in arr:
    if ch==1:
      left +=1
      ones = max(ones,left)
    else:
      left =0
  return ones
    
      
 
nums = [1,1,0,1,1,1]
print(findMostConsecutiveOnes(nums))