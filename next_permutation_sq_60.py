class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def nextPermuations(nums):
            nums = list(str(nums))
            n = len(nums)
            i = n-2
            while i>=0 and nums[i]>nums[i+1]:
                i-=1
            if i==-1:
                nums.reverse()
                return
            j = n-1
            while nums[j]<=nums[i]:
                j-=1
            nums[j],nums[i] = nums[i],nums[j]
            nums[i+1: ] = reversed(nums[i+1:])
            result = "".join(nums)
            return result
        word = ""

        for i in range(1, n + 1):
            word += str(i)

        if k == 1:
            return word

        c = 1

        while c < k:
            val = nextPermuations(word)

            if val is None:
                break

            word = val
            c += 1

        return word


        