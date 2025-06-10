import re
a = [i.strip() for i in open('13.txt')]

res = []
for item in a:
    if re.match('195.2\d*.\d\d*.14', item):
        res.append(item)
print(len(set(res)))