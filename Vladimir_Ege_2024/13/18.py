import ipaddress
ct = 0
for x in ipaddress.ip_network('192.168.32.160/255.255.255.240', False):
    #x = ''.join([bin(int(d))[2:] for d in str(x).split('.')])
    x = f'{x:b}'
    if x.count('0') > 21:
        ct += 1
print(ct)