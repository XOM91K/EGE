l = [[int(d) for d in x.split()] for x in open('20.txt')]
k = [-1] * 267
print(k)
print(l)
ct = 0
for x in l:
    for y in range(len(k)):
        if x[0] > k[y]:
            k[y] = x[1]
            ct += 1
            print(y + 1)
            break
print(ct)