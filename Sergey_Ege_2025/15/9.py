ct = 0
for A in range(1,1000):
  can = True
  for x in range(1,1000):
      if ((A%3==0) and ((220%x==0)<=((A%x!=0)<=(550%x != 0)))) == 0:
        can = False
  if can:
    ct += 1

print(ct)