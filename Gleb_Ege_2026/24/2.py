import string
s = open(r'C:\Users\Zarif\Downloads\340_1 (4).txt').readline()
# glas = 'AIOUYE'
# print(string.ascii_uppercase)
# soglas = 'BCDFGHJKLMNPQRSTVWXZ'
# for x in glas:
#     s = s.replace(x, '#')
# for x in soglas:
#     s = s.replace(x, '@')
# s = s.replace('@@', '@  @')
# s = s.replace('##', '#  #')
# s = s.split('')
# print(s)
# ct = 0
# mx = []
# for x in range(len(s) - 1):
#     if not(s[x] in 'AEOIUY' and s[x + 1] in 'AEOIUY') and not(s[x] not in 'AEOIUY' and s[x + 1] not in 'AEOIUY'):
#         ct += 1
#     else:
#         mx.append(ct + 1)
#         ct = 0
# print(max(mx))