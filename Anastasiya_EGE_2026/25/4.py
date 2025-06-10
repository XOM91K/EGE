import fnmatch as f
def is_prime(d):
    for x in range(2, int(d ** 0.5) + 1):
        if d % x == 0:
            return False
    return d > 1
for i in range(2627, 10**9, 2627):
    if f.fnmatch(str(i), '7*53?3*1') and is_prime(sum(map(int, str(i)))):
        print(i, i//2627)
# s = 2182
# s = str(s)
# # '2182' [2, 1, 8, 2]
# print(sum(map(int, s)))
# print(s.count('2') * 2 + s.count('1') * 1 + s.count('8') * 8)
# sm = 0
# for x in s:
#     sm += int(x)
# print(sm)