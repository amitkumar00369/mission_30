def isPalindrome(s):
        netStr = ""
        for ch in s:
            print(ch)
            if ch.isalpha():
                if ch.isupper():
                    netStr +=ch.lower()
                else:
                    netStr +=ch
        print(netStr)
        if len(netStr)<2:
             return False
                 
        left = 0
        right = len(netStr)-1
        while left<=right:
            if netStr[left]==netStr[right]:
                
                left +=1
                right -=1
            elif netStr[left]!=netStr[right]:
                return False
        return True
print(isPalindrome("0P"))



# optimal solutions
def Pellindrome(s):
    newStr = ""
    for ch in s:
        if ch.isalnum():
            newStr +=ch.lower()
    print(newStr)
    left  = 0
    right = len(newStr)-1
    while left<right:
        if newStr[left]!=newStr[right]:
            return False
        left +=1
        right -=1
    return True

print(Pellindrome("A man, a plan, a canal: Panama"))

    
               