


f = [[int(n) for n in i.split()] for i in open('9.txt')]

for s in f:
    if s == sorted(s, reverse=True):
        if ((s[0] + s[-1])/2) > sum(s[1:-1])/len(s[1:-1]):
            print(sum(s))
            break