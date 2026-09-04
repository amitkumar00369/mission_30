def trappingWater(hieght):
  left = 0
  right = len(height)-1
  left_max= height[left]
  right_max = height[right]
  water = 0
  while left<right:
    if left_max<=right_max:
      left +=1
      left_max = max(left_max,height[left])
      water +=left_max-height[left]
    else:
      right -=1
      right_max = max(right_max,height[right])
      water +=right_max - height[right]
  return water

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trappingWater(height))

def max_container_water(hieght):
  left = 0
  right = len(hieght)-1
  max_water = 0
  while left<right:
    width = right-left
    current_water = width*min(hieght[left],hieght[right])
    max_water = max(current_water,max_water)
    if hieght[left]<hieght[right]:
      left +=1
    else:
      right -=1
  return max_water

print(max_container_water([1,8,6,2,5,4,8,3,7]))




def max_sum_subarray(arr):
  current_sum = arr[0]
  max_sum = float("-inf")
  for n in arr[1:]:
    current_sum = max(n,current_sum+n)
    max_sum = max(current_sum,max_sum)
  return max_sum

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(max_sum_subarray(arr))



def minSUbarrayLen(target,arr):
  total = 0
  ans = float("inf")
  left = 0
  for right in range(len(arr)):
    total +=nums[right]
    while total>=target:
      ans = min(ans, right-left +1)
      total -=nums[left]
      left +=1

  return ans

target = 11
nums = [1,2,3,4,5]
print(minSUbarrayLen(target,nums))
     
def singleNumber(arr):
  result = 0
  for n in arr:
    result ^=n
  return result

print(singleNumber([4,1,2,1,2]))  # o/p 4

# def findadd(w):
#   total = 0
#   for ch in w:
    
    


def sumOfDigit(w,k):
  while len(w)>k:
    val = ""
    for i in range(0,len(w),k):
      
      val += str(sum(map(int,w[i:i+k])))
    
    w=val
  return w
print(sumOfDigit("11111222223",3))


def maxlongestString(words):
  left = 0
  freq = {}
  max_chr = 0
  
  for right,ch in enumerate(words):
    if ch in freq and freq[ch]>=left:
      left = freq[ch]+1
    freq[ch] = right
    max_chr = max(max_chr,right-left+1)
  return max_chr

print("optimal solutins", maxlongestString("abcabcab"))

import math
def jug_mug(x,y,t):
  if t==0:
    return False
  if t>x+y:
    return False
  return t % math.gcd(x,y)==0


print(jug_mug(3,5,4))

