def f(s,p):#21
  if s <= 1 and (p== 2 or p == 4):
    return 1
  if s <= 1 and (p==1 or p==3):
    return 0
  if s > 1 and p == 4:
    return 0
  if p%2==0:
      if s >= 4 and s % 3 == 0:
          return f(s-4,p+1) and f(s-1,p+1) and f(s//3,p+1)
      elif s >= 4:
          return f(s - 4, p + 1) and f(s - 1, p + 1)
      elif s % 3 == 0:
          return f(s - 1, p + 1) and f(s//3,p+1)
      else:
          return f(s-1,p+1)
  else:
      if s >= 4 and s % 3 == 0:
          return f(s-4,p+1) or f(s-1,p+1) or f(s//3,p+1)
      elif s >= 4:
          return f(s - 4, p + 1) or f(s - 1, p + 1)
      elif s % 3 == 0:
          return f(s - 1, p + 1) or f(s//3,p+1)
      else:
          return f(s-1,p+1)
for x in range(100,3,-1):
  if f(x,0) == 1:
    print(x)