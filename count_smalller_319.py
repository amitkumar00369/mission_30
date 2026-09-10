# Input: nums = [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.

def countSmaller(arr):
  count = [0]*len(arr)
  left = 0
  right = 1

  for i in range(0,len(arr)):
    c = 0
    for j in range(i+1,len(arr)):
      if arr[i]>arr[j]:
        c+=1
    count[i] = c
  return count
nums = [5,2,6,1]
print(countSmaller(nums))

def countSmaller1(nums):
  n = len(nums)
  result = [0] * n
  arr = [(num, i) for i, num in enumerate(nums)]
  print(arr)
  def merge_sort(left,right):
    if left>=right:
      return
    mid = (left+right)//2
    merge_sort(left,mid)
    merge_sort(mid+1,right)
    merge(left,mid,right)
  def merge(left,mid,right):
    temp = []
    i = left
    j = mid + 1
    smaller = 0

    while i<=mid and j<=right:
      if arr[j][0]<arr[i][0]:
        temp.append(arr[j])
        j +=1
        smaller +=1
      else:
        result[arr[i][1]] +=smaller
        temp.append(arr[i])
        i +=1
    while i<=mid:
      result[arr[i][1]] += smaller
      temp.append(arr[i])
      i += 1
    while j<=right:
      temp.append(arr[j])
      j += 1
    arr[left:right+1] = temp
      
  merge_sort(0,n-1)
  return result

print(countSmaller1(nums))
    
   
  
  
      
    
  