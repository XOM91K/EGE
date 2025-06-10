import ipaddress
ct = 0
for x in ipaddress.ip_network('192.168.32.48/255.255.255.192', False):
    #x = f'{x:b}'
    #x = ''.join([bin(int(d))[2:].zfill(8) for d in str(x).split('.')])
    x = bin(int(x))[2:].zfill(32)
    if x.count('1') % 5 != 0:
        print(x)
        ct += 1
print(ct)