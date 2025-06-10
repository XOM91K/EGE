def F(x,y):
  if x < y or x == 20:
    return 0
  if x == y:
    return 1
  if x > y:
    return F(x-2,y) + F(x-3,y) + F(x // 5,y)
print(F(41,10) * F(10, 5))