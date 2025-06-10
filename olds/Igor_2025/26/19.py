l = [[int(d) for d in x.split()] for x in open('19.txt')]
l = sorted(l)
st = l[0][0]
ed = 0
z = -1
sm = 0
for i in range(len(l) - 1):
    if i > z:
        st = l[i][0]
    if l[i + 1][0] <= l[i][1]:
        ed = l[i + 1][1]
        st = min(st, l[i][0])
    else:
        z = i
        sm += abs(st - ed)
print(sm)






















# mx_time = 0
# sm = 0
# #d = []
# med = 0
# for i in range(len(l)):
#     st = l[i][0]
#     ed = l[i][1]
#     for y in range(i, len(l)):
#         if l[y][0] <= ed:
#             ed = max(ed, l[y][1])
#         else:
#             time = abs(st - ed)
#             mx_time = max(mx_time, time)
#
#             break
#     if ed > med:
#         med = ed
#         sm += mx_time
#     #d.append(ed)
# # r = [d[0]]
# # for x in range(len(d) - 1):
# #     m = r[-1]
# #     if d[x] > m:
# #         r.append(d[x])
# print(sm)
# print(mx_time)