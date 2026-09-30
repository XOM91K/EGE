s = open('/Users/zarif/Downloads/1628_1.txt').readlines()
import string
print(string.ascii_uppercase)
mxln = []
for x in s:
    if x.count('A') < 25:
        for y in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if y in x:
                lt = x.find(y)
                rt = x.rfind(y)
                mxln.append(rt - lt)
print(max(mxln))