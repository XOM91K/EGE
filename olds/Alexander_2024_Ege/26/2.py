l = sorted([int(x) for x in open('2.txt')])
k = 100
big_t = l[-k:]
l = l[:-k]
print(l[-1])
print(big_t)
print(sum(big_t) * 0.2)