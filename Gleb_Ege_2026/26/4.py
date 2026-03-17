l = [[int(d) for d in x.split()] for x in open('4.txt')]
l = sorted(l)
okna = [0] * 267
print(okna)
ct = 0
for x in l:
    for y in range(len(okna)):
        if x[0] > okna[y]:
            okna[y] = x[1]
            ct += 1
            print(y + 1)
            break
print(okna)
print(ct)