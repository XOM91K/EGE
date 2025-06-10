import time

start = time.time()
print(start)
for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if (((x % 13 == 0) <= (not (40 <= x <= 60))) or (A < x + 20)) == 0:
            can = False
            break

    if can:
        print(A)
finish = time.time()
print(finish - start)
# import time
# start = time.time()
# print(start)
# for A in range(1, 1000):
#     k = 0
#     for x in range(1, 1000):
#         if (((x % 13 == 0) <= (not(40 <= x <= 60))) or (A < x + 20)) == 1:
#             k += 1
#         else:
#             break
#
#     if k == 999:
#         print(A)
# finish = time.time()
# print(finish - start)
