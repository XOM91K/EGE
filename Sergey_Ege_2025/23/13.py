def F(x,y):
  if x>y or x == 17 or x==32 or x ==50:
    return 0
  if x==y:
    return 1
  if x < y:
    return F(x+1,y)+F(x+5,y)+F(x**2,y)
print(F(5,25)*F(25,45)*F(45,60))