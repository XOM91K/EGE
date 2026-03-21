l = [[int(d) for d in x.split()] for x in open('11.txt')]
ot = [0] * 44640
for x in l:
    for i in range(x[0], x[1]):
        ot[i] = 1
print(ot.count(1))
s = ''.join([str(d) for d in ot]).split('0')
print(len(max(s, key=len)))