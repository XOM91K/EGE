c = []
for x in range(1,10000):
    r = bin(x)[2:]
    if r.count('1')%2==0:
        r = '1'+r+'00'
    else:
        r = '11'+r
    if int(r,2)>=412:
        print(x)
        break