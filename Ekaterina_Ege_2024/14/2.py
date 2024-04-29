s = 100**10-10**6+100
k = 0
while s > 0:
  if s % 10==0:
     k += 1
  s = s // 10
print(k)