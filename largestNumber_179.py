from functools import cmp_to_key
def largestNumber(arr):
    #ex [10,2] = 210


        '''Example 1:

    Input: nums = [10,2]
    Output: "210"
    Example 2:

    Input: nums = [3,30,34,5,9]
    Output: "9534330"'''
        nums = list(map(str,arr))
        #  ["3","30","34","5","9"]
        def compare(a,b):
                print("a and b",a,b)
                if a+b>b+a:
                        return -1
                elif a+b<b+a:
                        return 1
                else:
                        return 0

        nums.sort(key = cmp_to_key(compare))
        result = ''.join(nums)
        if result[0]=="0":
                return "0"
        return result
                
print(largestNumber( [3,30,34,5,9]))


def longestCommonPrefix()
        seen = set()