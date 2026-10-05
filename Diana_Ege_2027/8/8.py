import itertools
ct=0
for x in itertools.product("0123456789",repeat=7):
    x="".join(x)
    if x[0]!="0":
        if x[-1]=="0" or  x[-1]=="5":
            if len(set(x))==7:
                for y in '13579':
                    x=x.replace(y,'#')
                for y in '02468':
                    x=x.replace(y,"@")
                if '@@' not in x and '##' not in x :
                    ct+=1
print(ct)