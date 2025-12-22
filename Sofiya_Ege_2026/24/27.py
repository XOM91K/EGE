s = open(r'C:\Users\Zarif\Downloads\1415_1 (2).txt').readline()
s = s.split('X')
mn = []
for x in range(len(s) - 498):
    ln = 0
    ctY = 0
    for y in range(0, 499):
        ln += len(s[x + y])
        ctY += s[x + y].count('Y')
    if ctY == 0:
      mn.append(ln)
print(min(mn) + 500)