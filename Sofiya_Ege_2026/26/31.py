l=open('31.txt')
lt=[0]*366
yach=[]
for y in range(200):
    yach.append([0, 0])
ct=0
for s in l:
    st,k=[int(d)for d in s.split()]
    for y in range(len(yach)):
        if st>yach[y][0]:
            yach[y][0] = k
            break
    for i in range(st, k + 1):
        lt[i] += 1

lt = [str(x) for x in lt]
for y in range(len(lt)):
    if int(lt[y]) < 200:
        lt[y] = '#'
lt = ''.join(lt).split('#')
ct = 0
mx = []
for y in lt:
    if y != '':
        ct += 1
        mx.append(y.count('200'))
print(ct, max(mx))
