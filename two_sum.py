def two_sum(arr,t):
    seen = {}
    for i,num in enumerate(arr):
        diff = t-num
        if diff in seen:
            return [seen[diff],i]
        seen[num] = i
    return None

print(two_sum([2,7,11,15],9))

