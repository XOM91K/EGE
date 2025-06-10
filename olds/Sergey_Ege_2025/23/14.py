def F(x,y,z):
  if x > y or "AB" in z:
    return 0
  if x==y:
    return 1
  if x < y:
    return F(x+3,y,z+"A")+F(x*5,y,z+"B")+F(x*7,y,z+"C")
print(F(1,1000,""))