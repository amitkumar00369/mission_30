def claimstairs(n):
    one = 1
    two = 1
    for _ in range(n):
        one,two = two,one+two
    return one

print(claimstairs(2))