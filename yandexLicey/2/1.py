lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line.split(' '))
lines2 = []
for x in lines:
    lines2.append(x[-1].title())
lines2 = list(set(lines2))
lns = ''
for x in lines2:
    lns += x + ', '
print(lns[:-2])