s = open(r'C:\Users\Zarif\Downloads\24_2508.txt').readlines()
s = ''.join(s).count('C')
print(s)

# import collections
# mxQ = 0
# st = ''
# for x in s:
#     if x.count('Q') >= mxQ:
#         mxQ = x.count('Q')
#         st = x
# print(collections.Counter(st))