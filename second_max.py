def second_max(arr):
    first = second = float("-inf")
    for n in arr:
        if n>first:
            second = first
            first =n 

        elif first>n>second:
            second = n
    return second

print(second_max([1,2,3,4,5]))  