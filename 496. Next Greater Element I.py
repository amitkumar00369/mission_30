# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.



def nextGreaterElement(nums1,nums2):
  stack = []
  mp = {}
  for n in nums2:
    while stack and n>stack[-1]:
      smaller = stack.pop()
      mp[smaller] = n
    stack.append(n)
  while stack:
    mp[stack.pop()] = -1
  return [mp[n] for n in nums1]
nums1 = [4,1,2]
nums2 = [1,3,4,2]

print(nextGreaterElement(nums1,nums2))
    