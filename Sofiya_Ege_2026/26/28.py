l=[[d for d in x.split()]for x in open('28.txt')]
sl={}
for x in l:
    if int(x[0]) not in sl:
        sl[int(x[0])]=[]
    sl[int(x[0])].append([int(x[1]), 'G' if x[2] == '#00FF00' else 'B' if x[2] == '#0000FF' else 'R'])
# for x in sl:
#     for y in range(len(sl[x])):
#         if sl[x][y][1] == 'G':
#
lt=[]
for y in range(10000):
    lt.append(['*'] * 10000)
for x in sl:
    for y in range(len(sl[x])):
        lt[x][sl[x][y][0]] = sl[x][y][1]
# print(lt[0][:10], lt[1][:10])
ct = 0
mx_k = 0
for x in range(len(lt)):
    k = 0
    lt[x] = ''.join(lt[x])
    b = lt[x]
    for y in range(len(lt[x])):
        if lt[x][y] == 'G' and lt[x][y - 3: y] == 'BBB' and lt[x][y + 1: y + 4] == 'BBB':
            ct += 1
            k += 1
    if k == 2:
        print(x)
    mx_k = max(mx_k, k)
print(ct, mx_k)
# lt[0][3] = '#'
# print(lt[0][:5], lt[1][:5])
# for x in l:
#     if x[2]=='#00FF00':
#         lt[int(x[0])][int(x[1])]='G'
#     elif x[2]=='#0000FF':
#         lt[int(x[0])][int(x[1])]='B'
# for x in range(len(lt)):
#     lt[x]=''.join(lt[x])
# d=[]
# for x in lt:
#     d.append(x.count('BBBGBBB'))
#     print((max(d)))
# print(len(d))
# BBBGBBBGBBB