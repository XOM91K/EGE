l = [[int(d) for d in x.split()] for x in open('19.txt')]
b = [0] * 2
#l = sorted(l, key=lambda d: d[0])
for x in l:
    print(x, sum(x))