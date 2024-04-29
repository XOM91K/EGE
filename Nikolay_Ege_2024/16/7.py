def F(n):
  if n < 3:
    print("*")
  else:
    F(n-1)
    F(n-2)
    F(n-2)
F(6)