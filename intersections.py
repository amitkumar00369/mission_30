def findUnique(arr1,arr2):
   set1 = set(arr1)
   return list(set1.intersection(arr2))


print(findUnique([1,2,3,4,5],[4,5,6,7,8]))