# def trio(num):
#     ans = ""
#     while num > 0:
#         ans += str(num % 3)
#         num = num // 3
#     return ans[::-1]
# mn = []
# for i in range(11, 1000):
#     x = trio(i)
#     even = x.count('2') + x.count('0')
#     odd = x.count('1')
#     if even > odd:
#         x = "22" + x
#     else:
#         x = "11" + x
#     x = int(x, 3)
#     if x > 100:
#         mn.append(x)
# print(sorted(mn))
print(int('0001011100001001', 2))