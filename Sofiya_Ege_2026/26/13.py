l  = [[d for d in x.split()] for x in open('13.txt')]
sl = {}
print(l)
# for x in l:
#     if int(x[0]) not in sl:
#         sl[int(x[0])] = []
#     sl[int(x[0])].append([int(x[1]), x[2]])
# for x in sl:
#     print(x, sl[x])
# print(sl)
# ll = [['*'] * 10000] * 10000
# ll[0][2] = 'RED'
# print(ll[5])
# print(ll[3])
# for x in l:
#     if x[2] == '#00FF00':
#         ll[int(x[0])][int(x[1])] = 'G'
#     elif x[2] == '#FF0000':
#         ll[int(x[0])][int(x[1])] = 'R'
#     elif x[2] == '#0000FF':
#         ll[int(x[0])][int(x[1])] = 'B'
# for x in range(len(ll)):
#     ll[x] = ''.join(ll[x])
# for x in ll:
#     print(x)
l = [1, 2, 3]
d = l.copy()
d.append(100)
print(d)
print(l)