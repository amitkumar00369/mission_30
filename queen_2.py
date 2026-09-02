def nQueen(n):
    result = []
    cols = set()
    board = [["."]*n for _ in range(n)]
    diag1 =set()
    diag2 = set()
    def backtrack(row):
        if row==n:
            result.append([''.join(r) for r in board])
            return
        for col in range(n):
            if col in cols:
                continue
            if row-col in diag1:
                continue
            if row + col in diag2:
                continue
            board[row][col]="Q"
            cols.add(col)
            diag1.add(row-col)
            diag2.add(row+col)
            # row move next
            backtrack(row+1)
            # now move backtrack
            board[row][col] = "."
            cols.remove(col)
            diag1.remove(row-col)
            diag2.remove(row+col)

    backtrack(0)
    return len(result)



print(nQueen(4))