#
# for x in range(1, 1000):
#     try:
#         s = open(f'{x}.txt').readline()
#         if 'vsosh' in s:
#             print(s)
#     except:
#         pass
import collections as cl
s = 'sdaiudhiduqgwdiquwgdquidqwgdiwqudgsiugdqiwudgqwdiufgdasiudfqwuidfqwuidwqfdiuwdwqdq'
print(cl.Counter(s))