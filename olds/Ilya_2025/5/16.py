l = [0] * 100000000
for x in range(10000):
    l[int(bin(x)[2:] + bin(x % 4)[2:], 2)] = 1
mx = 0
for x in range(10000 - 65):
    mx = max(mx, sum(l[x:x + 65]))
print(mx)