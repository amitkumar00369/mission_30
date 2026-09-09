def rob(nums):
        prev2 = 0
        prev1 = 0

        for money in nums:
            current = max(prev1, money + prev2)

            prev2 = prev1
            prev1 = current

        return prev1
print(rob([1,2,3,1])) # 4

# 213,232