def minSubArrayLen0(target,nums):
    left = 0
    right = len(nums)-1
    while left<right:
        if nums[left]==target:
            return 1
        if nums[right]==target:
            return 1
        total = nums[left]+nums[right]
        if total==target:
            return len([left,right])
        elif total<target:
            left +=1
        else:
            right -=1
    return 0

target = 4
nums = [1,4,4]

print(minSubArrayLen0(target,nums))


# optima;l solution
def minSubArrayLen(target,nums):
    left = 0
    ans= float("inf")
    total = 0

    for right in range(len(nums)):
        total += nums[right]
        while total>=target:
            ans = min(ans,right-left+1)
            total -=nums[left]
            left +=1
    return 0 if ans==float("inf") else ans

target = 11
nums = [1,2,3,4,5]
print(minSubArrayLen(target,nums))