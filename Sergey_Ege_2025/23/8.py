def f(x,y,z):
  if x  > y or ("aa" in z):
    return 0
  if x == y:
    return 1
  if x < y :
    return f(x-1,y,z+"a") + f(x*2,y,z+"b") + f(x*3,y,z+"c")
print(f(3,15,""))