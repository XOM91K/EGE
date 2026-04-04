import tqdm
l = [[int(d) for d in x.split()] for x in open('14.txt')]
# l = sorted(l, key=lambda d: (d[0], -d[1]))
# K = 1236147000
# ct = 0
# start_int = 0
# end_int = K
# for x in l:
#     if x[0] <= K < x[1]:
#         start_int = x[0]
#         end_int = x[1]
#         ct += 1
#         if end_int - start_int == 0:
#             break
# print(ct)
# mx = max(max(l, key=max))
# K = 1236147000
# time = [0] * (mx - K)
# print(len(time))
# for x in tqdm.tqdm(range(len(time))):
#     for y in l:
#         if y[0] <= x + K < y[1] or (y[0] == 0 and x + K < y[1]) or (y[1] == 0 and x + K >= y[0]) or (y[0] == 0 and y[1] == 0):
#             time[x] += 1
# mx = max(time)
# print(mx)
# ct = 0
# for x in time:
#     if x == mx:
#         ct += 1
# print(ct)