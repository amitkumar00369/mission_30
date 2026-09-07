def sortByevnandoddonebyone(nums):
  even = 0
  odd = 1
  while even < len(nums) and odd < len(nums):
    while even<len(nums) and nums[even]%2==0:
      even +=2
    while odd<len(nums) and nums[odd]%2==1:
      odd +=2
    if even<len(nums) and odd<len(nums):
      nums[even],nums[odd] = nums[odd],nums[even]
  return nums
  
  
  

Input = [3,1,2,4]


print(sortByevnandoddonebyone(Input))