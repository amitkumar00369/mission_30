def sumOfDigit(s,k):
    # def sums(s):
    #     total = 0
    #     for w in s:
    #         total +=(ord(w)-ord('0'))
  
    #     return str(total)
    while len(s)>k:
        reduceString = ""
        for i in range(0,len(s),k):
         
            # reduceString +=sums(s[i:i+k])
            reduceStr += str(sum(map(int, s[i:i+k])))
        s = reduceString
    return s
    
    
# print(sumOfDigit("11111222223",3))

print(sumOfDigit("11111222223",3))