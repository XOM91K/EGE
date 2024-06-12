#6674
s = open('24.txt').readline().split('Z')
mn = 10 ** 10
for x in range(len(s) - 118):
    ln = 0
    for y in range(0, 119):
        ln += len(s[x + y])
    mn = min(mn, ln + 120)
print(mn)