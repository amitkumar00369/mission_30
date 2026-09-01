# scan from right until not found decresed element  find first pivot element 
#  after find pivot number we scan from this to left and find smallest and greater than pivot numer
#  swap this pivot index with this index
#  after that reversed remaining element from this


def next_permutation(num):
    digits = list(str(num))
    n = len(digits)
    i = n-2
    while i>=0 and digits[i]>=digits[i+1]:
        i -=1
    print("pivot index and number", i, digits[i],digits)
    if i==-1:
        # num.reverse()   when we do list
        return -1
    j = n-1
    while digits[j]<=digits[i]:
        j -=1
    digits[j],digits[i] = digits[i],digits[j]
    digits[1+1:] = reversed(digits[i+1: ])
    return int("".join(digits))


print(next_permutation(534976))
