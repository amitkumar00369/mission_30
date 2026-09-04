def noofislands(grid):
  rows = len(grid)
  cols = len(grid[0])
  print(rows,cols)
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




def nquen(n):
  board = [["*"] * n for _ in range(n)]
  cols = set()
  diag1= set()
  diag2= set()
  result = []
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

      board[row][col] = "Q"
      cols.add(col)
      diag1.add(row-col)
      diag2.add(row+col)

      backtrack(row+1)
      board[row][col]= "*"
      cols.remove(col)
      diag1.remove(row-col)
      diag2.remove(row+col)
  backtrack(0)
  return result, len(result)

print(nquen(4))
      
                    
      