import itertools
ct = 0
for x in itertools.product('НИКОЛАЙ', repeat=4):
    x = ''.join(x)
    x = x.replace("И", '-')
    x = x.replace("О", '-')
    x = x.replace("А", '-')
    if x[0] != 'Й' and x.count('-') >= 1:
        ct += 1
print(ct)