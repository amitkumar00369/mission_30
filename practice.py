# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Start small. Ship something.")


def twoSum(arr,t):
    left,right = 0,len(arr)-1
    while left<right:
        total = arr[left]+arr[right]
    
        if total==t:
            return [left,right]
        if total<t:
            left +=1
        else:
            right -=1
    return -1

print(twoSum([1,2,3,4,5],9))

def noofislands(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    def dfs(r,c):
        if (r<0 or r>=rows or c<0 or c>=cols or grid[r][c]!="1"):
            return
        grid[r][c] = "0"
        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]=="1":
                count +=1
                dfs(r,c)

    return count

arr = [
 ["1","1","0","0"],
 ["1","1","0","1"],
 ["0","0","1","1"],
 ["0","0","0","0"]
]
print(noofislands(arr))

def nQueen(n):
    board = [["."]*n for _ in range(n)]
    cols = set()  # store column
    diag1 = set()   # store diagona row -col
    diag2 = set()   # store row +col
    result=[]

    def backtrack(row):
        if row==n:
            result.append(["".join(r) for r in board])
            return 
        for col in range(n):
            if col in cols:
                continue
            if row-col in diag1:
                continue
            if row+col in diag2:
                continue
            board[row][col]="Q"
            cols.add(col)
            diag1.add(row-col)
            diag2.add(row+col)
            backtrack(row+1)
            board[row][col] = "."
            cols.remove(col)
            diag1.remove(row-col)
            diag2.remove(row+col)

    backtrack(0)
    return result, len(result)



print(nQueen(4))

def stringCalculations(s1,s2):
    if s1=="0" or s2=="0":
        return "0"

    m = len(s1)
    n = len(s2)
    result = [0]*(m+n)
    for i in range(m):
        for j in range(n):
            a = (ord(s1[i])-ord("0"))
            b = (ord(s2[j])-ord("0"))
            product = a*b
            pos = i+j+1
            total = result[pos]+product
            result[pos] = total%10
            result[pos-1] +=total//10
    return "".join(map(str,result)).lstrip("0")


print(stringCalculations("12","10"))


def permutation(n,k):
    def next_permutation(word):
        arr = list(str(word))
        print(arr)
        n = len(arr)
        i= n-2
        while i>=0 and arr[i]>arr[i+1]:
            i -=1
        if i==-1:
            # word.reverse()
            return

        j = n-1
        while arr[j]<=arr[i]:
            j -=1
        arr[j],arr[i] = arr[i],arr[j]
        arr[i+1: ] = reversed(arr[i+1:])
        res = "".join(arr)
        print("reess",res)

        return res
    word = ""
    for i in range(1,n+1):
        word +=str(i)
    print("wee",word)
    if k==1:
        return word
    c=1
    while c<k:
        val = next_permutation(word)
        print(val)
        if val is None:
            
            break
        word = val
   
        c +=1
        print(c)
    return word

print(permutation(3,3))


            










