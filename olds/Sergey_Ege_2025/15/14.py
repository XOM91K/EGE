ct =0
for A in range(-100,100):
  can = True
  for x in range(-100,100):
    for y in range(-100,100):
      if (((x > A) or (x**2 -7*x + 10 > 0)) and ((y <= A) or(y**2 + 7*y + 12 > 0))) == 0:
        can = False
  if can:
    ct+=1
print(ct)