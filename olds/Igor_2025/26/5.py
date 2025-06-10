sm = 100_000
l = [[d for d in x.split()] for x in open('5.txt')]
ctA = 0
for x in range(len(l)):
    l[x] = [int(l[x][0]), l[x][1]]
l = sorted(l)
j = 0
buyes = []
for x in l:
    if sm - x[0] >= 0:
        sm -= x[0]
        if x[1] == 'A':
            ctA += 1
        if x[1] != 'A':
            buyes.append(x)
        j += 1

print(buyes)
tovarA = []
st = j
for x in range(st, len(l)):
    if l[x][1] == 'A':
        tovarA.append(l[x])
j = -1
for x in range(len(tovarA)):
    if sm + buyes[j][0] - tovarA[x][0] >= 0:
        sm = sm + buyes[j][0] - tovarA[x][0]
        ctA += 1
        j -= 1
print(tovarA)
# for x in range(len(buyes) - 1, len(l)):
#     if l[x][1] == 'A' and buyes[j][1] != 'A':
#         if sm + buyes[j][0] - l[x][0] >= 0:
#             sm = sm + buyes[j][0] - l[x][0]
#             ctA += 1
#             j -= 1
#         else:
#             break
#     elif l[x][1] == 'A' and buyes[j][1] == 'A':
#         j -= 1
#         x -= 1
print(ctA, sm)
