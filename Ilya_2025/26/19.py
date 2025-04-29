a = sorted([[int(i) for i in x.split()] for x in open('19.txt')])
sl={}
i_maxx=0
ct_max=0
for i in a:
    if i[0] not in sl:
        sl[i[0]]=[]
    sl[i[0]].append(i[1])
# for i in sl:
#     if len(sl[i])>=2:
#         ll=[]
#         l = sorted(list(set(sl[i])))
#         ct=0
#         dlin =1
#         for n in range(len(l) - 1):
#             if abs(l[n + 1] - l[n]) == 2:
#                 dlin += 1
#                 ll.append(l[n])
#                 ll.append(l[n + 1])
#             else:
#                 ct = max(ct, dlin)
#                 ct = max(ct, len(set(ll)))
#                 ll = []
#                 dlin = 1
#         ct = max(ct, len(set(ll)))
#         if ct_max<=ct:
#             ct_max=ct
#             i_maxx = max(i_maxx, i)
#             #print(i_maxx, ct)
for i in sl:
    if len(sl[i])>=2:
        ll=[]
        l = sorted(list(set(sl[i])))
        ct=0
        dlin =1
        for n in range(len(l) - 1):
            if abs(l[n + 1] - l[n]) == 2:
                dlin += 1
                if dlin == 42:
                    print(i)
                ll.append(l[n])
                ll.append(l[n + 1])
            else:
                ct = max(ct, dlin)
                ct = max(ct, len(set(ll)))
                ll = []
                dlin = 1
