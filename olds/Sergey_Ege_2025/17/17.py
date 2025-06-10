l = [int(x) for x in open("17.txt")]
sr = sum(l) / len(l)
ct = 0
sm = 0
for x in range(len(l) -1):
  a = str(l[x])
  b = str(l[x+1])
  if (l[x] < sr and l[x+1] < sr) and (a[-1] == "9" or b[-1] == "9"):
    ct +=1
    sm = max(sm,l[x] + l[x+1])
print(ct,sm)