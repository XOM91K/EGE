# N = int(input())
# for i in range(100, 1000):
#     sm_cif = int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2])
#     if sm_cif == N:
#         print(i)
# sm = 0
# ct = 0
# for x in range(11, 100, 2):
#     sm += x
#     ct += 1
# print(sm / ct)
# d = 1234
# print(sum([int(i) for i in str(d)]))
# d = 498
# print(d // 100)
# print(d // 10 % 10)
# print(d % 10)
# d = 123
# print(int(str(d)[0]) + int(str(d)[1]) + int(str(d)[2]))
s = 'aaabaaee'
ct = 0
for i in s:
    if i not in 'aeouiy':
        ct += 1
print(ct)