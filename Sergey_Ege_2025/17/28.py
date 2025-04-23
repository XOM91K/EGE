l = [int(x) for x in open("28.txt")]
s = len([x for x in l if x % 32 == 0])
ct = 0
mx = -1000000000
for x in range(len(l)-1):
  k = 0
  if str(l[x])[0] == "-":
    k+=1
  if str(l[x+1])[0] == "-":
    k+=1
  if k >= 1:
    if l[x] + l[x+1] < s:
      ct +=1
      mx = max(l[x]+l[x+1],mx)
print(ct,mx)