l = [[int(d) for d in x.split()] for x in open('14.txt')]
l = sorted(l)
lines = [[-1] * 10]
clientlast = 0
for x in l:
    canLeave = False
    i = 0
    while i < len(lines):
        for j in range(len(lines[i])):
            if x[0] > lines[i][j]:
                lines[i][j] = x[1]
                clientlast = x[0]
                canLeave = True
                break
        else:
            if i == len(lines) - 1:
                lines.append([-1] * 10)
        if canLeave:
            break
        i += 1
print(lines)
print(len(lines))
ct = 0
for line in lines:
    for client in line:
        if client >= clientlast + 1:
            ct += 1
print(clientlast)
print(ct)
# l = [[-1] * 3]
# l.append([-1] * 3)
# l[1][2] = -5
# print(l)