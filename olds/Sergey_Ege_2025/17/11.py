l =[int(x) for x in open("11.txt")]
mx25 = 0
ct = 0
mx = 0
for x in l:
  if str(abs(x))[-2:] == "25":
    mx25 = max(mx25,x)
for x in range(len(l)-2):
    k = 0
    if len(str(abs(l[x]))) == 4:
        k += 1
    if len(str(abs(l[x+1]))) == 4:
        k += 1
    if len(str(abs(l[x+2]))) == 4:
        k += 1
    if k <= 2 and l[x] + l[x+1] + l[x+2] <= mx25:
        ct +=1
        mx = max(mx, l[x] + l[x+1]+l[x+2])
print(ct,mx)