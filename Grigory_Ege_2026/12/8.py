n='3'*6+'4'*75
while '35' in n or '355' in n or '3444' in n :
    if '35' in n :
        n=n.replace('35','4',1)
    else:
        if '355' in n :
            n=n.replace('355','4',1)
        else:
            n=n.replace('3444','3')
print(n)