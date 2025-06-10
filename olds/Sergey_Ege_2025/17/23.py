l = [int(x) for x in open("23.txt")]
mx = max([x for x in l if str(x)[-1] == "7"])

print(mx)
ct = 0
l1 = []
sr = 0
for x in range(len(l) - 2):
    k = 0
    if l[x] % 2 != 0:
        k += 1
    if l[x + 1] % 2 != 0:
        k += 1
    if l[x + 2] % 2 != 0:
        k += 1
    if k == 2:

      k1 = 0
      if l[x] > mx:
          k1 += 1
      if l[x + 1] > mx:
          k1 += 1
      if l[x + 2] > mx:
          k1 += 1
          if k1 == 1:
            print(l[x], l[x + 1], l[x + 2])
            ct += 1
            l1.append(l[x])
            l1.append(l[x + 1])
            l1.append(l[x + 2])
l1 = list(set(l1))
sr = sum(l1) / len(l1)
print(l1)
print(ct, sr)
