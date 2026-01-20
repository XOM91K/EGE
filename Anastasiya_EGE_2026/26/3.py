l = [int(x) for x in open('3.txt')]
l = sorted(l)[::-1]
kor = 1
osn = l[0]
for x in l:
    if osn - x >= 9:
        kor += 1
        osn = x
print(kor, osn)