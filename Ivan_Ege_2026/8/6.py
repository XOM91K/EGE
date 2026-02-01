import itertools
k = 0
k2 = 0
for x in itertools.product(sorted('привычка'), repeat=5):
    x = ''.join(x)
    k += 1
    if k % 5 != 0:
        k2 += 1
        print(k2, x)
# a = set(itertools.product('привычка', repeat = 5))
# print(a)
# s = []
# for i in range(0, len(a), 5):
#     s.append(a[i])
#     s.append(a[i+1])
#     s.append(a[i+2])
#     s.append(a[i+3])
# for i in range(len(s)):
#     if l[i] in itertools.permutations('првчк'):
#         print(i+1)
#         break

# import itertools
# a = itertools.product('привычка', repeat = 5)
# a = sorted(a)
# s = []
# for i in range(0, len(a)-4, 5):
#     s.append(a[i])
#     s.append(a[i+1])
#     s.append(a[i+2])
#     s.append(a[i+3])
# for i in range(len(s)):
#     if s[i] in itertools.permutations('првчк'):
#         print(i+1)
#         break