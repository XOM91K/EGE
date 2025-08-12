l = [[int(d) for d in x.split()] for x in open('164.txt')]
k = 0
for x in l:
    k += 1
    if x == sorted(x):
        ch = sum([sum(map(int, str(y))) for y in x if x.count(y) >= 2])
        if ch % 2 == 0 and ch != 0:
            print(k, x, ch)