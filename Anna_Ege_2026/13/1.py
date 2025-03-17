import ipaddress
ct = 0
for x in ipaddress.ip_network('90.65.32.0/255.255.224.0'):
    #x = str(x).split('.')
    #x = ''.join([bin(int(y))[2:].zfill(8) for y in x])
    #x = f'{x:b}'
    x = bin(int(x))[2:].zfill(32)
    if x.count('0') == x.count('1'):
        ct += 1
print(ct)
# a = 5
# b = 6
# print('У Гриши есть', a, 'яблок, а у Олега есть', b, 'бананов')
# print(f'У Гриши есть {a} яблок, а у Олега есть {b} бананов')