l = [int(x) for x in open("5.txt")]
mn = min([x for x in l]) ** 2
mx = []
for i in range(len(l) - 1):
   if (l[i] % 77) * (l[i+1] % 77) == mn:
       mx.append(l[i] * l[i + 1])
print(len(mx), min(mx))