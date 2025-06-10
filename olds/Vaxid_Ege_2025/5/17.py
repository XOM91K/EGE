import string
print(string.ascii_uppercase)
alf = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXY'
def v35(d):
    s = ''
    while d > 0:
        s += str(alf[d % 35])
        d //= 35
    return s[::-1]
for N in range(1, 10000):
    R = v35(N)
    if R.isdigit():
        R += 'GGWP'
    else:
        for x in 'ABCDEFGHIJKLMNOPQRSTUVWXY':
            R = R.replace(x, 'W')
    R = int(R, 35)
    if R > 123456789:
        print(N)


# d = '123981261298312631293m12398'
# if d.isdigit():
#     print('True')