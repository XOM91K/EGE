# for n in range(4,10000):
#     s = '8' + '7' * n
#     while '57' in s or '877' in s or '777' in s:
#         if '57' in s:
#             s = s.replace('57','7', 1)
#         if '877' in s:
#             s = s.replace('877','75', 1)
#         if '777' in s:
#             s = s.replace('777','8', 1)
#     d = (sum(map(int, str(s))))
#
#     print(d)



for n in range(4,10000):
    s = '8' + '7' * n
    while '57' in s or '877' in s or '777' in s:
        if '57' in s:
            s = s.replace('57','7', 1)
        if '877' in s:
            s = s.replace('877','75', 1)
        if '777' in s:
            s = s.replace('777','8', 1)
    if 5 ** s.count('5') * 7 ** s.count('7') * 8 ** s.count('8') > 1000000:
        print(5 ** s.count('5') * 7 ** s.count('7') * 8 ** s.count('8'))