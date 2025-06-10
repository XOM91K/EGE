l = [int(x) for x in open("29.txt")]
ct = 0
mn1 = 10**10
mn = min([x for x in l if x % 12 == 0 and str(x)[0] != "-"])
for x in range(len(l)-2):
  k = 0
  if len(str(abs(l[x]))) == 5 and l[x] % 506 == 0:
    k+=1
  if len(str(abs(l[x+1]))) == 5 and l[x+1] % 506 == 0:
    k+=1
  if len(str(abs(l[x+2]))) == 5 and l[x+2] % 506 == 0:
    k+=1
  if k >= 1:
    if abs(l[x]*l[x+1]*l[x+2]) % 100 == mn:
      ct +=1
      mn1 = min(mn1, abs(l[x] + l[x + 1] + l[x + 2]))
print(ct,mn1)