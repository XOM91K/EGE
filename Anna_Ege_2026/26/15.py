l = [[int(d) for d in x.split()] for x in open('15.txt')]
l = sorted(l, key=lambda d: d[0])
lines = [[0] * 10]
last_client = 0
for client in l:
    canLeave = False
    i = 0
    while i < len(lines):
        ct = 0
        for j in range(len(lines[i])):
            if client[0] > lines[i][j]:
                lines[i][j] = client[1]
                last_client = client[0]
                canLeave = True
                break
            else:
                ct += 1
        if ct == 3 and i == len(lines) - 1:
            lines.append([0] * 10)
        if canLeave:
            break
        i += 1
print(len(lines))
ct = 0
for line in lines:
    for house in line:
        if house >= last_client + 1:
            ct += 1
print(ct)


# for x in range(5):
#     print(x)
#     print(x)
#     print(x)