a = [[int(i) for i in x.split()] for x in open('18.txt')]
a = sorted(a)
sl = {}
m = 5700
ind = 1
for i in a:
    if i[0] not in sl:
        sl[i[0]] = []
    sl[i[0]].append(i[1])
ans = []
ans2 = []
for x in sl:
    sl[x] = sorted(set(sl[x]))
    can = True
    for y in range(ind, m + 1 - 2):
        if y + 2 in sl[x]:
            if can:
                ind = y + 2 + 1
                can = False
            ans2.append(y + 2)
        elif y + 1 in sl[x]:
            if can:
                ind = y + 1 + 1
                can = False
            ans2.append(y + 1)
        elif y in sl[x]:
            if can:
                ind = y + 1
                can = False
            ans2.append(y)
        ####
        if y + 2 not in sl[x] and y + 1 not in sl[x] and y not in sl[x] and y + 2 not in ans2 and y + 1 not in ans2 and y not in ans2:
            ans.append([x, y])


print(ans)










# sl_zan={}
# sl_svob={}
# sl_troik={}
# for i in a:
#     if i[0] not in sl_zan:
#         sl_zan[i[0]]=[i]
#     else:
#         sl_zan[i[0]].append(i)
# for r in range(1,6+1):
#     for m in range(1,9+1):
#         if r not in sl_svob and [r,m] not in sl_zan[r]:
#             sl_svob[r]=[m]
#         elif [r,m] not in sl_zan[r]:
#             sl_svob[r].append(m)
# for r in range(1,6+1):
#     for i in range(len(sorted(sl_svob[r]))-2):
#         if r not in sl_troik and sl_svob[r][i+2]-sl_svob[r][i+1]==1 and sl_svob[r][i+1]-sl_svob[r][i]==1:
#             can = True
#             for j in range(1,r):
#                 if sl_svob[r][i] not in  sl_svob[r-j] or sl_svob[r][i+1] not in sl_svob[r-j] or sl_svob[r][i+2] not in sl_svob[r-j]:
#                     can=False
#                     break
#             if can:
#                 sl_troik[r]=[[sl_svob[r][i],sl_svob[r][i+1],sl_svob[r][i+2]]]
#         elif sl_svob[r][i+2]-sl_svob[r][i+1]==1 and sl_svob[r][i+1]-sl_svob[r][i]==1:
#             can = True
#             for j in range(1, r):
#                 if sl_svob[r][i] not in sl_svob[r - j] or sl_svob[r][i + 1] not in sl_svob[r - j] or sl_svob[r][i + 2] not in sl_svob[r - j]:
#                     can = False
#             if can:
#                 sl_troik[r].append([sl_svob[r][i], sl_svob[r][i + 1], sl_svob[r][i + 2]])
# print(sl_troik)