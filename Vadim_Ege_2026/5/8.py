def v(x):
    k = ''
    while x>0:
        k += str(x%4)
        x//=4
    return k[::-1] if k != '' else '0'
c =[]
for x in range(0,20000):
    r=v(x)
    if x%2==0:
        r = '12'+ r + v(int(r[-1])*3)
    else:
        r = '13'+r+'21'
    if int(r,4) > 50:
        c.append(int(r,4))
print(min(c))