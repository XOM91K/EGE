l = [int(x) for x in open("19.txt")]
ct = 0
oc151 = [x for x in l if str(x)[-3:] == "151"]
sr = sum(oc151)/ len(oc151)
mn = 10**10
for x in range(len(l)-2):
  k = 0
  if len(str(abs(l[x]))) == 4:
    k +=1
  if len(str(abs(l[x+1]))) == 4:
    k +=1
  if len(str(abs(l[x+2]))) == 4:
    k +=1
  if k <= 2 and k != 0:
    k1 = 0
    k2 = 0
    if l[x] % 13 == 0:
      k1 += 1
    if l[x+1] % 13 == 0:
      k1 += 1
    if l[x+2] % 13 == 0:
      k1 += 1
    if l[x] % 7 == 0:
      k2 += 1
    if l[x+1] % 7 == 0:
      k2 += 1
    if l[x+2] % 7 == 0:
      k2 += 1
    if k1 > k2 and l[x] > sr and l[x+1] > sr and l[x+2] > sr:
      ct +=1
      mn = min(mn,l[x] +l[x+1] + l[x+2])
print(ct,mn)