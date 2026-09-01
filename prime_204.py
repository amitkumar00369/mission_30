def countPrimes(n):
        if n<=1:
            return 0
        def checkedPrimeNumber(n):
            if n<=1:
                return False
           
            if n==2 or n==3:
                return True
            if n%2==0:
                return False
            for i in range(3,int(n**.5)+1,2):
                if n%i==0:
                    return False
            return True
        c = 0
        for i in range(n):
            if checkedPrimeNumber(i):
                print(i)
                c +=1
        return c if c>0 else 0

print(countPrimes(10))

def countPrime(n):
    is_prime = [True]*n
    print(is_prime)
    is_prime[0] =  is_prime[1] =False
    print(is_prime)
    p = 2
    while p*p<n:
        if is_prime[p]:
            for multiple in range(p*p,n,p):
                is_prime[multiple] = False
        p +=1
    return sum(is_prime)
print(countPrime(10))
