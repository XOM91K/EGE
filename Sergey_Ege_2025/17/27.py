l = [int(x) for x in open("27.txt")]
mn = min([x for x in l if x % 2 == 0])
print(mn)
ct = 0
mn1 = 10**10
for x in range(len(l)-2):
  if (l[x] % 2 == 0 and l[x+2] % 2 != 0) or (l[x + 2] % 2 == 0 and l[x] % 2 != 0):
    if l[x + 1] % mn == 0:
        ct += 1
        mn1 = min(mn1,l[x]+l[x+2])
print(ct,mn1)