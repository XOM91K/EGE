import itertools
cnt=0
for x in itertools.permutations("0123456789",7):
    x="".join(x)
    if int(x)%5==0 and x[0]!="0":
        x = x.replace('0', '@')
        x = x.replace('2', '@')
        x = x.replace('4', '@')
        x = x.replace('6', '@')
        x = x.replace('8', '@')
        x = x.replace('1', '#')
        x = x.replace('3', '#')
        x = x.replace('5', '#')
        x = x.replace('7', '#')
        x = x.replace('9', '#')
        if '@@' not in x and '##' not in x:
            cnt+=1
print(cnt)
