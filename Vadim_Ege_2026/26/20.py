okna = [0] * 10
l = [[int(d) for d in x.split()] for x in open('20.txt')]
l = sorted(l)
ct = 0
for x in l:
    for y in range(len(okna)):
        if x[0] > okna[y]:
            okna[y] = x[1]
            ct += 1
            print(y + 1)
            break
print(ct)