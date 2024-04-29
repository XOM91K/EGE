l = [[int(d) for d in x.split()] for x in open('2.txt')]
mx = 0
print(l)
for x in l:
    if len(set(x)) < len(x):
        mx = max(mx, sum(x))
print(mx)