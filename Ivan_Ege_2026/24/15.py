import collections
l = open('15.txt').readlines()
ll = open('15.txt').read()
s = ''
mxQ = 0
for x in l:
    mxQ = max(mxQ, x.count('Q'))
for x in l:
    if x.count('Q') == mxQ:
        print(collections.Counter(x))
print(ll.count('C'))
# sq = 0
# for e in l:
#     if e.count('Q') >= sq:
#         s = e
#         sq = e.count('Q')
# print(s)
# a = sorted(set(s[:-1]))
# print(a)
# b = a[0]
# bn = s.count(b)
# for e in a:
#     if s.count(e) < bn:
#         b = e
#         bn = s.count(e)
# c = 0
# for e in l:
#     c += e.count(b)
# print(b, c)