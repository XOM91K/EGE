import ipaddress
ct = 0
for x in ipaddress.ip_network('90.65.32.0/255.255.224.0', False):
    #1-й способ x = ''.join([bin(int(d))[2:].zfill(8) for d in str(x).split('.')])
    #2-й способ x = f'{x:b}'
    x = bin(int(x))[2:].zfill(32)
    if x.count('1') == x.count('0'):
        ct += 1
print(ct)
# a = 6
# o = 12
# print('У Марии есть', a, 'яблок, а у Оли есть', o, 'апельсинов')
# print(f'У Марии есть {a} яблок, а у Оли есть {o} апельсинов') #format-строка