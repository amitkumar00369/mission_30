def permuteUnique(nums) :
    def nextPermutation(arr):
        n = len(arr)
        i = n-2
        while i>=0 and arr[i]>=arr[i+1]:
            i -=1
        if i==-1:
            arr.reverse()
            return
        j = n-1
        while arr[j]<=arr[i]:
            j-=1
        arr[j],arr[i] = arr[i], arr[j]
        arr[i+1: ] = reversed(arr[i+1:])
        return arr
    nums.sort()
    arrs = []
    arrs.append(nums.copy())
    while True:
        val = nextPermutation(nums)
        if val is None:
            break
        arrs.append(val.copy())
    return arrs