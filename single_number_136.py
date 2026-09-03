def single_num(arr):
    result = 0
    for n in arr:
        result ^=n
    return result
print(single_num([4,1,2,1,2]))