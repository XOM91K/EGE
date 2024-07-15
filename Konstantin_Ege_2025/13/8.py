import ipaddress
d = []
for A in range(0, 256):
    try:
        for x in ipaddress.ip_network('108.8.190.123/255.255.' + str(A) + '.0', False):
            x = f'{x:b}'
            if x[:16].count('1') > x[16:].count('1'):
                break
        else:
            d.append(A)
    except:
        print('Ошибка')
print(d)