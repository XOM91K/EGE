l = [int(x) for x in open('2.txt')]
l = sorted(l)[::-1]
korjs = [l[0]]
for x in l:
    if korjs[-1] - x >= 8:
        korjs.append(x)
print(len(korjs), korjs[-1])