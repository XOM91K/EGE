s = open('24.txt').readline().split('Z')
print(s)
mx = 1000000
for x in range(len(s) - 118):
    ln = 0
    for y in range(0, 119):
        ln += len(s[x + y])
    mx = min(mx, ln + 120)
print(mx)