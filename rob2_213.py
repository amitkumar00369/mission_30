def rob2(nums):
    if len(nums)==1:
        return  nums[0]
    def rob(nums):
        prev1 = 0
        prev2 = 0
        for num in nums:
            curr = max(prev1,prev2+num)
            prev2 = prev1
            prev1 = curr
        return prev1
    return max(rob(nums[1:]),rob(nums[:-1]))


print(rob2([2,3,2]))