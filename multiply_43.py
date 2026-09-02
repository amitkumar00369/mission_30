def multiply(num1,num2):
    if len(num1)=="0" or len(num2)=="0":
        return "0"
    m,n = len(num1),len(num2)
    result = [0]*(m+n)
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            a = (ord(num1[i])-ord('0'))
            b = (ord(num2[j])-ord('0'))
            product = a*b
            pos = i+j+1
            total=result[pos]+product
            result[pos] = total%10
            result[pos-1] += total//10
    return ''.join(map(str,result)).lstrip('0')

   
  
    return result
   
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(multiply("12","12"))