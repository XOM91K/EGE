s = open('11.txt').readline()
ct = 0
mx = 0
for x in range(0, 27):
    for y in range(len(s) - x):
        g = s[y: y + x]
        if len(set(g)) == len(g):
            mx = max(mx, x)
            break
print(mx)