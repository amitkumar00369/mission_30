# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Start small. Ship something.")

def sortByPariority(arr):
  left = 0
  right = len(arr)-1
  while left<right:
    if arr[left]%2==0:
      left +=1
    elif arr[right]%2==1:
      right -=1
    else:
      arr[left],arr[right] = arr[right],arr[left]
      left +=1
      right -=1
  return arr
print(sortByPariority([3,1,2,4]))


def sortByPriorityOddEven(arr):
  even = 0
  odd=1
  while even<len(arr) and odd<len(arr):
    while even<len(arr) and arr[even]%2==0:
      even +=2
    while odd<len(arr) and arr[odd]%2==1:
      odd +=2
    if even<len(arr) and odd<len(arr):
      arr[even],arr[odd] = arr[odd],arr[even]

  return arr

Input = [3,1,2,4]


print(sortByPriorityOddEven(Input))
      
    
      