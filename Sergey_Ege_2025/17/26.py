l = [int(x) for x in open('26.txt')]
mx = max([x for x in l if str(x)[-1] == "7"])
print(mx)
mx1 = 0
ct = 0
for x in range(len(l)-1):
  a = l[x]
  b = l[x+1]
  if str(a)[0] == str(b)[0]:
    k = 0
    if str(a)[-1] == '7' and len(str(abs(a))) == 3:
      k+=1
    if str(b)[-1] == '7' and len(str(abs(b))) == 3:
      k+=1
    if k >= 1 and (a+b) < mx:
      ct +=1
      mx1 = max(l[x]+l[x+1],mx1)
print(ct,mx1)