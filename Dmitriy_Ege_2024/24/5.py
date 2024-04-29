mxct = []
s = open(r'24_622_1.txt').readline()
s = s.split('D')
for x in s:
    if x.count('O') <= 2:
        mxct.append(len(x) + 2)
print(max(mxct))