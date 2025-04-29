l = [int(x) for x in open('3.txt')]
N = min([x for x in l if x % 15 != 0])
mx = []
for x in range(len(l) - 1):
    if l[x] % N == 0 and l[x + 1] % N == 0:
       mx.append(l[x] + l[x + 1])
print(len(mx), max(mx))