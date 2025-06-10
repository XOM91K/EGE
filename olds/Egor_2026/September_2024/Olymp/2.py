N = int(input())
l = []
for i in range(N):
    l.append(i + 1)
K = int(input())
ind = 0
while True:
    if ind % 3 == 0:
        if l[ind] == K:
            print('Yes')
            print(len(l))
            break
    elif ind % 3 == 1:
        if l[ind] == K:
            print('No')
            print(len(l))
            break
    elif ind % 3 == 2:
        l.append(l[ind])
    ind += 1
