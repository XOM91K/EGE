l = [[int(d) for d in x.split()] for x in open('21.txt')]
min_start = 10 ** 10

for x in l:
    if x[0] != 0:
        min_start = min(min_start, x[0])
max_start = 0
for x in l:
    if x[1] != 0:
        max_start = max(max_start, x[1])
print(l)
print(min_start)
print(max_start)
print(1633046400)
print(1634515200)
#1634515200
