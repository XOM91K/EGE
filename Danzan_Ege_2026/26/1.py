l = [int(x) for x in open('1.txt')]
l = sorted(l)[::-1]
korjs = [l[0]]
for x in l:
    if korjs[-1] - x >= 8:
        korjs.append(x)
#print(l)
print(len(korjs), korjs[-1])