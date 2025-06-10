import itertools
cnt=0
for x in itertools.product("012345678",repeat=7):
    x="".join(x)
    if x.count("6")>=1 and x[0] not in '01357' and x[-1] in '125478':
        cnt+=1
print(cnt,x)