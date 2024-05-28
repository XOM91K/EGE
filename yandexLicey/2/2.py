s = input().split('&')
lst = []
g = ''
for x in s:
    if len(x.split(' ')) > 1 and all([y.isalnum() or y.isspace() for y in x]):
        x = x.split(' ')
        lst.append(x[0].title() + ' ' + x[-1].title())
    elif len(x) % 3 == 0:
        x = ''.join([x[d].upper() if x[d].islower() else x[d].lower() for d in range(0, len(x), 3)])
        lst.append(x)
    else:
        lst.append(x[::-1].upper())
for x in lst:
    g += x + ', '
print(g[:-2])
