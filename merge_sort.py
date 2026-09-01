def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    i=j = 0
    merged = []
    while i<=len(left)-1 and j<=len(right)-1:
        if left[i]<right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    # Append any remaining elements from either list
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
