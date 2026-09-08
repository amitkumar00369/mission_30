def minMovesToCaptureTheQueen(a: int, b: int,c: int, d: int,e: int, f: int):
  print()
  
   

        # Check if rook can capture queen in 1 move
  if a == e:
      # Bishop blocks rook?
      if c == a and min(b, f) < d < max(b, f):
          pass
      else:
          return 1

  if b == f:
      # Bishop blocks rook?
      if d == b and min(a, e) < c < max(a, e):
          pass
      else:
          return 1

  # Check if bishop can capture queen in 1 move
  if abs(c - e) == abs(d - f):

      # Rook blocks bishop?
      if abs(a - e) == abs(b - f) and \
         min(c, e) < a < max(c, e) and \
         min(d, f) < b < max(d, f):
          pass
      else:
          return 1

  # Otherwise, 2 moves are always enough
  return 2
a = 1
b = 1 
c = 8
d = 8
e = 2
f = 3
print(minMovesToCaptureTheQueen(a,b,c,d,e,f))