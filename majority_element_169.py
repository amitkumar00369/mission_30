def majority_element_169(arr):
    candidate = arr[0]
    count = 1
    for i in range(1,len(arr)):
        if count==0:
            candidate = arr[i]
            count = 1
        elif arr[i] == candidate:
            count +=1
        else:
            count -=1
    return candidate

print(majority_element_169([2,2,1,1,1,2,2]))
