import collections
s = 'Hello, hello! World world.'.lower()
sl = {}
for x in s:
    if not x.isalpha() and x != ' ':
        s = s.replace(x, '')
s = s.split()
print(dict(collections.Counter(s)))
# for x in s:
#     if x not in sl:
#         sl[x] = 0
#     sl[x] += 1
# print(s)
# print(sl)