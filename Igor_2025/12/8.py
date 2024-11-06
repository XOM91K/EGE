# ct = 0
# for N in range(0, 100):
#     s = '1' * N
#     while '111' in s:
#         s = s.replace('111', '2', 1)
#         s = s.replace('222', '11', 1)
#         s = s.replace('1', '2', 1)
#     if len(s) == 3:
#         ct += 1
ct = 0
for N in range(234567900, 789012346):
    if N >= 3 and (N - 3) % 2 == 0:
        ct += 1