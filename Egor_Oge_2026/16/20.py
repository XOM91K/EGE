d = 121
dls = []
for x in range(1, d + 1):
    if d % x == 0:
       dls.append(x)
print(len(dls))
print(max(dls))
print(sum(dls))